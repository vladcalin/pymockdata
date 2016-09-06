from random import Random
import importlib
import os
from collections import namedtuple

from pymockdata.core.constants import Localisation


class DatasetAccess:
    def __init__(self, name, localisation, random=None):
        self.name = name
        self.localisation = localisation
        if random:
            self.random = random
        else:
            self.random = Random()

        self.dataset_instance = self._get_dataset_instance()

    def _get_dataset_instance(self):
        ds_modules = [f for f in os.listdir(os.path.dirname(__file__)) if
                      f.endswith(".py") and not f.startswith("__")]
        ds_modules = [x.replace(".py", "") for x in ds_modules]

        for module_to_imp in ds_modules:
            module = importlib.import_module("pymockdata.datasets." + module_to_imp)

            for dataset_name in dir(module):
                dataset = getattr(module, dataset_name)
                if isinstance(dataset,
                              tuple) and dataset.name == self.name and (dataset.localisation == self.localisation or dataset.localisation is None):
                    return dataset

        raise ValueError(
            "No suitable dataset found for name='{}' and localisation='{}'".format(self.name, self.localisation))

    def get_one(self):
        return self.random.choice(self.dataset_instance.items)

    def get_many(self, count):
        return [self.get_one() for _ in range(count)]


Dataset = namedtuple("Dataset", ["name", "localisation", "items"])

if __name__ == '__main__':
    dataset = DatasetAccess("female_name", Localisation.en_US)
    print(dataset.get_many(5))
