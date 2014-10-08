from ._one_or_many import OneOrMany
from ._alpha import Alpha
from ._underscore import Underscore
from ._digit import Digit
from ._seq import Seq
from ._or import Or


class Word(Seq):
    parser1 = Or(Alpha(), Underscore())
    parser2 = OneOrMany(Or(Or(Alpha(), Underscore()), Digit()))
