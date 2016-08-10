import pymockdata.data as datasets
from pymockdata.core.base import BaseGenerator
from pymockdata.core.template import Template, Token


class DomainGenerator(BaseGenerator):
    ID = "domain"

    __wordpick_token = Token.Choice(Token.DatasetValue(datasets.ADJECTIVES), Token.DatasetValue(datasets.NOUNS),
                                    Token.DatasetValue(datasets.ADVERBS))

    _templates = [
        Template(
            Token.Repeat(__wordpick_token, random_repeat=(1, 2)),
            Token.Generator("tld")
        ),
        Template(
            __wordpick_token,
            Token.Generator("tld")
        )
    ]


