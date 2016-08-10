Usage
=====

Next, we will show how to build a ``DataModel`` with specific field types.

The :py:func:`DataModel` class encapsulates the fields specifications that need to be generated, and when prompted to
generate the entries, will call the right generators in order to produce the desired results.

.. note::

    Use the defined constants in the :py:func:`DataModel` class to avoid typos and to be future proof.
    For more information, see :ref:`supported field types <defined_field_types>`.

A basic example of :py:func:`DataModel` is::

    model = DataModel(
        customer_name=DataModel.full_name,
        customer_email=DataModel.email,
        customer_ip=DataModel.ipv4_addr
        customer_mac=DataModel.mac
    )

After that, you can generate instances manually by calling :py:func:`DataModel.generate_one` or :py:func:`DataModel.generate_batch`.

An alternative for generating a single value of a kind, is by using the :py:func:`DataModel.value_for` method::

    DataModel().value_for(DataModel.domain)
    # lightning.org

Enjoy :)
