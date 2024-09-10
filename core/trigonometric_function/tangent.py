from check.check import Check
from command.manual import Manual
from core.result import Result


class Tangent(Manual, Result, Check):
    def man(self):
        pass

    def result(self, *args):
        pass

    def check(self, *args):
        pass
