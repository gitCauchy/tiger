from core.check import Check
from core.manual import Manual
from core.result import Result
from core.trigonometric_function.sine import Sine


class Secant(Manual, Result, Check):
    def man(self):
        print("usage: sec(rad,pre) 'rad' is the unit of measurement for the angle in which you want to "
              "calculate the sine value in radians, 'pre' is precision ,'pre' should have a value between 1 and 100,"
              "default value 10")
        print("example : sin(1,10)")

    def result(self, *args):
        x = args[0]
        if len(args) == 1:
            precision = 10
        else:
            precision = args[1]
        sin = Sine()
        return 1 / sin.result(x, precision)

    def check(self, *args):
        if len(args) == 0:
            print("input error , maybe you need use 'man sin to know how to use it.")
            return -1
        if len(args) == 2 and args[1] <= 0:
            print("the value of pre should have a value between 1 and 100 your input is illegal.")
            return -1
