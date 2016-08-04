import abc
import random


class BaseGenerator(abc.ABC):
    @abc.abstractmethod
    def generate(self):
        pass


class BaseExporter(abc.ABC):
    @abc.abstractmethod
    def set_data(self, data):
        pass

    @abc.abstractmethod
    def export(self):
        pass
