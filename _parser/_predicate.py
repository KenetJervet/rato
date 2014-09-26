from abc import ABCMeta, abstractmethod


class Predicate(metaclass=ABCMeta):
    @abstractmethod
    def __call__(self, s):
        raise NotImplementedError()
