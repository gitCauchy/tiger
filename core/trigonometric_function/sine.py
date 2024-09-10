from check.check import Check
from command.manual import Manual
from core.result import Result
from fundamental_tools.taylor_polynomial import TaylorPolynomial


class Sine(Manual, Check, Result):

    def result(self, *args):
        x = args[0]
        if len(args) == 1:
            precision = 10
        else:
            precision = args[1]
        taylor = TaylorPolynomial()
        result = taylor.result(f0=0, x=x, precision=precision, derivative_0=self.derivative_0)
        return result

    def man(self):
        print("usage: sin(rad,pre) 'rad' is the unit of measurement for the angle in which you want to "
              "calculate the sine value in radians, 'pre' is precision ,'pre' should have a value between 1 and 100,"
              "default value 10")
        print("example : sin(1,10)")

    def check(self, *args):
        if len(args) == 0:
            print("input error , maybe you need use 'man sin to know how to use it.")
            return -1
        if len(args) == 2 and args[1] <= 0:
            print("the value of pre should have a value between 1 and 100 your input is illegal.")
            return -1

    def derivative_0(self, k):
        if k % 4 == 0 or k % 4 == 2:
            return 0
        if k % 4 == 1:
            return 1
        return -1
