import pytest

from calculator.core import Calculator


@pytest.fixture(scope='session')
def calculator():
    return Calculator()
