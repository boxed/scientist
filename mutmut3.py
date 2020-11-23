# from datetime import datetime
from datetime import datetime

from mutmut import (
    list_mutations,
    Context,
    mutate,
)
from parso import parse


def create_mutants():

    with open('scientist_mutants.py', 'w') as out:

        # start = datetime.now()
        c = Context(filename='scientist/__init__.py')
        orig_name = c.ast.children[0].name.value
        c.ast.children[0].name.value += '_orig'
        print(c.get_code(), file=out)
        c.ast.children[0].name.value = orig_name

        mutation_ids = list_mutations(c)
        mutant_names = []

        for i, mutation_id in enumerate(mutation_ids):
            print(file=out)
            print('# ---------- ', file=out)
            c.mutation_id = mutation_id
            new_code, number = mutate(c)
            c.ast.children[0].name.value += f'_mutant_{i}'
            mutant_names.append(c.ast.children[0].name.value)
            assert number == 1, number
            print(c.get_code(), file=out)
            c.ast.children[0].name.value = orig_name

        print(f'{orig_name}_mutants = {{' + ', '.join(f'"{i}": {m}' for i, m in enumerate(mutant_names)) + '}', file=out)

        # trampoline
        print("""
def trampoline(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ.get('MUTANT_UNDER_TEST', None)
    return mutants.get(mutant_under_test, orig)(*args, **kwargs)""", file=out)

        f = c.ast.children[0]
        signature = f.children[2].get_code()

        # this is actually wrong, because the signature can be "(foo, *, bar)" which is invalid at the call site, need to fix this at some point
        call = signature[1:-1]  # the slice is to remove the parens

        # Replace body with trampoline
        trampoline_ast = parse(f"""
def {orig_name}{signature}:
    return trampoline({orig_name}_orig, {orig_name}_mutants, {call})""")

        f.children[-1] = trampoline_ast.children[0].children[-1]

        print(f.get_code(), file=out)

        # print()
        #
        # t = datetime.now() - start
        # print(len(mutation_ids), len(mutation_ids) / t.total_seconds(), 'mutations per s')


def mutmut_3():
    start = datetime.now()
    create_mutants()
    time = datetime.now() - start
    print('mutation generation', time)

    import sys
    import scientist_mutants
    sys.modules['scientist'] = scientist_mutants
    import os
    import hammett

    print('running baseline...', end='')
    if hammett.main(fail_fast=True, disable_assert_analyze=True) != 0:
        print("FAILED")
        return
    print('done')

    start = datetime.now()

    # manual fork
    key_from_pid = {}
    for key in scientist_mutants.check_candidate_mutants.keys():
        pid = os.fork()
        if not pid:
            os.environ['MUTANT_UNDER_TEST'] = key
            # In the child
            result = hammett.main(quiet=True, fail_fast=True, disable_assert_analyze=True)
            if result != 0:
                # os.write(write, b'x')
                # TODO: write failure information to stdout?
                pass
            os._exit(result)
        else:
            key_from_pid[pid] = key

    result_by_key = {}
    try:
        while True:
            pid, status = os.wait()
            result_by_key[key_from_pid[pid]] = (0xFF00 & status) >> 8  # The high byte contains the exit code
    except ChildProcessError:
        pass

    print(result_by_key)
    covered = {k for k, v in result_by_key.items() if v != 0}
    not_covered = {k for k, v in result_by_key.items() if v == 0}
    print('covered: ', covered)
    print('not covered: ', not_covered)

    t = datetime.now() - start
    print(t, len(scientist_mutants.check_candidate_mutants), len(scientist_mutants.check_candidate_mutants) / t.total_seconds(), 'mutations per s')


if __name__ == '__main__':
    mutmut_3()

