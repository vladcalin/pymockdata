import random

from pymockdata.base import BaseGenerator
from pymockdata.core.template import Template, Token
import pymockdata.data as datasets


class MaleNameGenerator(BaseGenerator):
    ID = "male_name"
    _templates = [
        # Konnor
        Template(
            Token.VALUE(datasets.MALE_NAME)
        ),
        # Zackery Nickolas
        Template(
            Token.VALUE(datasets.MALE_NAME),
            Token.SPACE,
            Token.VALUE(datasets.MALE_NAME)
        ),
        # Clay-Donavan
        Template(
            Token.VALUE(datasets.MALE_NAME),
            Token.LITERAL("-"),
            Token.VALUE(datasets.MALE_NAME)
        )
    ]

if __name__ == '__main__':
    print(MaleNameGenerator().generate())
