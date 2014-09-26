from abc import ABCMeta, abstractmethod
import re


class Parser:
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


class Nil(Parser):
    def parse(self, s):
        return Result.succeed('', s)


class Atom(Parser):
    def parse(self, s):
        return \
            Result.fail() if not s \
            else Result.succeed(
                s[0], s[1:]
            )


class SAT(Parser):
    def parse(self, s):
        res = self.parser.parse(s)
        if res.succeeded and self.predicate(res.recognized):
            return Result.succeed(
                res.recognized, res.remaining
            )
        return Result.fail()


class Predicate(metaclass=ABCMeta):
    @abstractmethod
    def __call__(self, s):
        raise NotImplementedError()


class RegexPredicate(Predicate):
    def __init__(self, regex):
        self.regex = re.compile(regex)

    def __call__(self, s):
        # Returns only True or False
        return bool(self.regex.match(s))


class Num(SAT):
    predicate = RegexPredicate('\d')
    parser = Atom()


class Char(SAT):
    predicate = RegexPredicate('[A-Za-z]')
    parser = Atom()


class And(Parser):
    def __init__(self, p1, p2):
        self.p1, self.p2 = p1, p2

    def parse(self, s):
        res_left = self.p1.parse(s)
        if res_left.succeeded:
            res_right = self.p2.parse(res_left.remaining)
            if res_right:
                return Result.succeed(
                    res_left.recognized + res_right.recognized,
                    res_right.remaining
                )

        return Result.fail()


class Or(Parser):
    def __init__(self, p1, p2):
        self.p1, self.p2 = p1, p2

    def parse(self, s):
        res_left = self.p1.parse(s)
        if res_left.succeeded:
            return Result.succeed(
                res_left.recognized,
                res_left.remaining
            )
        res_right = self.p2.parse(s)
        if res_right.succeeded:
            return Result.succeed(
                res_right.recognized,
                res_right.remaining
            )
        return Result.fail()
