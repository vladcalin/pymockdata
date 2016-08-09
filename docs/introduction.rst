Introduction
============


To be honest, the main motivation behind this project is fun. I built this library for the fun of programming and because
I wanted to provide a tool for automatic generation of test data, that is delivered in various popular formats (XML,
JSON, HTML) or directly into a database.


Although there are a better alternatives out there (such as `fake-factory <https://github.com/joke2k/faker>`_ that has more
features, including localization and more types of generated values), there is no easy method to easily populate your
database with such values without writing your own code.

General terms and workflow
--------------------------

The mock data generation and exporting are split into various components:

- :ref:`Datasets <datasets>` - a list of words that are used for generating data.
- Template - a collection of :py:class:`Token` instances that are parsed in order to generate the final mock value.
- Generator - a collection of :py:class:`Template` that defines what to generate.
- Exporter - a utility class that exports a set of generated entries to a specific format. (see :ref:`Exporters <exporters>`)


The general workfolow is the following::

    exporter = Exporter(exporting_params)
    model = Model(
        field1=type_of_field1,
        field2=type_of_field2,
        field3=type_of_field3,
        ...
    )
    Factory(model, exporter).generate(amount)

and after that, you have `amount` mocked instances with the `field`, `field2` ... fields into the desired format, depending
on the exporter you chose.

Or if you do not need to export the entries, you can just do::

    model.generate_one()

or::

    model.generate_batch(amount)

and do whatever you please with the instances.

Generated value types
---------------------

Currently, the following types of values can be generated:

- ``female_name``
- ``male_name``
- ``last_name``
- ``full_female_name``
- ``full_male_name``
- ``full_name``

- ``noun``
- ``adjective``

- ``forum_username``
- ``professional_username`` (derived from a full name)
- ``email``
- ``domain``
- ``tld``

- ``ipv4_addr``
- ``ipv6_addr``
- ``mac_addr``


See :ref:`supported field types <defined_field_types>` for a detailed description of each field and how to use them.