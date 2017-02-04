

def test_add_of_ints(calculator):
    assert calculator.add(5, 1) == 6


def test_commutativity_of_add_of_ints(calculator):
    assert calculator.add(1, 5) == calculator.add(5, 1)


def test_add_of_int_and_float(calculator):
    assert calculator.add(5, 3.22) == 8.22


def test_commutativity_of_add_of_int_and_float(calculator):
    assert calculator.add(3.2, 5) == calculator.add(5, 3.2)


def test_add_of_floats(calculator):
    assert calculator.add(0.1, 0.2) == 0.3


def test_commutativity_of_add_of_floats(calculator):
    assert calculator.add(1.2, 5.23) == calculator.add(5.23, 1.2)


def test_negative_add(calculator):
    assert calculator.add(3, 4) != -7
