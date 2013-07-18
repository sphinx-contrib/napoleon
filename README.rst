Napoleon - *Marching toward legible docstrings*
-----------------------------------------------

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
`docstrings`_. Compare the mess above to the same thing rewritten
according to the `Google Python Style Guide`_::

    Args:
        path (str): The path of the file to wrap
        field_storage (FileStorage): The :class:`FileStorage` instance to wrap
        temporary (bool): Whether or not to delete the file when the File
           instance is destructed

    Returns:
        BufferedFileStorage: A buffered writable file descriptor

Much more legible, no? Napoleon is a `Sphinx extension`_ that allows you to
write readable API documentation in your source code. Napoleon understands
both `Google`_ and `NumPy`_ style docstrings.

.. _ReStructuredText: http://docutils.sourceforge.net/rst.html
.. _docstrings: http://www.python.org/dev/peps/pep-0287/
.. _Google Python Style Guide:
   http://google-styleguide.googlecode.com/svn/trunk/pyguide.html
.. _Sphinx extension: http://sphinx-doc.org/extensions.html
.. _Google:
   http://google-styleguide.googlecode.com/svn/trunk/pyguide.html#Comments
.. _NumPy:
   https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt

Getting Started
---------------

After `setting up Sphinx`_ to build your project docs, install the
`sphinxcontrib-napoleon`_ package::

    $ pip install sphinxcontrib-napoleon

Enable napoleon in the Sphinx `conf.py` file::

    # conf.py

    # Add autodoc and napoleon to the extensions list
    extensions = ['sphinx.ext.autodoc', 'sphinxcontrib.napoleon']

.. _setting up Sphinx: http://sphinx-doc.org/tutorial.html
.. _sphinxcontrib-napoleon: http://pypi.python.org/pypi/sphinxcontrib-napoleon

Docstrings
----------

Napoleon supports two styles of docstrings: `Google`_ and `NumPy`_. The main
difference between the two styles is that Google uses indention to separate
sections, whereas NumPy uses underlines::

    # Google Style

    Args:
        arg1 (int): Description of arg1
        arg2 (str): Description of arg2

    Returns:
        bool: Description of return value

::

    # NumPy Style

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

NumPy style tends to require more vertical space, whereas Google style tends
to use more horizontal space. Google style tends to be easier to read for
short and simple docstrings, whereas NumPy style tends be easier to read for
long and in-depth docstrings.

The choice between styles is largely aesthetic, but the two styles should not
be mixed. Choose one style for your project and be consistent with it.

Development Setup
-----------------

Prerequisites
^^^^^^^^^^^^^
* Python - ``sudo brew install python``
* Paver - ``sudo pip install paver``

Dev Environment
^^^^^^^^^^^^^^^

::

    $ paver bootstrap
    $ source virtualenv/bin/activate
    $ python setup.py develop
