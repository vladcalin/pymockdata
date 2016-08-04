import os.path
from pymockdata.generators import _all_generators


def get_all_generators():
    return _all_generators


def get_generator_for_datatype(data_type):
    for generator in get_all_generators():
        if generator.ID == data_type:
            return generator
    raise ValueError("No generator found for {}".format(data_type))


def generate_data(data_type, instances=1):
    if instances == 1:
        return get_generator_for_datatype(data_type).generate()
    elif instances > 1:
        items = []
        generator = get_generator_for_datatype(data_type)
        for item in range(instances):
            items.append(generator.generate())
        return items
    raise ValueError("instances must be a positive integer")


if __name__ == '__main__':
    from pymockdata.consts import Fields
    print(generate_data(Fields.FEMALE_NAME, instances=10))