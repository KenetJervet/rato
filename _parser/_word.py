from ._parser import Parser, Result
from ._one_or_many import OneOrMany
from ._alpha import Alpha
from ._underscore import Underscore
from ._digit import Digit
from ._seq import Seq
from ._or import Or
from ._and import And


class Word(OneOrMany):
    parser = Seq(
