import pymockdata.data as datasets
from pymockdata.core.base import BaseGenerator
from pymockdata.core.template import Template, Token


class MaleNameGenerator(BaseGenerator):
    ID = "male_name"
    _templates = [
        # Konnor
        Template(
            Token.DatasetValue(datasets.MALE_NAME)
        ),
        # Zackery Nickolas
        Template(
            Token.DatasetValue(datasets.MALE_NAME),
            Token.SPACE,
            Token.DatasetValue(datasets.MALE_NAME)
        ),
        # Clay-Donavan
        Template(
            Token.DatasetValue(datasets.MALE_NAME),
            Token.Literal("-"),
            Token.DatasetValue(datasets.MALE_NAME)
        )
    ]

if __name__ == '__main__':
    print(MaleNameGenerator().generate())
