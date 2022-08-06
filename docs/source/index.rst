.. Napoleon documentation master file.

Napoleon - *Marching toward legible docstrings*
===============================================

.. note:: As of Sphinx 1.3, the napoleon extension will come packaged with
   Sphinx under `sphinx.ext.napoleon`. The `sphinxcontrib.napoleon` extension
   will continue to work with Sphinx <= 1.2.

Are you tired of writing docstrings that look like this::

    :param path: The path of the file to wrap
    :type path: str
    :param field_storage: The :class:`FileStorage` instance to wrap
    :type field_storage: FileStorage
    :param temporary: Whether or not to delete the file when the File
       instance is destructed
    :type temporary: bool
    :returns: A buffered writable file descriptor
    :rtype: BufferedFileStorage

`ReStructuredText`_ is great, but it creates visually dense, hard to read
`docstrings`_. Compare the jumble above to the same thing rewritten
according to the `Google Python Style Guide`_::

    Args:
        path (str): The path of the file to wrap
        field_storage (FileStorage): The :class:`FileStorage` instance to wrap
        temporary (bool): Whether or not to delete the file when the File
           instance is destructed

    Returns:
        BufferedFileStorage: A buffered writable file descriptor

Much more legible, no?

Napoleon is a `Sphinx extension`_ that enables Sphinx to parse both `NumPy`_
and `Google`_ style docstrings - the style recommended by `Khan Academy`_.

Napoleon is a pre-processor that parses `NumPy`_ and `Google`_ style
docstrings and converts them to reStructuredText before Sphinx attempts to
parse them. This happens in an intermediate step while Sphinx is processing
the documentation, so it doesn't modify any of the docstrings in your actual
source code files.

.. _ReStructuredText: http://docutils.sourceforge.net/rst.html
.. _docstrings: http://www.python.org/dev/peps/pep-0287/
.. _Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html
.. _Sphinx extension: http://sphinx-doc.org/extensions.html
.. _Google:
   http://google.github.io/styleguide/pyguide.html#Comments
.. _NumPy:
   https://numpydoc.readthedocs.io/en/latest/example.html#module-example
.. _Khan Academy:
   https://sites.google.com/a/khanacademy.org/forge/for-developers/styleguide/python#TOC-Docstrings

Getting Started
---------------

1. Install the napoleon extension::

       $ pip install sphinxcontrib-napoleon

2. After `setting up Sphinx`_ to build your docs, enable napoleon in the
   Sphinx `conf.py` file::

       # conf.py

       # Add napoleon to the extensions list
       extensions = ['sphinxcontrib.napoleon']

3. Use `sphinx-apidoc` to build your API documentation::

       $ sphinx-apidoc -f -o docs/source projectdir

.. _setting up Sphinx: http://sphinx-doc.org/tutorial.html

Docstrings
----------

Napoleon interprets every docstring that `Sphinx autodoc`_ can find,
including docstrings on: ``modules``, ``classes``, ``attributes``,
``methods``, ``functions``, and ``variables``. Inside each docstring,
specially formatted `Sections`_ are parsed and converted to
reStructuredText.

All standard reStructuredText formatting still works as expected.

.. _Sphinx autodoc: http://sphinx-doc.org/ext/autodoc.html


.. _Sections:

Docstring Sections
------------------

All of the following section headers are supported:

    * ``Args`` *(alias of Parameters)*
    * ``Arguments`` *(alias of Parameters)*
    * ``Attributes``
    * ``Example``
    * ``Examples``
    * ``Keyword Args`` *(alias of Keyword Arguments)*
    * ``Keyword Arguments``
    * ``Methods``
    * ``Note``
    * ``Notes``
    * ``Other Parameters``
    * ``Parameters``
    * ``Return`` *(alias of Returns)*
    * ``Returns``
    * ``Raises``
    * ``References``
    * ``See Also``
    * ``Todo``
    * ``Warning``
    * ``Warnings`` *(alias of Warning)*
    * ``Warns``
    * ``Yield`` *(alias of Yields)*
    * ``Yields``

Google vs NumPy
---------------

Napoleon supports two styles of docstrings: `Google`_ and `NumPy`_. The
main difference between the two styles is that Google uses indention to
separate sections, whereas NumPy uses underlines.

Google style::

    def func(arg1, arg2):
        """Summary line.

        Extended description of function.

        Args:
            arg1 (int): Description of arg1
            arg2 (str): Description of arg2

        Returns:
            bool: Description of return value

        """
        return True

NumPy style::

    def func(arg1, arg2):
        """Summary line.

        Extended description of function.

        Parameters
        ----------
        arg1 : int
            Description of arg1
        arg2 : str
            Description of arg2

        Returns
        -------
        bool
            Description of return value

        """
        return True

NumPy style tends to require more vertical space, whereas Google style
tends to use more horizontal space. Google style tends to be easier to
read for short and simple docstrings, whereas NumPy style tends be easier
to read for long and in-depth docstrings.

The `Khan Academy`_ recommends using Google style.

The choice between styles is largely aesthetic, but the two styles should
not be mixed. Choose one style for your project and be consistent with it.

.. seealso::

   For complete examples:

   * :ref:`example_google`
   * :ref:`example_numpy`


Type Annotations
----------------

`PEP 484`_ introduced a standard way to express types in Python code.
This is an alternative to expressing types directly in docstrings.
One benefit of expressing types according to `PEP 484`_ is that
type checkers and IDEs can take advantage of them for static code
analysis.

Google style with Python 3 type annotations::

    def func(arg1: int, arg2: str) -> bool:
        """Summary line.

        Extended description of function.

        Args:
            arg1: Description of arg1
            arg2: Description of arg2

        Returns:
            Description of return value

        """
        return True

Google style with types in docstrings::

    def func(arg1, arg2):
        """Summary line.

        Extended description of function.

        Args:
            arg1 (int): Description of arg1
            arg2 (str): Description of arg2

        Returns:
            bool: Description of return value

        """
        return True

.. Note::
   `Python 2/3 compatible annotations`_ aren't currently
   supported by Sphinx and won't show up in the docs.

.. _PEP 484:
   https://www.python.org/dev/peps/pep-0484/

.. _Python 2/3 compatible annotations:
   https://www.python.org/dev/peps/pep-0484/#suggested-syntax-for-python-2-7-and-straddling-code


Configuration
=============

For detailed configuration options see :class:`sphinxcontrib.napoleon.Config`.


Index
=====
.. toctree::
   :maxdepth: 2

   sphinxcontrib.napoleon


* :ref:`example_google`
* :ref:`example_numpy`

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
