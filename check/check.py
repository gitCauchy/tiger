from abc import abstractmethod, ABCMeta


class Check(metaclass=ABCMeta):
    @abstractmethod
    def check(self, *args):
        pass
