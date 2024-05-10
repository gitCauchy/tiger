from command.help import do_help
from core.trigonometric_function.sine import Sine

if __name__ == '__main__':
    sine = Sine()
    print(sine.result(2,100))
    # do_help()
    # user_input = input(">>>")
    # if user_input in ["q", "quit", "quit()"]:
    #     print("Good bye!")
    #     pass
    # while user_input not in ["q", "quit", "quit()"]:
    #     print("YOUR INPUT IS : ", user_input)
    #     user_input = input(">>>")
    # print("Good bye!")
