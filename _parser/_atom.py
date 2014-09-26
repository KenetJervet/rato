from ._parser import Parser, Result


class Atom(Parser):
    def parse(self, s):
        return \
            Result.fail() if not s \
            else Result.succeed(
                s[0], s[1:]
            )
