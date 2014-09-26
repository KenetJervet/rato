from ._sat import SAT
from ._atom import Atom
from ._regex_predicate import RegexPredicate


class Digit(SAT):
    predicate = RegexPredicate('\d')
    parser = Atom()
