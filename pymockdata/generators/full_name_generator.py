from pymockdata.core.base import BaseGenerator
from pymockdata.core.template import Template, Token


class FullNameGenerator(BaseGenerator):
    ID = "full_name"
    _templates = [
        Template(
            Token.Generator("full_female_name")
        ),
        Template(
            Token.Generator("full_male_name")
        )
    ]

if __name__ == '__main__':
    print(FullNameGenerator().generate())
