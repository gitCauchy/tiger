from check.check import Check
from command.manual import Manual
from core.result import Result
from fundamental_tools.taylor_polynomial import TaylorPolynomial


class Cosine(Manual, Check, Result):

    def result(self, *args):
        x = args[0]
        if len(args) == 2:
            precision = args[1]
        else:
            precision = 10
        taylor = TaylorPolynomial()
        result = taylor.result(f0=1, x=x, precision=precision, derivative_0=self.derivative_0)
        return result

    def man(self):
        print("usage: cos(rad,pre) 'rad' is the unit of measurement for the angle in which you want to "
              "calculate the cosine value in radians, 'pre' is precision ,'pre' should have a value between 1 and 100,"
              "default value 10")
        print("example : cos(1,10)")

    def check(self, *args):
        if len(args) == 0:
            print("input error , maybe you need use 'man cos to know how to use it.")
            return -1
        if len(args) == 2 and args[1] <= 0:
            print("the value of pre should have a value between 1 and 100 your input is illegal.")
            return -1

    def derivative_0(self, i):
        r = i % 4
        if r == 1 or r == 3:
            return 0
        elif r == 2:
            return -1
        else:
            return 1
