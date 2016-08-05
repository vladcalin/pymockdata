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
    @abc.abstractproperty
    def _templates(self):
        pass

    @abc.abstractmethod
    def set_data(self, data):
        pass

    @abc.abstractmethod
    def export(self):
        pass

