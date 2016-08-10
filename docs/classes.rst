Classes
=======


.. py:class:: DataModel(**fields)
              DataModel(seed, **fields)

    The ``fields`` must be pairs of key-type that will specify how the generated entries will look like.

    If specified, the ``seed`` parameter will be used as the seed of the random generator leading to generated controlled
    results. Two different generations with the same seed will lead to the same results. The value must be :py:class:`int`.

    .. py:method:: generate_one(self)

        Generates one mock entry as a :py:class:`dict`. The keys this entry will have will match the ``fields`` keys.

        If the data model is defined as ``DataModel(field1=..., fiedl2=..., field3=...)``, then this method will return a
        :py:class:`dict` instance like this::

            {
                "field1": ...,
                "field2": ...,
                "field3": ...
            }

    .. py:method:: generate_batch(self, count)

        Generates a list of *count* entries (see :py:func:`generate_one` for more information about the structure of the entries)

    .. py:method:: value_for(self, field)

        Generates one mock value for the specified field.

        :param field: must be one of the constants defined in this class.

    .. py:method:: register_generator(self, generator)

        Registers a generator that can be used afterwards to generate mock values. See :doc:`advanced_usage`
        for more information about this topic.

        After regstering, the generator can be used to generate data by calling::

            data_model.value_for(identifier)

        .. note::

                This method adds the generator only in the :py:class:`DataModel` instance that calls this method. If you need
                to generate entries with the custom generator, you have to define the data model first with the custom field and
                after that to register the generator::

                        data_model = DataModel(my_field="my_generator_id")
                        data_model.register_generator(my_generator)

                        # now it is safe to generate stuff





    .. _defined_field_types:

    .. py:attribute:: female_name

        Generates a female name.

        Example: *Larissa Karli*, *Makena*, *Lailah-Makayla*

    .. py:attribute:: male_name

        Generates a male name.

        Example: *Franklin-Damon*, *Trevor*, *Dylan*

    .. py:attribute:: last_name

        Generates a last name.

        Example: *Howell*, *Mccall*, *Shelton*

    .. py:attribute:: full_female_name

        Generates a full female name (first name, optional middle name, last name).

        Example: *Camryn-Karley G. Chandler*, *Tabitha Porter*, *Araceli X. Vargas*

    .. py:attribute:: full_male_name

        Generates a full male name (first name, optional middle name, last name).

        Example: *Rowan Lincoln Case*, *Zachery-Jaylin Goodman*, *Darnell-Kole C. Adams*

    .. py:attribute:: full_name

        Generates a full male or female name.

    .. py:attribute:: email

        Generates an email address.

        Examples: *mmoran@fuel.biz*, *mblake@swim.es*, *ellishardy@flimsy.jp*, *alexandra_shaniatodd@waterjoyously.net*

    .. py:attribute:: domain

        Generates a domain.

        Examples: *jovially.biz*, *victoriously.io*, *fair.org*, *beginner.de*

    .. py:attribute:: tld

        Generates a top-level domain.

        Examples: *.com*, *.net*, *.io*, *.biz*

    .. py:attribute:: forum_username

        Generates a forum username.

        Examples: *mindless-level96*, *accessible.care41*, *strange.thing02*

    .. py:attribute:: professional_username

        Generates a professional-looking username.

        Examples: *krasmussen*, *destiny_amy_hensley*, *mariam_averieorozco*, *thooper*

    .. py:attribute:: ipv4_addr

        Generates an IPv4 address (public or private).

        Examples: *166.254.145.53*, *160.102.119.86*, *149.56.27.84*, *229.177.224.146*

    .. py:attribute:: ipv6_addr

        Generates an IPv6 address

        Examples: *8384:bf40:459f:8a3e:e46d:4561:a912:3995*, *c47c:abf0:6311:f1a9:8ee9:62d4:5c25:b800*, *2576:1ae4:cba6:5d74:6be8:4f5b:9a85:306f*

    .. py:attribute:: mac_addr

        Generates a MAC address.

        Examples: *81:29:66:aa:10:25*, *65:1d:73:80:3f:42*, *84:cc:a2:b0:ee:cb*

    .. py:attribute:: md5

        Generates an hex representation of an MD5 hash.

        Examples: *68b35de195413767c1700ac383265f4e*, *7bcb4e8b774aeefe67d0e1f6a8845bf4*, *f005d9fb0871507700382ab4c0a45477*

    .. py:attribute:: file_extension

        Generates a file extension

        Examples: *.png*, *.xml*, *.cpp*


.. py:class:: Token

    Represents a token instance in the template that will be resolved to a string.

    .. py:attribute:: DIGIT

        Renders to a decimal digit.

    .. py:attribute:: LETTER_LOWER

        Renders to a lowercase ascii letter.

    .. py:attribute:: LETTER_UPPER

        Renders to an uppercase ascii letter.

    .. py:attribute:: LETTER

        Renders to an ascii letter.

    .. py:attribute:: DOT

        Renders to ``"."``.

    .. py:attribute:: SYMBOL

        Renders to a random character from ``"!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~"``.

    .. py:attribute:: SPACE

        Renders to ``" "``.

    .. py:method:: DatasetValue(field_name)

        Renders to a random value from the ``field_name`` dataset. If no suitable dataset is found, will raise an exception.

    .. py:method:: NumberInterval(min, max)

        Renders to a random decimal representation of a number in the interval ``[min, max]``

    .. py:method:: Literal(str_literal)

        Renders to ``str_literal``.

    .. py:method:: RandomSymbol(symbol_set)

        Renders to a random character from *symbol_set*.

    .. py:method:: Custom(func, args=None, kwargs=None)

        Calls *func* with arguments ``*args`` and ``**kwargs`` and renders to its response. *func* must be a callable that
        returns a string.

    .. py:method:: Repeat(token, repeat=1, random_repeat=None)

        Causes *token* to be rendered multiple times, specifically *repeat* times if random_repeat is not specified. If
        *random_repeat* is specified, it must be an :py:class:`tuple(int, int)`

    .. py:method:: Generator(generator_id)

        Calls another generator and render to its generated value.

    .. py:method:: Transform(token, template)

        Renders the *token* token and applies *template* on the result.

    .. py:method:: Choice(*tokens, count=None, count_range=None)

        Randomly choose a number of tokens from *tokens* to render (also their order is random).

        :param tokens: The set of tokens from where to choose.
        :param count: The number of tokens to be chosen from *tokens*. Can be greater than ``len(tokens)``.
        :param count_range: a tuple of two positive integers. If present, there will be chosem ``random.randint(count_range[0], count_range[1])`` tokens from *tokens*.

    .. py:method:: SetInternalVariable(identifier, token)

        Sets an internal variable inside the template that can be referenced afterwards by :py:func:`Token.GetInternalVariable`.

        If another internal variable with the id *identifier* was previously set, it will be overwritten.

        .. note::

            This token will not render in the final result. Its rendering only affects the internal state of the template.

        :param identifier: a string representing the internal variable ID through which it will be referenced later.
        :param token: a :py:class:`Token` instance.

    .. py:method:: GetInternalVariable(identifiers, template)

        Manipulates the internal variables previously set in the template.

        If *identifiers* is a string, *template* must be a callable which takes a single argument.
        If *identifiers* is a list of strings, *template* must be a callable which takes ``len(identifiers)`` parameters.

        This token will render to the result of the *template* function applied on the designated internal variables.


.. py:class:: Template(*tokens)

    :param tokens: a list of tokens that will be parsed in order to generate a mock value.

    .. py:method:: render(seed=None)

        Renders the tokens into the final result. Returns a string.

.. py:class:: BaseGenerator

    The base class for all generators.

    :module: pymockdata.core.base

    .. py:attribute:: ID

        **Abstract attribute**

        The identifier of the generator.

    .. py:attribute:: _templates

        **Abstract attribute**

        A list of :py:class:`Template` instances.

    .. py:method:: on_finish(self, result_string)

        This method is called after the rendering of a template is completed and *result_string* is result.

        Must return a string and can be overwritten in sublcasses, although it is not mandatory. By default, returns
        *result_string*.

    .. py:method:: generate(self, seed=None)

        Chooses a random template and renders it. Returns the final result after calling :py:func:`on_finish` on the result.


