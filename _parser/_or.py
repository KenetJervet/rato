from ._parser import Parser, Result


class Or(Parser):
    p1 = p2 = None

    def __init__(self, p1=None, p2=None):
        if p1:
            self.p1 = p1
        if p2:
            self.p2 = p2

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
