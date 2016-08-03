import random
import string

from pymockdata.data.names import Names


class NameGenerator:
    person_name_patterns = {
        0: "{} {}. {}",
    }

    @classmethod
    def get_female_name(cls):
        return random.choice(Names.female_names)

    @classmethod
    def get_male_name(cls):
        return random.choice(Names.male_names)

    @classmethod
    def get_last_name(cls):
        return random.choice(Names.last_names)

    @classmethod
    def get_person_name(cls):
        return cls.person_name_patterns[0].format(cls.get_last_name(), random.choice(string.ascii_uppercase),
                                                  random.choice([cls.get_female_name, cls.get_male_name])())


if __name__ == '__main__':
    for _ in range(10):
        print(NameGenerator.get_person_name())
