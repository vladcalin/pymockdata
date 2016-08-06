import random
import ipaddress

from pymockdata.base import BaseGenerator
from pymockdata.core.template import Template, Token
import pymockdata.data as datasets


def generate_valid_ipv6():
    return str(ipaddress.IPv6Address(random.randint(1, 2 ** ipaddress.IPV6LENGTH)))


class Ipv6AddressGenerator(BaseGenerator):
    ID = "ipv6_addr"

    _templates = [
        Template(
            Token.Custom(generate_valid_ipv6)
        )
    ]


if __name__ == '__main__':
    print(Ipv6AddressGenerator().generate())
