import random

from pymockdata.base import BaseGenerator
from pymockdata.core.template import Template, Token
import pymockdata.data as datasets


class LastNameGenerator(BaseGenerator):
    ID = "last_name"
    _templates = [
        Template(
            Token.VALUE(datasets.LAST_NAME)
        )
    ]

if __name__ == '__main__':
    print(LastNameGenerator().generate())
