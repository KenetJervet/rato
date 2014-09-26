from ._sat import SAT
from ._regex_predicate import RegexPredicate
from ._atom import Atom


class Underscore(SAT):
    predicate = RegexPredicate('_')
    parser = Atom()
