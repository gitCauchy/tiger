from decimal import Decimal

from core.trigonometric_function.cosine import Cosine
from core.trigonometric_function.sine import Sine
from core.trigonometric_function.tangent import Tangent


def solve_function(exp):
    if exp.startswith("sin"):
        sin = Sine()
        args_str = exp[3:]
        if "," in args_str:
            arg_1 = args_str.split(",")[0]
            arg_2 = args_str.split(",")[1]
            return sin.result(Decimal(arg_1), int(arg_2))
        else:
            return sin.result(Decimal(args_str))

    if exp.startswith("cos"):
        cos = Cosine()
        args_str = exp[3:]
        if "," in args_str:
            arg_1 = args_str.split(",")[0]
            arg_2 = args_str.split(",")[1]
            return cos.result(Decimal(arg_1), int(arg_2))
        else:
            return cos.result(Decimal(args_str))

    if exp.startswith("tan"):
        tan = Tangent()
        args_str = exp[3:]
        if "," in args_str:
            arg_1 = args_str.split(",")[0]
            arg_2 = args_str.split(",")[1]
            return tan.result(Decimal(arg_1), int(arg_2))
        else:
            return tan.result(Decimal(args_str))