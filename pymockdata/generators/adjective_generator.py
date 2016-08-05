import random

from pymockdata.base import BaseGenerator
from pymockdata.core.template import Template, Token
import pymockdata.data as datasets


class AdjectiveGenerator(BaseGenerator):
    ID = "adjective"
    _templates = [
        # Stafford
        Template(
            Token.VALUE(datasets.ADJECTIVES)
        )
    ]

if __name__ == '__main__':
    print(AdjectiveGenerator().generate())
