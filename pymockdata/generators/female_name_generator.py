import pymockdata.data as datasets
from pymockdata.core.base import BaseGenerator
from pymockdata.core.template import Template, Token


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

