from core.check import Check
from core.manual import Manual
from core.result import Result
from core.trigonometric_function.cosine import Cosine


class Cosecant(Manual, Check, Result):
    def man(self):
        print("usage: sec(rad,pre) 'rad' is the unit of measurement for the angle in which you want to "
              "calculate the cosecant value in radians, 'pre' is precision ,'pre' should have a value "
              "between 1 and 100, default value is 10")
        print("example : sec(1,10)")

    def check(self, *args):
        if len(args) == 0:
            print("input error , maybe you need use 'man tan to know how to use it.")
            return -1
        if len(args) == 2 and args[1] <= 0:
            print("the value of pre should have a value between 1 and 100 your input is illegal.")
            return -1

    def result(self, *args):
        x = args[0]
        if len(args) == 2:
            precision = args[1]
        else:
            precision = 10
        cos = Cosine()
        cos.result(x, precision)
        return 1 / cos.result(x, precision)
