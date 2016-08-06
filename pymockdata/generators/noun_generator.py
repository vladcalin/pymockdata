import pymockdata.data as datasets
from pymockdata.core.base import BaseGenerator
from pymockdata.core.template import Template, Token


class NounGenerator(BaseGenerator):
    ID = "noun"
    _templates = [
        Template(
            Token.DatasetValue(datasets.NOUNS)
        )
    ]

if __name__ == '__main__':
    print(NounGenerator().generate())
