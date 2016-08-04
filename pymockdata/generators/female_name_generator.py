import random
import string

from pymockdata.data.names import female_names
from pymockdata.consts import Fields
from pymockdata.base import BaseGenerator


class FemaleNameGenerator(BaseGenerator):
    templates = [
        (1, "{}"),
        (2, "{} {}"),
        (2, "{}-{}")
    ]

    ID = Fields.FEMALE_NAME

    def generate(self):
        items, templ = random.choice(self.templates)
        templ_args = [random.choice(female_names) for _ in range(items)]
        return templ.format(*templ_args)

