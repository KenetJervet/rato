from ._parser import Parser, Result


class OneOrMany(Parser):
    def parse(self, s):
        res = self.parser.parse(s)
        if not res.succeeded:
            return Result.fail()
        res2 = self.parse2(s)
        return Result.succeed(
            res.recognized + res2.recognized,
            res2.remaining
        )

    def parse2(self, s):
        res = self.parser.parse(s)
        if res.succeeded:
            res2 = self.parse2(res.remaining)
            return Result.succeed(
                res.recognized + res2.recognized,
                res2.remaining
            )
        return Result.succeed(
            '',
            s
        )
        
