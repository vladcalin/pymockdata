from random import Random
import abc

import pymockdata.datasets
from pymockdata.core.constants import Localisation


class Generator(metaclass=abc.ABCMeta):
    def __init__(self, *templates, random=None):
        self.templates = templates

        if not random:
            self.random = Random()
        else:
            self.random = random

    @abc.abstractmethod
    def generate(self):
        pass
