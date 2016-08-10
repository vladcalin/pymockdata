import abc
import random


class BaseGenerator(abc.ABC):
    @abc.abstractproperty
    def _templates(self):
        pass

    def on_finish(self, result_string):
        return result_string

    @abc.abstractproperty
    def ID(self):
        pass

    def generate(self, seed=None):
        template = random.choice(self._templates)
        if seed:
            random.seed(seed)
            to_return = template.render(seed=seed)
        else:
            to_return = template.render()

        return self.on_finish(to_return)

