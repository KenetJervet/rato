import re
from ._predicate import Predicate


class RegexPredicate(Predicate):
    regex = None

    def __init__(self, regex=None):
        if regex:
            self.regex = regex
        self.regex = re.compile(self.regex)

    def __call__(self, s):
        # Returns only True or False
        return bool(self.regex.match(s))
