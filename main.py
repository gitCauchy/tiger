from command.help import do_help
from fundamental_tools.function_tools import calculate
from conf.config_read import read_config_info
from command.man import man
from core import *
import sys


def solve(exp):
    print("YOUR INPUT IS : ", exp)
    exp = exp.strip()
    if exp == "":
        return
    if exp.startswith("man"):
        # check man func exists
        if not exp[3:].strip() in read_config_info(section="man", key="man_func_list"):
            print("command not exists")
        else:
            man(exp[3:].strip())
    else:
        print(calculate(exp))


def terminated():
    print("Good bye!")
    sys.exit(0)


if __name__ == '__main__':
    do_help()
    while True:
        user_input = input()
        if user_input in ["q", "quit", "quit()"]:
            terminated()
        else:
            solve(user_input)
