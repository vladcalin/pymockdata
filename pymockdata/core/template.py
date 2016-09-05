class Template:
    def __init__(self, template_func, localisation=None):
        self.template_func = template_func
        self.localisation = localisation
        self.random = None

    def set_random(self, random):
        self.random = random

    def set_localisation(self, localisation):
        self.localisation = localisation

    def render(self, *args, **kwargs):
        to_return = self.template_func(*args, random=self.random, localisation=self.localisation, **kwargs)
        assert isinstance(to_return, str), \
            "function passed in template must return " \
            "a string, but returned '{}' instead".format(type(to_return))
        return to_return
