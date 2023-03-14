import os
from datetime import datetime
from os import (
    makedirs,
    walk,
)
from pathlib import Path

from mutmut import (
    guess_paths_to_mutate,
    list_mutations,
    Context,
    mutate,
)
from parso import parse
from tqdm import tqdm

from rich.traceback import install
install(show_locals=True)

from inspect import signature


def foo(a, *, b: int, **kwargs):
    pass


signature(foo)


def create_mutants():
    paths = [guess_paths_to_mutate()]
    next_id = 0
    for path in paths:
        for root, dirs, files in walk(path):
            for filename in files:
                if not filename.endswith('.py'):
                    continue
                if filename.endswith('__tests.py'):
                    continue
                if filename.startswith('test_.py'):
                    continue
                next_id = create_mutants_for_file(Path(root) / filename, next_id=next_id)
    return next_id


def write_trampoline(out, orig_name, mutant_names):
    print(file=out)

    def index(s):
        return s.rpartition('_')[-1]

    print(f'{orig_name}_mutants = {{' + ', '.join(f'"{index(m)}": {m}' for m in mutant_names) + '}', file=out)

    print(file=out)
    print(file=out)
    print(f"""
def {orig_name}(*args, **kwargs):
    return trampoline({orig_name}_orig, {orig_name}_mutants, *args, **kwargs)  
""", file=out)
    print(f'{orig_name}.__signature__ = __signature({orig_name}_orig)', file=out)


def write_mutant(out, c, mutation_id, next_id, mutant_names, orig_name):
    if not mutation_id.subject_stack:
        return
    print(file=out)
    c.mutation_id = mutation_id
    new_code, number = mutate(c)
    node = mutation_id.subject_stack[-1]
    node.name.value += f'_mutant_{next_id}'
    mutant_names.append(node.name.value)
    # assert number == 1, number
    if number != 1:
        print(f'warning: got {number} mutations when mutating {mutation_id}')
    print(node.get_code(), file=out)
    node.name.value = orig_name


def write_original_alias(out, last_subject_stack):
    orig_name = last_subject_stack[-1].name.value
    print(f'{orig_name}_orig = {orig_name}', file=out)  # the trampoline will then overwrite the original


def write_trampoline_impl(out):
    # language=python
    print("""
from inspect import signature as __signature


def trampoline(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ.get('MUTANT_UNDER_TEST', None)
    return mutants.get(mutant_under_test, orig)(*args, **kwargs)""", file=out)


def create_mutants_for_file(filename, next_id):
    output_path = Path('mutants') / filename
    makedirs(output_path.parent, exist_ok=True)

    input_stat = os.stat(filename)

    if output_path.exists() and output_path.stat().st_mtime == input_stat.st_mtime:
        print('    skipped', output_path, 'already up to date')
        return int(os.getxattr(output_path, 'user.next_id').decode())

    with open(output_path, 'w') as out:
        c = Context(filename=filename)
        print(c.source, file=out)
        write_trampoline_impl(out)

        mutation_ids = list_mutations(c)

        mutant_names = []
        last_subject_stack = None

        for mutation_id in mutation_ids:
            if not c.subject_stack:
                continue

            # TODO: mutate methods too!, then we have a classdef then a funcdef in the stack
            if c.subject_stack[0].type != 'funcdef':
                continue

            if last_subject_stack != c.subject_stack:
                if last_subject_stack:
                    write_original_alias(out, last_subject_stack)

                if mutant_names:
                    write_trampoline(out, orig_name, mutant_names)

                orig_name = c.subject_stack[0].name.value
                mutant_names = []
                last_subject_stack = c.subject_stack

            write_mutant(out, c, mutation_id, next_id, mutant_names, orig_name)

            next_id += 1

        if last_subject_stack:
            write_original_alias(out, last_subject_stack)

        if mutant_names:
            write_trampoline(out, orig_name, mutant_names)

    os.utime(output_path, (input_stat.st_atime, input_stat.st_mtime))
    os.setxattr(output_path, 'user.next_id', str(next_id).encode())

    return next_id


def mutmut_3():
    start = datetime.now()
    print('generating mutants...')
    next_id = create_mutants()
    time = datetime.now() - start
    print('mutation generation', time)

    import sys
    sys.path.insert(0, 'mutants')
    import os
    import hammett

    print('running baseline...', end='')
    if hammett.main(fail_fast=True, disable_assert_analyze=True) != 0:
        print("FAILED")
        return
    print('done')

    # manual fork
    result_by_key = {}

    def read_one_child_exit_status():
        pid, status = os.wait()
        # print('got exit', pid)
        result_by_key[key_from_pid[pid]] = (0xFF00 & status) >> 8  # The high byte contains the exit code

    hammett_kwargs = hammett.main_setup(quiet=True, fail_fast=True, disable_assert_analyze=True)

    key_from_pid = {}
    running_children = 0
    max_children = 1

    start = datetime.now()

    for key in tqdm(range(next_id)):
        pid = os.fork()
        if not pid:
            # print('in child', os.getpid())
            # In the child
            os.environ['MUTANT_UNDER_TEST'] = str(key)

            # TODO: this is needed for non-memory DBs
            # hammett.Config.workerinput = dict(workerinput=f'_{key}')

            result = hammett.main_run_tests(**hammett_kwargs)
            if result != 0:
                # TODO: write failure information to stdout?
                pass
            # print('exiting', os.getpid())
            os._exit(result)
        else:
            # print('in master', pid)
            key_from_pid[pid] = key
            running_children += 1

        if running_children >= max_children:
            read_one_child_exit_status()
            running_children -= 1

    try:
        # print('waiting at the end')
        while running_children:
            read_one_child_exit_status()
            running_children -= 1
    except ChildProcessError:
        pass

    t = datetime.now() - start

    covered = {k for k, v in result_by_key.items() if v != 0}
    not_covered = {k for k, v in result_by_key.items() if v == 0}
    print('covered: ', covered)
    print('not covered: ', not_covered)

    print('time:', t)
    print('next ID:', next_id)
    print('mutations/s:', int(next_id / t.total_seconds()))


if __name__ == '__main__':
    mutmut_3()
