import random
import string

from pymockdata.data.names import female_names
from pymockdata.base import BaseGenerator


class FemaleNameGenerator(BaseGenerator):
    templates = [
        (1, "{}"),
        (2, "{} {}"),
        (2, "{}-{}")
    ]

    def generate(self):
        items, templ = random.choice(self.templates)
        templ_args = [random.choice(female_names) for i in range(items)]
        return templ.format(*templ_args)


if __name__ == '__main__':
    gen = FemaleNameGenerator()
    for _ in range(10):
        print(gen.generate())
