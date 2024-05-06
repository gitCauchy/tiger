""" stack """


class Stack(object):
    def __init__(self):
        """Create a stack & init"""
        self.stack = []

    def pop(self):
        """ item pop from top"""
        if self.stack:
            return self.stack.pop(0)
        else:
            raise IndexError("stack is null")

    def push(self, data):
        self.stack.append(data)

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)
