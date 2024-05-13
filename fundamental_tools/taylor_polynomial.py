from fundamental_tools.function import fac


class TaylorPolynomial(object):

    def result(self, f0, x, precision, derivative_0):
        result = f0
        for i in range(1, precision + 1):
            result += (self.integer_power(x, i) * derivative_0(i)) / fac(i)
        return result

    def integer_power(self, x, pow):
        result = 1
        for i in range(pow):
            result = result * x
        return result
