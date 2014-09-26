from ._parser import Parser, Result


class Nil(Parser):
    def parse(self, s):
        return Result.succeed('', s)

