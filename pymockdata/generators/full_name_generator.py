import random

from pymockdata.base import BaseGenerator
from pymockdata.core.template import Template, Token
import pymockdata.data as datasets


class FullNameGenerator(BaseGenerator):
    ID = "full_name"
    _templates = [
        Template(
            Token.Generator("full_female_name")
        ),
        Template(
            Token.Generator("full_male_name")
        )
    ]

if __name__ == '__main__':
    print(FullNameGenerator().generate())
