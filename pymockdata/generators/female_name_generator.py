import random

from pymockdata.base import BaseGenerator
from pymockdata.core.template import Template, Token
import pymockdata.data as datasets


class FemaleNameGenerator(BaseGenerator):
    ID = "female_name"
    _templates = [
        # Scarlett
        Template(
            Token.DatasetValue(datasets.FEMALE_NAME)
        ),
        # Karlie Bailee
        Template(
            Token.DatasetValue(datasets.FEMALE_NAME),
            Token.SPACE,
            Token.DatasetValue(datasets.FEMALE_NAME)
        ),
        # Kianna-Keyla
        Template(
            Token.DatasetValue(datasets.FEMALE_NAME),
            Token.Literal("-"),
            Token.DatasetValue(datasets.FEMALE_NAME)
        )
    ]

if __name__ == '__main__':
    print(FemaleNameGenerator().generate())
