from decimal import Decimal

from core.check import Check
from core.manual import Manual
from core.result import Result
from core.trigonometric_function.cosine import Cosine
from core.trigonometric_function.sine import Sine


class Tangent(Manual, Result, Check):
    def result(self, *args):
        x = args[0]
        if len(args) == 1:
            precision = 10
        else:
            precision = args[1]
        sin = Sine()
        cos = Cosine()
        sin_r = Decimal(sin.result(x, precision))
        cos_r = Decimal(cos.result(x, precision))
        return sin_r / cos_r

    def man(self):
        print("usage: tan(rad,pre) 'rad' is the unit of measurement for the angle in which you want to "
              "calculate the tangent value in radians, 'pre' is precision ,'pre' should have a value between "
              "1 and 100,default value 10")
        print("example : sin(1,10)")

    def check(self, *args):
        if len(args) == 0:
            print("input error , maybe you need use 'man tan to know how to use it.")
            return -1
        if len(args) == 2 and args[1] <= 0:
            print("the value of pre should have a value between 1 and 100 your input is illegal.")
            return -1
