from ._parser import Parser, Result


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
