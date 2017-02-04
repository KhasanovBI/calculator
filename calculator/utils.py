from decimal import localcontext, Context, Decimal


def round_result(function):
    def function_wrapper(*args):
        with localcontext(Context(10)):
            return float(function(*map(lambda x: Decimal(str(x)), args)))

    return function_wrapper
