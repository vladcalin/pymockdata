import random

from pymockdata.base import BaseGenerator
from pymockdata.core.template import Template, Token
import pymockdata.data as datasets


class FullMaleNameGenerator(BaseGenerator):
    ID = "full_male_name"
    _templates = [
        Template(
            Token.Generator("male_name"),
            Token.SPACE,
            Token.Generator("last_name")
        ),
        Template(
            Token.Generator("male_name"),
            Token.SPACE,
            Token.LETTER_UPPER,
            Token.DOT,
            Token.SPACE,
            Token.Generator("last_name")
        )
    ]

if __name__ == '__main__':
    print(FullMaleNameGenerator().generate())
