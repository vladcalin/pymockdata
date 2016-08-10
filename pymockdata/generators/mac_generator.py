import random

from pymockdata.core.base import BaseGenerator
from pymockdata.core.template import Template, Token


def generate_valid_mac():
    return ":".join(["%x" % random.randint(1, 0xff) for _ in range(6)])


class MacAddressGenerator(BaseGenerator):
    ID = "mac_addr"

    _templates = [
        Template(
            Token.Custom(generate_valid_mac)
        )
    ]


