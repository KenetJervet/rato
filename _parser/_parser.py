from abc import ABCMeta, abstractmethod


class ParserMeta(ABCMeta):
    def __call__(cls, *args, **kwargs):
        is_singleton = getattr(cls, 'singleton', None)
        if is_singleton:
            if not hasattr(cls, '_singleton'):
                cls._singleton = cls.__new__(cls, *args, **kwargs)
                cls._singleton.__init__(*args, **kwargs)
            return cls._singleton

        else:
            instance = cls.__new__(cls, *args, **kwargs)
            instance.__init__(*args, **kwargs)
            return instance


class Parser(metaclass=ParserMeta):
    @abstractmethod
    def parse(self, s):
        raise NotImplementedError()


class Result:
    def __init__(self, recognized, remaining, succeeded):
        self._recognized = recognized
        self._remaining = remaining
        self._succeeded = succeeded

    @property
    def recognized(self):
        return self._recognized

    @property
    def remaining(self):
        return self._remaining

    @property
    def succeeded(self):
        return self._succeeded

    @classmethod
    def succeed(cls, recognized, remaining):
        return Result(recognized, remaining, True)

    @classmethod
    def fail(cls):
        return Result('', '', False)
