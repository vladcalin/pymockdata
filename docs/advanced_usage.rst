Advanced usage
==============

This library provides support for defining your own template and generate random data using it. In the following sections
we will describe how to extend the generating capabilities of the framework at runtime and how to create a new generator from
scratch.

This framework is composed of a collection of generators, which are a collection of templates, which are a collection of
tokens. So when you are generating a value, what happens under the hood is:

- the :py:class:`DataModel` instance chooses the right generator for that value type.
- the chosen generator randomly chooses a template.
- the chosen template is rendered, meaning that each token from the template is rendered individually.
- the results of the tokens are joined together and the final result is produced.


Defining your own Template
--------------------------

The template you are going to define is an instance of :py:class:`Template`. Basically, a template is a collection of
:py:class:`Token`.

Firstly, you have to define the template as follows::

    template = Template(
        token1,
        token2,
        token3,
        ...
    )

where ``token1``, ``token2``, ``token3`` are valid tokens (see :py:class:`Token` for possible token values)

To test your template, simply run ``template.render()`` and it will return a generated value.

Examples::

    template = Template(
        Token.Literal("hello"),
        Token.SPACE,
        Token.Literal("world")
    )
    template.render()
    # "hello world"

    template = Template(
        Token.Generator("domain"),
        Token.SPACE,
        Token.Literal("has "),
        Token.NumberInverval(0, 2000),
        Token.Literal(" visits every day")
    )
    template.render()
    # recondite.io has 654 visits every day

.. note::

    The tokens are parsed in the order they are declared in the template. This aspect is crucial because of
    :py:func:`Token.SetInternalVariable` and :py:func:`Token.GetInernalVariable`.


Building your own Generator
---------------------------

A generator is a sublcass of :py:class:`BaseGenerator` and must have the following attributes and
methods defined:

- ``ID = "some_identifier"`` which identifies the generator. The generator will be referenced by this identifier
- ``_templates = [Template(...), Template(...)]`` which is a list of templates. When generating a new value, a random template from this list will be chosen and rendered.
- ``on_finish(self, result_string)`` which is an optional function that takes one string parameter which is called after the rendering is done.


After these fields are populated, all you have to do is call :py:func:`generate()` on your generator instance.

A basic example of a generator which generates a random MD5 hash in hexadecimal format is::

    class Md5Generator(BaseGenerator):
        ID = "md5"

        _templates = [
            Template(
                Token.Repeat(Token.RandomSymbol("0123456789abcdef"), repeat=32)
            )
        ]

    Md5Generator().generate()
    # a955faeca4984ea52df4ac472f6cdf96

A more advanced example of generator which overwrites the ``on_finish`` method would be ::

    class SomeWeirdNameGenerator(BaseGenerator):
        ID = "weird_name"
        _templats = [
            Tempate(
                Token.Generator("full_name")
            )
        ]
        def on_finish(self, result_string):
            chars = {"a": "4", "e": "3", "t": "7", "i": "1", "o": "0"}
            for char in chars:
                result_string = result_string.replace(char, chars[char])
            return result_string.upper()

    SomeWeirdNameGenerator().generate()
    # RUDY K4YD3N X. R0M4N

Complete example
----------------
::

    from pymockdata.core.template import Template, Token

    # defining an empty data model
    data_model = DataModel()

    # defining the generator
    class MyGenerator(BaseGenerator):

        ID = "my_first_generator"
        _templates = [
            Template(Token.Repeat(Token.SYMBOL, repeat=25))
        ]

    # registering it
    data_model.register_generator(MyGenerator)
    # or data_model.register_generator(MyGenerator())

    # calling it
    print(data_model.value_for("my_first_generator"))
    # .}-);~_>}#\?{++(:~+=["!.<

.. important::

    If you come up with any interesting generator idea, feel free to submit a pull request :)