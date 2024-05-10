from check.check import Check
from command.command import Command
from core.result import Result
from fundamental_tools.function import fac


class Sine(Command, Check, Result):
    def result(self, *args):
        sum = 0
        x = args[0]
        if len(args) == 1:
            precision = 10
        else:
            precision = args[1]
        for i in range(precision):
            sum += (self.power_x(x, i) * self.derivative_0(i)) / fac(i)
        return sum

    def man(self):
        print("1. usage: sin(rad,pre) 'rad' is the unit of measurement for the angle in which you want to "
              "calculate the sine value in radians, 'pre' is precision ,'pre' should have a value between 1 and 100,"
              "default value 10")
        print("example : sin(1,10)")

    def check(self, *args):
        pass

    def derivative_0(self, k):
        if k % 4 == 0 or k % 4 == 2:
            return 0
        if k % 4 == 1:
            return 1
        return -1

    def power_x(self, x, pow):
        result = 1
        for i in range(pow):
            result = result * x
        return result
