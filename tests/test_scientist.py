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


def test_different_return_value():
    def callback(**kwargs):
        pass

    assert check_candidate(
        lambda: 1,
        lambda: 2,
        callback,
    ) == 1
