import random

from pymockdata.base import BaseGenerator
from pymockdata.core.template import Template, Token
import pymockdata.data as datasets


class TldGenerator(BaseGenerator):
    ID = "tld"
    _templates = [
        Template(
            Token.DatasetValue(datasets.TLD)
        )
    ]

if __name__ == '__main__':
    print(TldGenerator().generate())
