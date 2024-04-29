"""
queue
"""


class Queue(object):

    def __init__(self):
        self.queue = []

    def is_empty(self):
        return bool(self.queue)

    def enter_queue(self, data):
        self.queue.append(data)

    def delete(self):
        self.queue.remove()

    def clear(self):
        self.queue.clear()
