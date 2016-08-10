from pymockdata.core.base import BaseGenerator
from pymockdata.core.template import Template, Token


class EmailGenerator(BaseGenerator):
    ID = "email"

    _templates = [
        Template(
            Token.Generator("professional_username"),
            Token.Literal("@"),
            Token.Generator("domain")
        ),
    ]


