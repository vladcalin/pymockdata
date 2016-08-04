from .female_name_generator import FemaleNameGenerator
from .male_name_generator import MaleNameGenerator
from .last_name_generator import LastNameGenerator
from .full_female_name_generator import FullFemaleNameGenerator
from .full_male_name_generator import FullMaleNameGenerator

_all_generators = [
    # names
    FemaleNameGenerator(),
    MaleNameGenerator(),
    LastNameGenerator(),
    FullFemaleNameGenerator(),
    FullMaleNameGenerator()
]