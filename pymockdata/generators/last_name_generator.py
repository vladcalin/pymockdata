import pymockdata.data as datasets
from pymockdata.core.base import BaseGenerator
from pymockdata.core.template import Template, Token


class LastNameGenerator(BaseGenerator):
    ID = "last_name"
    _templates = [
        Template(
            Token.DatasetValue(datasets.LAST_NAME)
        )
    ]

