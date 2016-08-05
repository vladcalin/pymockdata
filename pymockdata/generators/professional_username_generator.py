import random

from pymockdata.base import BaseGenerator
from pymockdata.core.template import Template, Token
import pymockdata.data as datasets


class ForumUsernameGenerator(BaseGenerator):
    ID = "forum_username"
    _templates = [
        # Stafford
        Template(
            Token.VALUE(datasets.NOUNS),
            Token.Repeat(Token.DIGIT, random_repeat=(0, 6))
        ),
        Template(
            Token.VALUE(datasets.ADJECTIVES),
            Token.VALUE(datasets.NOUNS),
            Token.Repeat(Token.DIGIT, random_repeat=(0, 6))
        ),
        Template(
            Token.VALUE(datasets.ADJECTIVES),
            Token.RANDOM_SYMBOL("-_."),
            Token.VALUE(datasets.NOUNS),
            Token.Repeat(Token.DIGIT, random_repeat=(0, 6))
        )
    ]

if __name__ == '__main__':
    print(ForumUsernameGenerator().generate())
