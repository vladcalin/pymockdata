from string import Formatter
import abc
from random import Random

from pymockdata.core.constants import Localisation
from pymockdata.datasets import DatasetAccess


class Template(metaclass=abc.ABCMeta):
    """
        Will expose a list of pattern lists.

        A pattern is a string like

            "{token_name} some static strings {token_name2}"
    """

    def __init__(self, localisation=Localisation.default, random=None):
        self._formats = [(x, list(Formatter().parse(x))) for x in self.pattern_list]
        self.localisation = localisation

        self.random = random or Random()

    def _choose_template(self):
        return self.random.choice(self._formats)

    def _parse_template(self, tokens):
        result = ""
        for x in tokens:
            literal, field_name, _, _ = x
            result += literal
            result += self._resolve_dataset(field_name)
        return result

    def _resolve_dataset(self, field_name):
        return DatasetAccess(field_name, self.localisation, self.random).get_one()

    def render(self, *args, **kwargs):
        if args or kwargs:
            raise ValueError("The default Template.render() method does not take any arguments")
        template, tokens = self._choose_template()
        result = self._parse_template(tokens)
        return self.on_result(result)

    @abc.abstractproperty
    def pattern_list(self):
        pass

    @abc.abstractmethod
    def on_result(self, result_string):
        pass
