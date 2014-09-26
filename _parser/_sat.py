from ._parser import Parser, Result


class SAT(Parser):
    predicate = parser = None

    def __init__(self, predicate=None, parser=None):
        if predicate:
            self.predicate = predicate
        if parser:
            self.parser = parser

    def parse(self, s):
        res = self.parser.parse(s)
        if res.succeeded and self.predicate(res.recognized):
            return Result.succeed(
                res.recognized, res.remaining
            )
        return Result.fail()
