import ipaddress
import random

from pymockdata.core.base import BaseGenerator
from pymockdata.core.template import Template, Token


def generate_valid_ipv4():
    return str(ipaddress.IPv4Address(random.randint(1, 2 ** ipaddress.IPV4LENGTH)))


class Ipv4AddressGenerator(BaseGenerator):
    ID = "ipv4_addr"

    _templates = [
        Template(
            Token.Custom(generate_valid_ipv4)
        )
    ]


if __name__ == '__main__':
    print(Ipv4AddressGenerator().generate())
