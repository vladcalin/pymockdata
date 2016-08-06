import random

from pymockdata.base import BaseGenerator
from pymockdata.core.template import Template, Token
import pymockdata.data as datasets


class ForumUsernameGenerator(BaseGenerator):
    ID = "forum_username"
    _templates = [
        Template(
            Token.DatasetValue(datasets.ADJECTIVES),
            Token.RandomSymbol("_-."),
            Token.DatasetValue(datasets.NOUNS),
            Token.Repeat(Token.DIGIT, random_repeat=(0, 6))
        ),
    ]

if __name__ == '__main__':
    print(ForumUsernameGenerator().generate())
