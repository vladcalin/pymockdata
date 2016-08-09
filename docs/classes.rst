Classes
=======


.. py:class:: DataModel(**fields)
DataModel(seed, **fields)

    The ``fields`` must be pairs of key-type that will specify how the generated entries will look like.

    If specified, the ``seed`` parameter will be used as the seed of the random generator leading to generated controlled
    results. Two different generations with the same seed will lead to the same results. The value must be :py:class:`int`.

    .. py:method:: generate_one(self)

        Generates one mock entry as a :py:class:`dict`. The keys this entry will have will match the ``fields`` keys.

    .. py:method:: generate_batch(self, count)

        Generates a list of *count* entries (see :py:func:`generate_one` for more information about the structure of the entries)


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

        Examples: *mmoran@fuel.biz*, *mblake@swim.es, *ellishardy@flimsy.jp*, *alexandra_shaniatodd@waterjoyously.net*

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


.. py:class:: DataGenerator(seed=None)

    This class is used for generating a single mock instance. See :ref:`defined_field_types` for the supported fields.

    If the *seed* parameter is provided, that value will be used as the random seed.

    Example usage::

        DataGenerator().full_name()
        # Rowan Lincoln Case

        DataGenerator().mac_addr()
        # 65:1d:73:80:3f:42

    .. note::

            If the DataModel has an constant defined, the :py:class:`DataGenerator` class exposes a corresponding callable
            that is used to generate one instance of mock data of that type. For example, if :py:class:`DataModel` has defined
            the attribute :py:attr:`DataModel.full_name`, the :py:func:`DataGenerator.full_name()` will generate one value of that kind.


