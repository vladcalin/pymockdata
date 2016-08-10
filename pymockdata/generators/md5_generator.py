from pymockdata.core.base import BaseGenerator
from pymockdata.core.template import Token, Template


class Md5Generator(BaseGenerator):
    ID = "md5"

    _templates = [
        Template(
            Token.Repeat(Token.RandomSymbol("0123456789abcdef"), repeat=32)
        )
    ]


if __name__ == "__main__":
    print(Md5Generator().generate())
