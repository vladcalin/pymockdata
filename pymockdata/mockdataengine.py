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

        gen_module = importlib.import_module("pymockdata.generators." + gen_file.strip(".py"))
        for item_name in dir(gen_module):
            item = getattr(gen_module, item_name)
            if inspect.isclass(item) and not inspect.isabstract(item) and issubclass(item, BaseGenerator):
                generators.append(item)
    _ALL_GENERATORS = generators
    return generators


class MockDataEngine:
    def __getattribute__(self, item):
        gen = [generator for generator in _load_generators() if generator.ID == item]
        if gen:
            return gen[0]().generate()
        raise AttributeError("Object {} has no attribute {}".format(self.__class__, item))


if __name__ == '__main__':
    print(MockDataEngine().male_name)
