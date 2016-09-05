import os
from random import Random
import importlib
from collections import namedtuple

import pymockdata.datasets
from pymockdata.core.constants import Localisation


class Generator:
    def __init__(self, name, template, localisation, *args, **kwargs):
        self.name = name
        self.localisation = localisation
        self.args = args
        self.kwargs = kwargs
        self.template = template

        self.random = Random()

        self.template.set_random(self.random)
        self.template.set_localisation(localisation)

    def set_seed(self, seed):
        self.random = Random(seed)
        self.template.set_random(self.random)

    def generate_one(self):
        return self.template.render(*self.args, **self.kwargs)

