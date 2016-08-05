import random

from pymockdata.base import BaseGenerator
from pymockdata.core.template import Template, Token
import pymockdata.data as datasets


class EmailGenerator(BaseGenerator):
    ID = "email"

    _templates = [
        Template(
            Token.Generator("professional_username"),
            Token.LITERAL("@"),
            Token.Generator("domain")
        ),
    ]


if __name__ == '__main__':
    print(EmailGenerator().generate())
