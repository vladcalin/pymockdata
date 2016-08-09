Classes
=======



DataModel
---------

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

Defined constants for field types
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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


.. _exporters:

Exporters
---------

The examples provided in this section are generated for the following dataset::

    data_model = DataModel(
        name=DataModel.full_name,
        email=DataModel.email,
        ip=DataModel.ipv4_addr,
        mac=DataModel.mac_addr,
    )

.. py:class:: StreamExporter(stream=sys.stdout)

    :module: pymockdata.exporters

    A class that writes the exported data dirrectly to a stream. If no stream is provided, will write to ``sys.stdout``.

    Example output::

        email: msimpson@clearlynormally.ru
        mac: 4f:f7:12:54:af:ec
        ip: 240.75.43.110
        name: Bo-Chaim N. Farmer

        email: guillermo_adrielnunez@striped.net
        mac: f:9f:39:6e:fc:d3
        ip: 30.164.190.200
        name: Jade Buck

        ...

.. py:class:: JsonExporter(filename="output.json")

    :module: pymockdata.exporters.file

    A class that writes the exported data to a JSON file (defaults to ``./output.json``)

    Example output::

        {
            "entries": [
                {
                    "email": "mmullen@kindheartedly.ro",
                    "ip": "0.233.170.225",
                    "mac": "ee:73:d0:7a:2d:2e",
                    "name": "Jamya Carissa I. Barron"
                },
                {
                    "email": "ann_estrellamorris@difficult.net",
                    "ip": "194.9.155.138",
                    "mac": "41:9a:e7:21:3:8e",
                    "name": "Gina Walton"
                },
                ...

.. py:class:: XmlExporter(filename="output.xml")

    :module: pymockdata.exporters.file

    A class that writes the exported data to a XML file. The root element is ``data`` and its children are ``entry`` elements which contains
    a child element ``<atr_name>attr_value</attr_name>`` where ``attr_name`` is the name of the dataset value to be generated and ``attr_value`` is its value.

    Example output::

        <data>
            <entry>
                <mac>88:c8:ee:6a:de:6</mac>
                <email>leia_abbeyhess@hook.biz</email>
                <ip>22.213.243.143</ip>
                <name>Madalynn-Cloe Chen</name>
            </entry>
            <entry>
                <mac>fc:e8:1:c5:5:c8</mac>
                <email>jasiahmoreno@nine.org</email>
                <ip>91.174.188.183</ip>
                <name>Makai Yosef Rollins</name>
            </entry>
            ...

.. py:class:: CsvExporter(filename="output.csv")

    :module: pymockdata.exporters.file

    A class that writes the generated data to a CSV file, using ``;`` as separator.

    **NOTE: the value names are not preserved.**

    Example output::

        1a:79:c9:d:5b:78;166.3.125.8;Claudia-Lillian Alvarez;perla_lexiewest@chalk.ru
        1a:97:b7:41:b:ba;125.215.152.254;Gisselle Desirae Hanna;tjacobs@slowly.es
        70:ea:f2:2f:3a:b2;84.144.132.11;Rayan Alan D. Owen;javier_franciscopayne@quirkily.com
        c3:5d:e0:7c:42:18;249.46.117.215;Zander M. Walter;tate_skylar_p_farmer@invincible.ru
        4e:dd:36:d2:5b:42;136.124.41.59;Brianna Kristina Webb;eden_jarrettmcdowell@scrawny.ru
        7:49:f4:5c:91:2e;0.234.78.202;Abbey Zaniyah Stewart;ioliver@brightly.ro
        ...


.. py:class:: HtmlTableExporter(filename="output.html")

    :module: pymockdata.exporters.file

    A class that writes the generated data to a HTML file, in a tabular structure.

    Example output::

        <table>
            <thead>
            <tr>
                <th>mac</th>
                <th>ip</th>
                <th>name</th>
                <th>email</th>
            </tr>
            </thead>
            <tbody>
            <tr>
                <td>7c:7:31:3f:e:f7</td>
                <td>105.181.61.159</td>
                <td>Jeffery-Baron H. Benson</td>
                <td>mrice@actually.md</td>
            </tr>
            <tr>
                <td>f8:98:d1:6d:d3:67</td>
                <td>190.143.124.191</td>
                <td>Conner Brown</td>
                <td>jamiedavis@dock.us</td>
            </tr>
            ...

The DataFactory class
---------------------

.. py:class:: DataFactory(data_model, exporter=StreamExporter())

    :module: pymockdata

    Wraps a :py:class:`DataModel` instance and a :py:class:`Exporter` instance (see :ref:`Exporters <exporters>` for more information) for generating and exporting entries at the same time.

    .. py:function:: generate(count)

        Generates ``count`` instances through the provided data_model instance and exports them through the provided generator





