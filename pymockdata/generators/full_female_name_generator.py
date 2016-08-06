from pymockdata.core.base import BaseGenerator
from pymockdata.core.template import Template, Token


class FullFemaleNameGenerator(BaseGenerator):
    ID = "full_female_name"
    _templates = [
        Template(
            Token.Generator("female_name"),
            Token.SPACE,
            Token.Generator("last_name")
        ),
        Template(
            Token.Generator("female_name"),
            Token.SPACE,
            Token.LETTER_UPPER,
            Token.DOT,
            Token.SPACE,
            Token.Generator("last_name")
        )
    ]

if __name__ == '__main__':
    print(FullFemaleNameGenerator().generate())
