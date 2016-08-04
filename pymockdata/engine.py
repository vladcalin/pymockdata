import os.path
from pymockdata.generators import _all_generators


def get_all_generators():
    return _all_generators


def get_generator_for_datatype(data_type):
    for generator in get_all_generators():
        if generator.ID == data_type:
            return generator
    raise ValueError("No generator found for {}".format(data_type))


def generate_data(data_type, instances=1, seed=None):
    generator = get_generator_for_datatype(data_type)
    if seed:
        generator.set_seed(seed)
    if instances == 1:
        return generator.generate()
    elif instances > 1:
        items = []
        for item in range(instances):
            items.append(generator.generate())
        return items
    raise ValueError("instances must be a positive integer")
