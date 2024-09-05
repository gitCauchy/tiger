from command.help import do_help
import sys


def solve(exp):
    print("YOUR INPUT IS : ", exp)


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
