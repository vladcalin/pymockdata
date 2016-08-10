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

