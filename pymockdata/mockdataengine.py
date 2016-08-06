import importlib
import os
import inspect

import pymockdata.generators
from pymockdata.base import BaseGenerator

_ALL_GENERATORS = None


def _load_generators():
    global _ALL_GENERATORS
    if _ALL_GENERATORS:
        return _ALL_GENERATORS

    _generators_path = pymockdata.generators.__path__[0]
    generators = []
    for gen_file in os.listdir(_generators_path):
        if not gen_file.endswith("generator.py"):
            continue

        gen_module = importlib.import_module("pymockdata.generators." + gen_file.rstrip(".py"))
        for item_name in dir(gen_module):
            item = getattr(gen_module, item_name)
            if inspect.isclass(item) and not inspect.isabstract(item) and issubclass(item, BaseGenerator):
                generators.append(item)
    _ALL_GENERATORS = generators
    return generators


def _get_generator(generator_id):
    generator = [gen for gen in _load_generators() if gen.ID == generator_id]
    if generator:
        return generator[0]
    else:
        return None


class MockDataEngine:
    """
    Main class for generating mock data. Data is randomly generated when a specific member is accessed.
    The following members are used for generating mock data:

    Names:

    MockDataEngine.male_name
    MockDataEngine.female_name
    MockDataEngine.last_name
    MockDataEngine.full_male_name
    MockDataEngine.full_female_name
    MockDataEngine.full_name

    Various words:

    MockDataEngine.noun
    MockDataEngine.adjective

    Internet related:

    MockDataEngine.forum_username
    MockDataEngine.professional_username
    MockDataEngine.tld
    MockDataEngine.domain
    MockDataEngine.email
    MockDataEngine.ipv4_addr
    MockDataEngine.ipv6_addr
    MockDataEngine.mac_addr
    """
    def __init__(self, seed=None):
        self._seed = seed

    def __getattribute__(self, item):
        gen = [generator for generator in _load_generators() if generator.ID == item]
        if gen:
            return gen[0]().generate(seed=self._seed)
        return super(MockDataEngine, self).__getattribute__(item)


if __name__ == '__main__':
    print(MockDataEngine().email)