from fundamental_tools.queue import Queue
from fundamental_tools.stack import Stack


def resolve(s):
    """
    resolve number character and function
    :param s: string
    :return: result
    """
    num_stack = Stack()
    op_char_stack = Stack()
    num_stage = Queue()
    char_stage = Queue()
    for item in user_input:
        """
        create a stage 
        """
        if item.isdigit():
            num_stage.enter_queue(data=item)
        else:
            # move stage elements to num_stack
            num = ""
            while num_stage:
                num += num_stage.delete()
            num_stack.push(num)


if __name__ == '__main__':
    user_input = input("")
    print("YOUR INPUT IS : ", user_input)
