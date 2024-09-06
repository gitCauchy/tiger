from fundamental_tools.tigerstack import TigerStack


def is_operator(ch):
    if ch in ["+", "-", "*", "/"]:
        return True
    return False


def operator_priority(op):
    if op in ["+", "-"]:
        return 1
    return 2


def rpn_reverse(exp):
    suffix_exp = ""
    char_stack = TigerStack()
    for c in exp:
        if c == "(":
            char_stack.push(c)

        # if c is ')' pop element of stack until top of stack is '('
        # and then pop '('
        if c == ")":
            while char_stack.get_top() != "(":
                suffix_exp += char_stack.pop()
            char_stack.pop()

        # elif c.isdigit():
        #     suffix_exp = suffix_exp + c
        #     continue

        elif is_operator(c):
            top_element = char_stack.get_top()
            if char_stack.is_empty() or top_element == "(" or operator_priority(c) > operator_priority(top_element):
                char_stack.push(c)
            else:
                while operator_priority(char_stack.get_top()) < operator_priority(
                        c) and not char_stack.get_top() == "(":
                    suffix_exp += char_stack.pop()

            # if (operator_priority(c) < operator_priority(char_stack.get_top())) and not char_stack.is_empty():
            #     suffix_exp = suffix_exp + (char_stack.pop())
            # char_stack.push(c)
            # suffix_exp = suffix_exp + " "
    while not char_stack.is_empty():
        suffix_exp = suffix_exp + (char_stack.pop())
    return suffix_exp


class FunctionTools:
    function_list = ["sin", "cos"]

    def is_function(self, exp):
        if exp in self.function_list:
            return True
        return False


if __name__ == "__main__":
    exp = "150-(7+5)*2+30*2"
    result = rpn_reverse(exp)
    print(result)
