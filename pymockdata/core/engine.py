import importlib
import inspect
import os

import pymockdata.generators
from pymockdata.core.base import BaseGenerator

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


class _DataGenerator:
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
        return super(_DataGenerator, self).__getattribute__(item)


class DataModel:
    """
    Defines a model for the generated mock data. Used for generation of mock entries that consist in sets of key/value pairs

    Usage:
    >>> my_data_model = DataModel(field1=DataModel.male_name, field2=DataModel.last_name, ...)
    >>> my_data_model.generate_one()
    {"field1": "John", "field2": "Smith" ... }
    >>> my_data_model.generate_batch(2)
    [{"field1": "Mike", "field2": "Anderson" ... }, {"field1": "Zachery", "field2": "Wilson" ... }]

    Supported value types are:

    - DataModel.male_name
    - DataModel.female_name
    - DataModel.last_name
    - DataModel.full_male_name
    - DataModel.full_female_name
    - DataModel.full_name
    - DataModel.noun
    - DataModel.adjective
    - DataModel.forum_username
    - DataModel.professional_username
    - DataModel.tld
    - DataModel.domain
    - DataModel.email
    - DataModel.ipv4_addr
    - DataModel.ipv6_addr
    - DataModel.mac_addr

    """
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

    md5 = "md5"
    file_extension = "file_extension"

    def __init__(self, seed=None, **fields):
        """
        Defines the model for the generated entries
        :param seed: a numeric value used for the random generator. Defaults to the :function:`os.urandom`
        :param fields: the fields of the data model. Each field value must be one of the constants defined in this class
        """
        self._fields = fields
        self._mock_data_generator = _DataGenerator(seed=seed)
        self._extra_generators = []

    def generate_one(self):
        """
        Generates one mock entry.
        :return: a :class:`dict` instance containing the generated mock data.
        """
        entry = {}
        for key in self._fields.keys():
            entry[key] = self._resolve_field(self._fields[key])
        return entry

    def _resolve_field(self, field_value):
        for extra_generator in self._extra_generators:
            if extra_generator.ID == field_value:
                return extra_generator.generate()
        return getattr(self._mock_data_generator, field_value)()

    def generate_batch(self, count):
        """
        Generates a list of mock entries. This function calls :method:`generate_one()` multiple times in order to populate
        the list
        :param count: number of items to generate
        :return:
        """
        return [self.generate_one() for _ in range(count)]

    def value_for(self, field):
        """
        Generates a single mock value of type `field`.
        :param field: one of the constants defined in this class
        :return:
        """
        return self._resolve_field(field)

    def register_generator(self, generator):
        if not issubclass(generator, BaseGenerator):
            raise TypeError(
                "Expected parameter of type BaseGenerator but got {} instead".format(type(generator).__name__))
        if inspect.isclass(generator):
            generator = generator()
        self._extra_generators.append(generator)


if __name__ == '__main__':
    # data_model = DataModel(
    #     name=DataModel.full_name,
    #     email=DataModel.email,
    #     ip=DataModel.ipv4_addr,
    #     mac=DataModel.mac_addr,
    # )
    #
    # # print(data_model.generate_batch(10))
    #
    # print(data_model.value_for(DataModel.md5))
    # print(data_model.value_for(DataModel.md5))
    # print(data_model.value_for(DataModel.md5))

    from pymockdata.core.template import Template, Token

    data_model = DataModel()

    class MyGenerator(BaseGenerator):

        ID = "my_first_generator"
        _templates = [
            Template(Token.Repeat(Token.SYMBOL, repeat=25))
        ]

    data_model.register_generator(MyGenerator)

    print(data_model.value_for("my_first_generator"))
