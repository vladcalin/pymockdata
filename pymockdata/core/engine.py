import importlib
import inspect
import os

import pymockdata.generators
from pymockdata.core.base import BaseGenerator, BaseExporter

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


class MockDataGenerator:
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

        class GeneratorWrapper:
            def __init__(self, generator_instance, _seed):
                self._gen = generator_instance
                self._seed = _seed

            def __call__(self):
                return self._gen.generate(seed=self._seed)

        if gen:
            return GeneratorWrapper(gen[0](), self._seed)
        return super(MockDataGenerator, self).__getattribute__(item)


class DataModel:
    # constants
    male_name = "male_name"
    female_name = "female_name"
    last_name = "last_name"
    full_male_name = "full_male_name"
    full_female_name = "full_female_name"
    full_name = "full_name"

    noun = "noun"
    adjective = "adjective"

    forum_username = "forum_username"
    professional_username = "professional_username"
    tld = "tld"
    domain = "domain"
    email = "email"
    ipv4_addr = "ipv4_addr"
    ipv6_addr = "ipv6_addr"
    mac_addr = "mac_addr"

    def __init__(self, seed=None, **fields):
        self._fields = fields
        self._mock_data_generator = MockDataGenerator(seed=seed)

    def generate_one(self):
        entry = {}
        for key in self._fields.keys():
            entry[key] = self._resolve_field(self._fields[key])
        return entry

    def _resolve_field(self, field_value):
        return getattr(self._mock_data_generator, field_value)()

    def generate_batch(self, count):
        return [self.generate_one() for _ in range(count)]

    def value_for(self, field):
        return self._resolve_field(field)


class DataFactory:
    """
    A class that will automatically export generated data through the exporter.
    """

    def __init__(self, data_model, exporter):

        if not isinstance(data_model, DataModel):
            raise TypeError("data_model must be an instance of pymockdata.core.engine.DataModel")

        if not isinstance(exporter, BaseExporter):
            raise TypeError("exporter must be an instance of pymockdata.exporters.*")

        self.data_model = data_model
        self.exporter = exporter

    def generate(self, count):
        self.exporter.add_entries(data_model.generate_batch(count))
        self.exporter.export()


if __name__ == '__main__':
    data_model = DataModel(
        person_name=DataModel.full_name,
        email=DataModel.email,
        unofficial_username=DataModel.forum_username
    )

    from pymockdata.exporters.file import HtmlTableExporter

    exporter = HtmlTableExporter()
    DataFactory(data_model, exporter).generate(100)
