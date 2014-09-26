import re
from ._predicate import Predicate


class RegexPredicate(Predicate):
    def __init__(self, regex):
        self.regex = re.compile(regex)

    def __call__(self, s):
        # Returns only True or False
        return bool(self.regex.match(s))
