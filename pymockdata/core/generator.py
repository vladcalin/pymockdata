from random import Random

import pymockdata.datasets
from pymockdata.core.constants import Localisation
from pymockdata.templates.names_templates import FullFemaleNameTemplate, FullMaleNameTemplate, FemaleNameTemplate, \
    MaleNameTemplate, FullNameTemplate


class Generator:
    _templates = {
        "male_name": MaleNameTemplate,
        "female_name": FemaleNameTemplate,
        "full_male_name": FullMaleNameTemplate,
        "full_female_name": FullFemaleNameTemplate,
        "full_name": FullNameTemplate,
        "name": FullNameTemplate
    }

    def __init__(self, random=None, localisation=Localisation.default):
        if not random:
            self._random = Random()
        else:
            self._random = random
        self._localisation = localisation

    def __getattribute__(self, item):
        if item.startswith("_"):
            return super(Generator, self).__getattribute__(item)
        if item in self._templates:
            localisation = self._localisation
            random = self._random

            class TemplateWrapper:
                def __init__(self, template_class):
                    self.template = template_class(localisation=localisation, random=random)

                def __call__(self, *args, **kwargs):
                    return self.template.render(*args, **kwargs)

            return TemplateWrapper(self._templates[item])


if __name__ == '__main__':
    print(Generator(localisation=Localisation.ro_RO).name())
