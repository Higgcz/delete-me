import pytest

from delete_me.example import fib


def test_input_above_zero():
    with pytest.raises(ValueError):
        fib(-1)


def test_input_is_int():
    with pytest.raises(TypeError):
        fib(0.1)


@pytest.mark.parametrize(
    "number,expected",
    [
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 3),
        (5, 5),
        (6, 8),
        (7, 13),
        (8, 21),
        (9, 34),
        (10, 55),
        (11, 89),
        (12, 144),
        (13, 233),
        (14, 377),
    ],
)
def test_evaluation(number, expected):
    assert fib(number) == expected
