import pytest
from scientist import check_candidate

control_exception = TypeError('asd')
candidate_exception = TypeError('asd')


def control_raises():
    raise control_exception


def candidate_raises():
    raise candidate_exception


# Tests for the two cases success cases

def test_golden_path():
    def callback(**_):
        assert False

    assert check_candidate(
        lambda a, b: a + b,
        lambda a, b: a + b,
        callback,
        1,
        b=2,
    ) == 3


def test_both_throws():
    def callback(**_):
        assert False

    with pytest.raises(TypeError) as e:
        check_candidate(control_raises, candidate_raises, callback)

    assert e.value is control_exception


# Tests for the failure cases

def test_old_code_raised_new_code_did_not():
    callback_kwargs = {}

    def callback(**kwargs):
        callback_kwargs.update(kwargs)

    with pytest.raises(TypeError) as e:
        check_candidate(
            control_raises,
            lambda: 1,
            callback,
        )

    assert e.value is control_exception

    assert callback_kwargs == dict(
        control_result=None,
        candidate_result=1,
        control_exception=control_exception,
        candidate_exception=None,
        reason='old code raised, new did not',
    )


def test_different_return_value():
    callback_kwargs = {}

    def callback(**kwargs):
        callback_kwargs.update(kwargs)

    assert check_candidate(
        lambda: 1,
        lambda: 2,
        callback,
    ) == 1

    assert callback_kwargs == dict(
        control_result=1,
        candidate_result=2,
        control_exception=None,
        candidate_exception=None,
        reason='different results',
    )


def test_new_code_raised_old_code_did_not():
    callback_kwargs = {}

    def callback(**kwargs):
        callback_kwargs.update(kwargs)

    assert check_candidate(
        lambda: 1,
        candidate_raises,
        callback,
    ) == 1

    assert callback_kwargs == dict(
        control_result=1,
        candidate_result=None,
        control_exception=None,
        candidate_exception=candidate_exception,
        reason='new code raised, old did not',
    )


def test_both_throws_but_different_types():
    callback_kwargs = {}

    def callback(**kwargs):
        callback_kwargs.update(kwargs)

    wrong_exception = ValueError()

    def candidate_raises_wrong_type():
        raise wrong_exception

    with pytest.raises(TypeError) as e:
        check_candidate(control_raises, candidate_raises_wrong_type, callback)

    assert e.value is control_exception

    assert callback_kwargs == dict(
        control_result=None,
        candidate_result=None,
        control_exception=control_exception,
        candidate_exception=wrong_exception,
        reason='new and old both raised exception, but different types',
    )


def test_both_throws_but_different_data():
    callback_kwargs = {}

    def callback(**kwargs):
        callback_kwargs.update(kwargs)

    wrong_exception = TypeError('wrong data!')

    def candidate_raises_wrong_type():
        raise wrong_exception

    with pytest.raises(TypeError) as e:
        check_candidate(control_raises, candidate_raises_wrong_type, callback)

    assert e.value is control_exception

    assert callback_kwargs == dict(
        control_result=None,
        candidate_result=None,
        control_exception=control_exception,
        candidate_exception=wrong_exception,
        reason='new and old both raised exception, but with different data',
    )
