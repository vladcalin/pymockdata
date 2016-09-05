import string
import random
from pymockdata.datasets import DatasetAccess
from pymockdata.core.constants import Localisation


def generate_us_male_name():
    male_name = DatasetAccess("male_name", Localisation.en_US)
    last_name = DatasetAccess("last_name", Localisation.en_US)

    templates = [
        "{male_name} {last_name}",
        "{male_name} {last_name}",
        "{male_name} {last_name}",
        "{male_name} {last_name}",
        "{male_name} {last_name}",

        "{male_name}-{male_name2} {last_name}",
        "{male_name}-{male_name2} {letter}. {last_name}",
    ]

    templ = random.choice(templates)

    return templ.format(
        male_name=male_name.get_one(),
        male_name2=male_name.get_one(),
        last_name=last_name.get_one(),
        letter=random.choice(string.ascii_uppercase)
    )


if __name__ == '__main__':
    print(generate_us_male_name())
