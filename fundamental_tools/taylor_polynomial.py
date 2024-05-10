from fundamental_tools.function import fac


class TaylorPolynomial(object):

    def result(self, x, precision, derivative_0):
        result = 0
        for i in range(precision):
            result += (self.integer_power(x, i) * derivative_0(i)) / fac(i)
        return result

    def integer_power(self, x, pow):
        result = 1
        for i in range(pow):
            result = result * x
        return result
