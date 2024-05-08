from abc import abstractmethod, ABCMeta


class Result(metaclass=ABCMeta):
    @abstractmethod
    def result(self, *args):
        pass
