# -*- coding: utf-8 -*-
# Copyright 2013 Rob Ruana
# Licensed under the BSD License, see LICENSE file for details.

"""Python 3 compatibility helpers."""

from __future__ import division
from __future__ import absolute_import

import sys


PY3 = sys.version_info[0] >= 3
if PY3:
    basestring = str
    unicode = str
    string_types = str
    callable = lambda o: hasattr(o, '__call__')
    xrange = range

    def u(s):
        return s
else:
    basestring = basestring
    unicode = unicode
    string_types = basestring
    callable = callable
    xrange = xrange

    def u(s):
        return unicode(s.replace(r'\\', r'\\\\'), "unicode_escape")


class UnicodeMixin(object):
    """Mixin class to handle defining the proper __str__/__unicode__
    methods in Python 2 or 3."""

    if PY3:  # Python 3
        def __str__(self):
            return self.__unicode__()
    else:  # Python 2
        def __str__(self):
            return self.__unicode__().encode('utf8')
