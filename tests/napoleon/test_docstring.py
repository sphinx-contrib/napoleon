# -*- coding: utf-8 -*-
# Copyright 2014 Rob Ruana
# Licensed under the BSD License, see LICENSE file for details.

"""Tests for :mod:`sphinxcontrib.napoleon.docstring` module."""

from collections import namedtuple

# inspect.cleandoc() implements the trim() function from PEP 257
from inspect import cleandoc
from textwrap import dedent
from sphinxcontrib.napoleon import Config
from sphinxcontrib.napoleon.docstring import GoogleDocstring, NumpyDocstring
from unittest import TestCase

try:
    # Python >=3.3
    from unittest.mock import Mock
except ImportError:
    from mock import Mock


class NamedtupleSubclass(namedtuple('NamedtupleSubclass', ('attr1', 'attr2'))):
    """Sample namedtuple subclass

    Attributes
    ----------
    attr1 : Arbitrary type
        Quick description of attr1
    attr2 : Another arbitrary type
        Quick description of attr2

    """
    # To avoid creating a dict, as a namedtuple doesn't have it:
    __slots__ = ()

    def __new__(cls, attr1, attr2=None):
        return super(NamedtupleSubclass, cls).__new__(cls, attr1, attr2)


class BaseDocstringTest(TestCase):
    pass


class NamedtupleSubclassTest(BaseDocstringTest):
    def test_attributes_docstring(self):
        config = Config()
        actual = str(NumpyDocstring(cleandoc(NamedtupleSubclass.__doc__),
                     config=config, app=None, what='class',
                     name='NamedtupleSubclass', obj=NamedtupleSubclass))
        expected = dedent("""\
           Sample namedtuple subclass

           .. attribute:: attr1

              *Arbitrary type*

              Quick description of attr1

           .. attribute:: attr2

              *Another arbitrary type*

              Quick description of attr2
           """)

        self.assertEqual(expected, actual)


class GoogleDocstringTest(BaseDocstringTest):
    docstrings = [(
        """Single line summary""",
        """Single line summary"""
    ), (
        """
        Single line summary

        Extended description

        """,
        """
        Single line summary

        Extended description
        """
    ), (
        """
        Single line summary

        Args:
          arg1(str):Extended
            description of arg1
        """,
        """
        Single line summary

        :Parameters: **arg1** (*str*) --
                     Extended
                     description of arg1"""
    ), (
        """
        Single line summary

        Args:
          arg1(str):Extended
            description of arg1
          arg2 ( int ) : Extended
            description of arg2

        Keyword Args:
          kwarg1(str):Extended
            description of kwarg1
          kwarg2 ( int ) : Extended
            description of kwarg2""",
        """
        Single line summary

        :Parameters: * **arg1** (*str*) --
                       Extended
                       description of arg1
                     * **arg2** (*int*) --
                       Extended
                       description of arg2

        :Keyword Arguments: * **kwarg1** (*str*) --
                              Extended
                              description of kwarg1
                            * **kwarg2** (*int*) --
                              Extended
                              description of kwarg2"""
    ), (
        """
        Single line summary

        Arguments:
          arg1(str):Extended
            description of arg1
          arg2 ( int ) : Extended
            description of arg2

        Keyword Arguments:
          kwarg1(str):Extended
            description of kwarg1
          kwarg2 ( int ) : Extended
            description of kwarg2""",
        """
        Single line summary

        :Parameters: * **arg1** (*str*) --
                       Extended
                       description of arg1
                     * **arg2** (*int*) --
                       Extended
                       description of arg2

        :Keyword Arguments: * **kwarg1** (*str*) --
                              Extended
                              description of kwarg1
                            * **kwarg2** (*int*) --
                              Extended
                              description of kwarg2"""
    ), (
        """
        Single line summary

        Return:
          str:Extended
          description of return value
        """,
        """
        Single line summary

        :returns: *str* --
                  Extended
                  description of return value"""
    ), (
        """
        Single line summary

        Returns:
          str:Extended
          description of return value
        """,
        """
        Single line summary

        :returns: *str* --
                  Extended
                  description of return value"""
    ), (
        """
        Single line summary

        Returns:
          Extended
          description of return value
        """,
        """
        Single line summary

        :returns: Extended
                  description of return value"""
    ), (
        """
        Single line summary

        Args:
          arg1(str):Extended
            description of arg1
          *args: Variable length argument list.
          **kwargs: Arbitrary keyword arguments.
        """,
        """
        Single line summary

        :Parameters: * **arg1** (*str*) --
                       Extended
                       description of arg1
                     * **\\*args** --
                       Variable length argument list.
                     * **\\*\\*kwargs** --
                       Arbitrary keyword arguments."""
    ), (
        """
        Single line summary

        Yield:
          str:Extended
          description of yielded value
        """,
        """
        Single line summary

        :Yields: *str* --
                 Extended
                 description of yielded value"""
    ), (
        """
        Single line summary

        Yields:
          Extended
          description of yielded value
        """,
        """
        Single line summary

        :Yields: Extended
                 description of yielded value"""
    )]

    def test_docstrings(self):
        config = Config(napoleon_use_param=False, napoleon_use_rtype=False)
        for docstring, expected in self.docstrings:
            actual = str(GoogleDocstring(dedent(docstring), config))
            expected = dedent(expected)
            self.assertEqual(expected, actual)

    def test_parameters_with_class_reference(self):
        docstring = """\
Construct a new XBlock.

This class should only be used by runtimes.

Arguments:
    runtime (:class:`Runtime`): Use it to access the environment.
        It is available in XBlock code as ``self.runtime``.

    field_data (:class:`FieldData`): Interface used by the XBlock
        fields to access their data from wherever it is persisted.

    scope_ids (:class:`ScopeIds`): Identifiers needed to resolve scopes.

"""

        actual = str(GoogleDocstring(docstring))
        expected = """\
Construct a new XBlock.

This class should only be used by runtimes.

:param runtime: Use it to access the environment.
                It is available in XBlock code as ``self.runtime``.

:type runtime: :class:`Runtime`
:param field_data: Interface used by the XBlock
                   fields to access their data from wherever it is persisted.

:type field_data: :class:`FieldData`
:param scope_ids: Identifiers needed to resolve scopes.

:type scope_ids: :class:`ScopeIds`
"""
        self.assertEqual(expected, actual)

    def test_attributes_with_class_reference(self):
        docstring = """\
Attributes:
    in_attr(:class:`numpy.ndarray`): super-dooper attribute
"""

        actual = str(GoogleDocstring(docstring))
        expected = """\
.. attribute:: in_attr

   :class:`numpy.ndarray`

   super-dooper attribute
"""
        self.assertEqual(expected, actual)

        docstring = """\
Attributes:
    in_attr(numpy.ndarray): super-dooper attribute
"""

        actual = str(GoogleDocstring(docstring))
        expected = """\
.. attribute:: in_attr

   *numpy.ndarray*

   super-dooper attribute
"""
        self.assertEqual(expected, actual)


class NumpyDocstringTest(BaseDocstringTest):
    docstrings = [(
        """Single line summary""",
        """Single line summary"""
    ), (
        """
        Single line summary

        Extended description

        """,
        """
        Single line summary

        Extended description
        """
    ), (
        """
        Single line summary

        Parameters
        ----------
        arg1:str
            Extended
            description of arg1
        """,
        """
        Single line summary

        :Parameters: **arg1** (*str*) --
                     Extended
                     description of arg1"""
    ), (
        """
        Single line summary

        Parameters
        ----------
        arg1:str
            Extended
            description of arg1
        arg2 : int
            Extended
            description of arg2

        Keyword Arguments
        -----------------
          kwarg1:str
              Extended
              description of kwarg1
          kwarg2 : int
              Extended
              description of kwarg2
        """,
        """
        Single line summary

        :Parameters: * **arg1** (*str*) --
                       Extended
                       description of arg1
                     * **arg2** (*int*) --
                       Extended
                       description of arg2

        :Keyword Arguments: * **kwarg1** (*str*) --
                              Extended
                              description of kwarg1
                            * **kwarg2** (*int*) --
                              Extended
                              description of kwarg2"""
    ), (
        """
        Single line summary

        Return
        ------
        str
            Extended
            description of return value
        """,
        """
        Single line summary

        :returns: *str* --
                  Extended
                  description of return value"""
    ), (
        """
        Single line summary

        Returns
        -------
        str
            Extended
            description of return value
        """,
        """
        Single line summary

        :returns: *str* --
                  Extended
                  description of return value"""
    ), (
        """
        Single line summary

        Parameters
        ----------
        arg1:str
             Extended description of arg1
        *args:
            Variable length argument list.
        **kwargs:
            Arbitrary keyword arguments.
        """,
        """
        Single line summary

        :Parameters: * **arg1** (*str*) --
                       Extended description of arg1
                     * ***args** --
                       Variable length argument list.
                     * ****kwargs** --
                       Arbitrary keyword arguments."""
    ), (
        """
        Single line summary

        Yield
        -----
        str
            Extended
            description of yielded value
        """,
        """
        Single line summary

        :Yields: *str* --
                 Extended
                 description of yielded value"""
    ), (
        """
        Single line summary

        Yields
        ------
        str
            Extended
            description of yielded value
        """,
        """
        Single line summary

        :Yields: *str* --
                 Extended
                 description of yielded value"""
    )]

    def test_docstrings(self):
        config = Config(napoleon_use_param=False, napoleon_use_rtype=False)
        for docstring, expected in self.docstrings:
            actual = str(NumpyDocstring(dedent(docstring), config))
            expected = dedent(expected)
            self.assertEqual(expected, actual)

    def test_parameters_with_class_reference(self):
        docstring = """\
Parameters
----------
param1 : :class:`MyClass <name.space.MyClass>` instance

"""

        config = Config(napoleon_use_param=False)
        actual = str(NumpyDocstring(docstring, config))
        expected = """\
:Parameters: **param1** (:class:`MyClass <name.space.MyClass>` instance)
"""
        self.assertEqual(expected, actual)

        config = Config(napoleon_use_param=True)
        actual = str(NumpyDocstring(docstring, config))
        expected = """\
:param param1:
:type param1: :class:`MyClass <name.space.MyClass>` instance
"""
        self.assertEqual(expected, actual)

    def test_parameters_without_class_reference(self):
        docstring = """\
Parameters
----------
param1 : MyClass instance

"""

        config = Config(napoleon_use_param=False)
        actual = str(NumpyDocstring(docstring, config))
        expected = """\
:Parameters: **param1** (*MyClass instance*)
"""
        self.assertEqual(expected, actual)

        config = Config(napoleon_use_param=True)
        actual = str(NumpyDocstring(dedent(docstring), config))
        expected = """\
:param param1:
:type param1: MyClass instance
"""
        self.assertEqual(expected, actual)

    def test_see_also_refs(self):
        docstring = """\
numpy.multivariate_normal(mean, cov, shape=None, spam=None)

See Also
--------
some, other, funcs
otherfunc : relationship

"""

        actual = str(NumpyDocstring(docstring))

        expected = """\
numpy.multivariate_normal(mean, cov, shape=None, spam=None)

.. seealso::

   :obj:`some`, :obj:`other`, :obj:`funcs`
   \n\
   :obj:`otherfunc`
       relationship
"""
        self.assertEqual(expected, actual)

        docstring = """\
numpy.multivariate_normal(mean, cov, shape=None, spam=None)

See Also
--------
some, other, funcs
otherfunc : relationship

"""

        config = Config()
        app = Mock()
        actual = str(NumpyDocstring(docstring, config, app, "method"))

        expected = """\
numpy.multivariate_normal(mean, cov, shape=None, spam=None)

.. seealso::

   :meth:`some`, :meth:`other`, :meth:`funcs`
   \n\
   :meth:`otherfunc`
       relationship
"""
        self.assertEqual(expected, actual)
