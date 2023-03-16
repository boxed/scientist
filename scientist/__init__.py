from datetime import date
import time


def check_candidate(a, candidate, callback_when_different, *args, **kwargs):
    control_result = None
    candidate_result = None
    control_exception = None
    candidate_exception = None
    reason = None

    try:
        control_result = a(*args, **kwargs)
    except BaseException as e:
        control_exception = e

    try:
        candidate_result = candidate(*args, **kwargs)
        if control_exception is not None:
            reason = 'old code raised, new did not'

        elif control_result != candidate_result:
            reason = 'different results'

    except BaseException as e:
        candidate_exception = e
        if control_exception is None:
            reason = 'new code raised, old did not'
        else:
            if type(control_exception) != type(candidate_exception):
                reason = 'new and old both raised exception, but different types'
            elif control_exception.args != candidate_exception.args:
                reason = 'new and old both raised exception, but with different data'

    if reason is not None:
        callback_when_different(
            control_result=control_result,
            candidate_result=candidate_result,
            control_exception=control_exception,
            candidate_exception=candidate_exception,
            reason=reason,
        )

    if control_exception is not None:
        raise control_exception

    return control_result


class Foo:
    def foo(self):
        def nested_foo():
            return 4

        return nested_foo()


def foo():
    def nested_foo():
        return 4

    def nested_bar():
        return 4

    return nested_foo()
