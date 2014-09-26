from ._sat import SAT
from ._regex_predicate import RegexPredicate
from ._atom import Atom


class Alpha(SAT):
    predicate = RegexPredicate('[A-Za-z]')
    parser = Atom()
