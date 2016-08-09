Usage
=====

Next, we will show how to build a ``DataModel`` with specific field types and choose an ``Exporter``.


Defining the DataModel
----------------------

The :py:func:`DataModel` class encapsulates the fields specifications that need to be generated, and when prompted to
generate the entries, will call the right generators in order to produce the desired results.

Note: use the defined constants in the :py:func:`DataModel` class to avoid typos and to be future proof.

A basic example of :py:func:`DataModel` is::

    model = DataModel(
        customer_name=DataModel.full_name,
        customer_email=DataModel.email,
        customer_ip=DataModel.ipv4_addr
        customer_mac=DataModel.mac
    )

After that, you can generate instances manually by calling :py:func:`DataModel.generate_one` or :py:func:`DataModel.generate_batch` or wrapping it into a :py:class:`DataFactory` instance to
generate and export instances at the same time.


Choosing an exporter
--------------------

There are various exporters to choose from (see :ref:`Exporters <exporters>` for available exporters).

After choosing the right one for your needs, go to nest step.


Generating and exporting
------------------------

This process is done by the :py:class:`DataFactory` class. The code to accomplish that is the following::

    my_data_model = DataModel(...)
    my_exporter = XmlExporter("my_data.xml")  # export data to a XML file
    DataFactory(my_data_model, my_exporter).generate(100)

And after that, you will have exported 100 mock entries into the ``my_data.xml`` file in XML format.

Enjoy :)
