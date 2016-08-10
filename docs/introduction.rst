Introduction
============


To be honest, the main motivation behind this project is fun. I built this library for the fun of programming and because
I wanted to provide a tool for automatic generation of test data that is lightweight, with no external dependencies, and
that is easy to extend and comprehend.

Although there are a better alternatives out there (such as `fake-factory <https://github.com/joke2k/faker>`_ that has more
features, including localization and more types of generated values), ``pymockdata`` wants to be a simple and lightweight
library for mock data generation that is easy to extend.

General workflow
----------------


Basically in order to generate data, you have to define your data model and then generate data using it. See how in :doc:`usage`.

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

- ``md5``
- ``file_extension``


See :ref:`supported field types <defined_field_types>` for a detailed description of each field and how to use them.