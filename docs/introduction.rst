Introduction
============


The pymockdata module generates mock data and offers the possibility to export it directly into popular file format
(such as CSV, JSON, XML) or export it into a database o your choice (currently supported databases are: SQLite)


General workflow
----------------

The mock data generation and exporting are split into various components:

- :ref:`Datasets <datasets>` - a list of words that are used for generating data.
- Template - a collection of :py:class:`Token` instances that are parsed in order to generate the final mock value.
- Generator - a collection of :py:class:`Template` that defines what to generate.
- Exporter - a utility class that exports a set of generated entries to a specific format.



