# -*- coding: utf-8 -*-
# Copyright 2013 Rob Ruana
# Licensed under the BSD License, see LICENSE file for details.

"""Tests for :mod:`sphinxcontrib.napoleon.pavertasks` module."""

import os
import shutil
from sphinxcontrib.napoleon.pavertasks import apidoc, html
from unittest import TestCase


class BasePavertasksTest(TestCase):
    def setUp(self):
        if not os.path.exists('tests/docs/build'):
            os.makedirs('tests/docs/build')
        if not os.path.exists('tests/docs/source'):
            os.makedirs('tests/docs/source')
        self.options = {
            'apidoc_excludes': [],
            'apidoc_moduledir': 'tests',
            'apidoc_outputdir': 'tests/docs/source',
            'apidoc_overwrite': True,
            'builddir': 'build',
            'docroot': 'tests/docs',
            'sourcedir': 'source',
        }

    def tearDown(self):
        if os.path.exists('tests/docs/build'):
            shutil.rmtree('tests/docs/build', True)
        super(BasePavertasksTest, self).tearDown()


class ApidocTest(BasePavertasksTest):
    def test_apidoc(self):
        apidoc(self.options)


class HtmlTest(BasePavertasksTest):
    def test_html(self):
        html(self.options)
