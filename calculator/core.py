from calculator.utils import round_result


class Calculator(object):
    @staticmethod
    @round_result
    def add(a, b):
        return a + b

    @staticmethod
    @round_result
    def subtract(a, b):
        return a - b

    @staticmethod
    @round_result
    def multiply(a, b):
        return a * b

    @staticmethod
    @round_result
    def divide(a, b):
        return a / b
