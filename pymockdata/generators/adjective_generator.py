import pymockdata.data as datasets
from pymockdata.core.base import BaseGenerator
from pymockdata.core.template import Template, Token


class AdjectiveGenerator(BaseGenerator):
    ID = "adjective"
    _templates = [
        # Stafford
        Template(
            Token.DatasetValue(datasets.ADJECTIVES)
        )
    ]

if __name__ == '__main__':
    print(AdjectiveGenerator().generate())
