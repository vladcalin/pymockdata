Classes
=======


.. py:class:: DataModel(**fields)
              DataModel(seed, **fields)

    The ``fields`` must be pairs of key-type that will specify how the generated entries will look like.

    If specified, the ``seed`` parameter will be used as the seed of the random generator leading to generated controlled
    results. Two different generations with the same seed will lead to the same results. The value must be :py:class:`int`.