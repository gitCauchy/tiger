from fundamental_tools.tigerstack import TigerStack
import re


def transfer(exp):
    num_stack = TigerStack()
    op_stack = TigerStack()
    func_stack = TigerStack()
    # remove redundant blank characters
    new_exp = re.sub(r"\s+", "", exp)


if __name__ == '__main__':
    exp = "H aaa          v   e"
    transfer(exp)
