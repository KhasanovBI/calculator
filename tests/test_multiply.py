def test_multiply_of_ints(calculator):
    assert calculator.multiply(5, 2) == 10


def test_commutativity_of_multiply_of_ints(calculator):
    assert calculator.multiply(2, 5) == calculator.multiply(5, 2)


def test_multiply_of_int_and_float(calculator):
    assert calculator.multiply(12, 0.1) == 1.2


def test_commutativity_of_multiply_of_int_and_float(calculator):
    assert calculator.multiply(3.2, 5) == calculator.multiply(5, 3.2)


def test_multiply_of_floats(calculator):
    assert calculator.multiply(5.2, 1.2) == 6.24


def test_commutativity_of_multiply_of_floats(calculator):
    assert calculator.multiply(1.2, 5.23) == calculator.multiply(5.23, 1.2)


def test_negative_multiply(calculator):
    assert calculator.multiply(3, 4) != -12
