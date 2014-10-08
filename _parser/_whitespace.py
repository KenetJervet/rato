from ._sat import SAT
from ._regex_predicate import RegexPredicate
from ._atom import Atom


class WhiteSpace(SAT):
    predicate = RegexPredicate('\s')
    parser = Atom()
