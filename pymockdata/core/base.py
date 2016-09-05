from random import Random


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


class Dataset:

    def __init__(self, name, localisation, random=None):
        self.name = name
        self.localisation = localisation
        self.random = None

    def get_one(self):
        pass

    def get_many(self, many):
        pass