import pymockdata.data as datasets
from pymockdata.core.base import BaseGenerator
from pymockdata.core.template import Template, Token


class TldGenerator(BaseGenerator):
    ID = "tld"
    _templates = [
        Template(
            Token.DatasetValue(datasets.TLD)
        )
    ]

if __name__ == '__main__':
    print(TldGenerator().generate())
