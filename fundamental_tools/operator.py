def priority(op):
    """
    return operator priority
    :return: returns an integer, with a higher number representing a higher priority of operation.
    + - * /
    """
    if op == '+' or op == "-":
        return 1
    if op == "*" or op == "/":
        return 2


def add(*args):
    return sum(args)


def minus(minuend, subtrahend):
    return minuend - subtrahend


def multiply(*args):
    result = 1
    for item in args:
        result *= item
    return result


def division(dividend, divisor):
    pass


class Operator(object):
    operator = []

    def __init__(self):
        self.operator = ["+", "-", "*", "/", "sin", "cos", "tan", "sec", "csc", "cot"]

    def is_operator(self, op):
        """
        check whether it is a valid operator
        :param : op
        :return: boolean result.py
        """
        if op in self.operator:
            return True

    def calculate(self, operator, *args):
        pass
