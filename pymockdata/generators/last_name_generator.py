import random
import string

from pymockdata.data.names import last_names
from pymockdata.consts import Fields
from pymockdata.base import BaseGenerator


class LastNameGenerator(BaseGenerator):
    templates = [
        (1, "{}"),
        (2, "{} {}"),
        (2, "{}-{}")
    ]

    ID = Fields.LAST_NAME

    def generate(self):
        return "{}".format(random.choice(last_names))

