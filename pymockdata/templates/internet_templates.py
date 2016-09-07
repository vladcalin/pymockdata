import string
import random
import ipaddress

from pymockdata.core.base.template import Template


class Ipv4AddressTemplate(Template):
    pattern_list = []

    def render(self, *args, **kwargs):
        return str(ipaddress.IPv4Address(random.randint(1, 2 ** ipaddress.IPV4LENGTH)))

    def on_result(self, result_string):
        return result_string


class Ipv6AddressTemplate(Template):
    pattern_list = []

    def render(self, *args, **kwargs):
        return str(ipaddress.IPv6Address(random.randint(1, 2 ** ipaddress.IPV6LENGTH)))

    def on_result(self, result_string):
        return result_string


class MacAddressTemplate(Template):
    pattern_list = []

    def render(self, *args, **kwargs):
        def hex_char():
            return random.choice(string.hexdigits)

        sep = kwargs.get("sep", ":")
        return sep.join(["%s%s" % (hex_char(), hex_char()) for _ in range(6)]).upper()

    def on_result(self, result_string):
        return string


if __name__ == '__main__':
    print(MacAddressTemplate().render())
