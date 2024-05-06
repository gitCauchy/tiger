def power(base_number, pow):
    pass


def log(base_number, antilogarithm):
    pass


def lg(antilogarithm):
    pass


def ln(antilogarithm):
    pass


def check_fac_param(x):
    if not type(x) == int:
        print("error! 'x' should be an integer.")
    if x < 0:
        print("error! 'x' should be greater than zero.")


def fac(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x * fac(x - 1)


if __name__ == '__main__':
    print(power(3, 3))
