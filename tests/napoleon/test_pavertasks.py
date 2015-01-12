# -*- coding: utf-8 -*-
# Copyright 2014 Rob Ruana
# Licensed under the BSD License, see LICENSE file for details.

"""Tests for :mod:`sphinxcontrib.napoleon.pavertasks` module."""

import os
import shutil
from paver.easy import options
from sphinxcontrib.napoleon.pavertasks import apidoc
from unittest import TestCase


class BasePavertasksTest(TestCase):
    def setUp(self):
        if not os.path.exists('tests/docs/build'):
            os.makedirs('tests/docs/build')
        if not os.path.exists('tests/docs/source'):
            os.makedirs('tests/docs/source')
        options.apidoc_excludes = []
        options.apidoc_moduledir = 'tests'
        options.apidoc_outputdir = 'tests/docs/source'
        options.apidoc_overwrite = True
        options.builddir = 'build'
        options.docroot = 'tests/docs'
        options.sourcedir = 'source'

    def tearDown(self):
        if os.path.exists('tests/docs/build'):
            shutil.rmtree('tests/docs/build', True)
        super(BasePavertasksTest, self).tearDown()


class ApidocTest(BasePavertasksTest):
    def test_apidoc(self):
        apidoc(options)
