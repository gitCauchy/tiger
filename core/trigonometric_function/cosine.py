from check.check import Check
from command.command import Command
from core.result import Result


class Cosine(Command, Check, Result):
    def result(self, *args):
        pass

    def man(self):
        pass

    def check(self, *args):
        pass
