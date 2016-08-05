import random
import ipaddress

from pymockdata.base import BaseGenerator
from pymockdata.core.template import Template, Token
import pymockdata.data as datasets


def generate_valid_mac():
    return ":".join(["%x" % random.randint(1, 0xff) for _ in range(6)])


class MacAddressGenerator(BaseGenerator):
    ID = "mac_addr"

    _templates = [
        Template(
            Token.CUSTOM(generate_valid_mac)
        )
    ]


if __name__ == '__main__':
    print(MacAddressGenerator().generate())
