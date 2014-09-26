from ._parser import Parser, Result


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
