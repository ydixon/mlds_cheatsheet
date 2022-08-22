.. _sphinx_guide:

================
Sphinx Guide
================

.. contents:: :local:



.. rubric:: Markdown parsing

.. code::

    conf.py

    extensions = ['sphinx.ext.mathjax',
                'sphinx.ext.githubpages',
                # 'recommonmark',
                'myst_parser',
                ]

    myst_enable_extensions = [
        "amsmath",
        "dollarmath",

    ]

    myst_dmath_double_inline = True

.. code:: 

    Use case:

    .. include:: markdown/matrix_multiplication_element_form.md
       :parser: myst_parser.sphinx_

    
