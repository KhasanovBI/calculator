def test_subtract_of_ints(calculator):
    assert calculator.subtract(1, 5) == -4


def test_subtract_of_int_and_float(calculator):
    assert calculator.subtract(5, 3.22) == 1.78


def test_subtract_of_floats(calculator):
    assert calculator.subtract(5.3, 1.2) == 4.1


def test_negative_subtract(calculator):
    assert calculator.subtract(4, 3) == -1
