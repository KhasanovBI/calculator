import pytest


def test_divide_of_ints(calculator):
    assert calculator.divide(5, -2) == -2.5


def test_divide_of_int_and_float(calculator):
    assert calculator.divide(5, 3.2) == 1.5625


def test_divide_of_floats(calculator):
    assert calculator.divide(0.3, 0.1) == 3


def test_divide_by_zero(calculator):
    with pytest.raises(ZeroDivisionError):
        calculator.divide(3, 0)


def test_negative_divide(calculator):
    assert calculator.divide(3, 4) != -7
