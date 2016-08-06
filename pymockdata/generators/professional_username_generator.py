import random
import re

from pymockdata.base import BaseGenerator
from pymockdata.core.template import Template, Token
import pymockdata.data as datasets


class ProfessionalUsernameGenerator(BaseGenerator):
    ID = "professional_username"
    _templates = [
        Template(
            Token.Transform(Token.Generator("full_name"), lambda x: re.sub("[ -]", "_", x.lower()).replace(".", ""))
        ),
        Template(
            Token.Transform(Token.Generator("male_name"), lambda x: x[0].lower()),
            Token.Transform(Token.Generator("last_name"), lambda x: x.lower())
        ),
        Template(
            Token.Transform(Token.Generator("female_name"), lambda x: x[0].lower()),
            Token.Transform(Token.Generator("last_name"), lambda x: x.lower())
        ),
        Template(
            Token.Transform(Token.Generator("male_name"), lambda x: re.sub("[ -]", "_", x.lower()).replace(".", "")),
            Token.Transform(Token.Generator("last_name"), lambda x: x.lower())
        ),
        Template(
            Token.Transform(Token.Generator("female_name"), lambda x: re.sub("[ -]", "_", x.lower()).replace(".", "")),
            Token.Transform(Token.Generator("last_name"), lambda x: x.lower())
        )
    ]

if __name__ == '__main__':
    print(ProfessionalUsernameGenerator().generate())