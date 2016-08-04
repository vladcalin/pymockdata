import random
import string

from pymockdata.data.names import male_names
from pymockdata.consts import Fields
from pymockdata.base import BaseGenerator


class MaleNameGenerator(BaseGenerator):
    templates = [
        (1, "{}"),
        (2, "{} {}"),
        (2, "{}-{}")
    ]

    ID = Fields.MALE_NAME

    def generate(self):
        items, templ = random.choice(self.templates)
        templ_args = [random.choice(male_names) for _ in range(items)]
        return templ.format(*templ_args)

