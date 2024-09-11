from core.trigonometric_function.cosine import Cosine
from core.trigonometric_function.sine import Sine
from fundamental_tools.tigerstack import TigerStack
from decimal import Decimal
from conf.config_read import read_config_info


def is_function(exp):
    function_list = list(read_config_info("function", "function_list"))
    for fun in function_list:
        if exp.startswith(fun):
            return True


def solve_function(exp):
    if exp.startswith("sin"):
        sin = Sine()
        args_str = exp[3:]
        if "," in args_str:
            arg_1 = args_str.split(",")[0]
            arg_2 = args_str.split(",")[1]
            return sin.result(Decimal(arg_1), int(arg_2))
        else:
            return sin.result(Decimal(args_str))

    if exp.startswith("cos"):
        cos = Cosine()
        args_str = exp[3:]
        if "," in args_str:
            arg_1 = args_str.split(",")[0]
            arg_2 = args_str.split(",")[1]
            return cos.result(Decimal(arg_1), int(arg_2))
        else:
            return cos.result(Decimal(args_str))


def plus(d1, d2):
    return d1 + d2


def minus(d1, d2):
    return d1 - d2


def multiply(d1, d2):
    return d1 * d2


def divide(d1, d2):
    return d1 / d2


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
        # 1.if c is num append it to suffix_exp
        if c.isdigit():
            suffix_exp = suffix_exp + c
            continue

        # 2. if c is '(' push it into char_stack
        if c == "(":
            char_stack.push(c)

        # 3. if c is ')' pop element of stack until top of stack is '('
        # and then pop '('
        elif c == ")":
            while char_stack.get_top() != "(":
                suffix_exp += " "
                suffix_exp += char_stack.pop()
            # pop element '('
            char_stack.pop()

        elif is_operator(c):
            top_element = char_stack.get_top()
            if char_stack.is_empty() or top_element == "(" or operator_priority(c) > operator_priority(top_element):
                char_stack.push(c)
            else:
                while operator_priority(char_stack.get_top()) >= operator_priority(
                        c) and not char_stack.get_top() == "(" and not char_stack.is_empty():
                    suffix_exp += " "
                    suffix_exp += char_stack.pop()
                char_stack.push(c)
            suffix_exp += " "
        # defined function e.g. sin cos tan
        else:
            suffix_exp += c

    while not char_stack.is_empty():
        suffix_exp += " "
        suffix_exp += (char_stack.pop())
        suffix_exp += " "
    return suffix_exp


def rpn_calculate(rpn_exp):
    num_stack = TigerStack()
    ele_list = rpn_exp.split()
    for e in ele_list:
        if not is_operator(e):
            if is_function(e):
                num_stack.push(Decimal(solve_function(e)))
            else:
                num_stack.push(Decimal(e))
        else:
            digit_1 = num_stack.pop()
            digit_2 = num_stack.pop()
            if e == "+":
                num_stack.push(plus(digit_1, digit_2))
            elif e == "-":
                num_stack.push(minus(digit_2, digit_1))
            elif e == "*":
                num_stack.push(multiply(digit_1, digit_2))
            else:
                num_stack.push(divide(digit_2, digit_1))

    return num_stack.pop()


def calculate(ipt):
    suffix_exp = rpn_reverse(ipt)
    return rpn_calculate(suffix_exp)
