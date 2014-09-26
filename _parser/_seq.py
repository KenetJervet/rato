from ._parser import Parser, Result


class Seq(Parser):
    parser1 = parser2 = None

    def __init__(self, p1=None, p2=None):
        if p1:
            self.parser1 = p1
        if p2:
            self.parser2 = p2

    def parse(self, s):
        p1, p2 = self.parser1, self.parser2
        res = p1.parse(s)
        if res.succeeded:
            res2 = p2.parse(res.remaining)
            if res2.succeeded:
                return Result.succeed(
                    res.recognized + res2.recognized,
                    res2.remaining
                )
        return Result.fail()
