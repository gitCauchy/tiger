from abc import abstractmethod, ABCMeta


class Command(metaclass=ABCMeta):
    @abstractmethod
    def man(self): pass
