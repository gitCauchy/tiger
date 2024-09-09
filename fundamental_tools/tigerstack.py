""" stack """


class TigerStack(object):
    def __init__(self):
        """Create a stack & init"""
        self.stack = []

    def pop(self):
        """ item pop from top"""
        if self.stack:
            return self.stack.pop(-1)
        else:
            raise IndexError("stack is null")

    def push(self, data):
        self.stack.append(data)

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

    def get_top(self):
        if self.is_empty():
            return None
        return self.stack[-1]

    def get_bottom(self):
        if self.is_empty():
            return None
        return self.stack[0]
