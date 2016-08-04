import random
import string

from pymockdata.data.names import male_names, last_names
from pymockdata.consts import Fields
from pymockdata.base import BaseGenerator


class FullMaleNameGenerator(BaseGenerator):
    TOKEN_LAST = 0
    TOKEN_LETTER = 1
    TOKEN_NAME = 2

    templates = [
        # ()
        ((TOKEN_LAST, TOKEN_NAME), "{} {}"),
        ((TOKEN_LAST, TOKEN_LETTER, TOKEN_NAME), "{} {}. {}"),
    ]

    ID = Fields.FULL_MALE_NAME

    def generate(self):
        tokens, templ = random.choice(self.templates)
        templ_args = []
        for token in tokens:
            if token == self.TOKEN_LAST:
                templ_args.append(random.choice(last_names))
            elif token == self.TOKEN_LETTER:
                templ_args.append(random.choice(string.ascii_uppercase))
            elif token == self.TOKEN_NAME:
                templ_args.append(random.choice(male_names))
        return templ.format(*templ_args)

