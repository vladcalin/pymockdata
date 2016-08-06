import abc
import random


class BaseGenerator(abc.ABC):
    @abc.abstractproperty
    def _templates(self):
        pass

    @abc.abstractproperty
    def ID(self):
        pass

    def generate(self, seed=None):
        if seed:
            random.seed(seed)
            return random.choice(self._templates).render(seed=seed)
        return random.choice(self._templates).render()


class BaseExporter():
    """
    Will export a list of entries to various formats, depending on the implementation.

    A valid entry is
    {
        "key1": "value1",
        "key2": "value2",
        ...
    }
    """

    @abc.abstractmethod
    def add_entry(self, entry):
        pass

    @abc.abstractmethod
    def add_entries(self, entries):
        pass

    @abc.abstractmethod
    def export(self):
        pass
