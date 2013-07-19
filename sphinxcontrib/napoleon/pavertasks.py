# -*- coding: utf-8 -*-
# Copyright 2013 Rob Ruana
# Licensed under the BSD License, see LICENSE file for details.

"""Sphinx related paver tasks.

Methods
-------
apidoc
    Derive reStructuredText API doc files from python source code.

    This task is essentially a wrapper around the `sphinx-apidoc`_ script.
    The following settings can be set on the options object:

    * ``apidoc_excludes`` -- (*str or list of str*) A directory or list of
      directories to exclude from doc generation. These should either be
      absolute paths, or relative to `apidoc_moduledir`
    * ``apidoc_moduledir`` -- (*str*) The root directory to search for Python
      modules. Defaults to "."
    * ``apidoc_outputdir`` -- (*str*) The output directory. Defaults to
      `options.docroot/options.sourcedir`
    * ``apidoc_overwrite`` -- (*bool*) True to overwrite existing files.
      Defaults to True

    .. _sphinx-apidoc: http://sphinx-doc.org/man/sphinx-apidoc.html

    Example
    -------

    Creating API documentation is easy with a `pavement.py` file like this::

        # pavement.py

        from sphinxcontrib.napoleon.pavertasks import apidoc, html
        from paver.easy import *

        options(
            sphinx=Bunch(
                apidoc_excludes=['tests'],
                apidoc_moduledir='sphinxcontrib/napoleon',
                apidoc_outputdir='docs/source',
                apidoc_overwrite=True,

                builddir='build',
                docroot='docs',
                sourcedir='source',
            ),
        )

    And call::

        $ paver apidoc
        ---> sphinxcontrib.napoleon.pavertasks.apidoc
        sphinx-apidoc -f -o docs/source sphinxcontrib tests
        Creating file docs/source/sphinxcontrib.rst.
        Creating file docs/source/sphinxcontrib.napoleon.rst.
        Creating file docs/source/modules.rst.

html
    Build HTML documentation, including API documentation.

    This task is a convenience method for calling `apidoc` followed by
    `paver.docutils.html`. To use it, simply import it in your `pavement.py`
    file::

        from sphinxcontrib.napoleon.pavertasks import html

    And call::

        $ paver html

"""

import os

try:
    from paver.easy import BuildFailure, needs, task
    has_paver = True
    BuildError = BuildFailure
except ImportError:
    has_paver = False
    BuildError = ValueError

try:
    import sphinx
    assert(sphinx)
    has_sphinx = True
except ImportError:
    has_sphinx = False


def apidoc(options):
    if not has_sphinx:
        raise BuildError('Install sphinx to build html docs')

    outputdir = options.get('apidoc_outputdir', '')
    if not outputdir:
        docroot = options.get('docroot', 'docs')
        if not os.path.exists(docroot):
            raise BuildError('Doc root dir (%s) does not exist' % docroot)
        outputdir = os.path.join(docroot, options.get('sourcedir', ''))
    if not os.path.exists(outputdir):
        raise BuildError('Doc source dir (%s) does not exist' % outputdir)

    moduledir = options.get('apidoc_moduledir', '.')
    if not os.path.exists(moduledir):
        raise BuildError('Module dir (%s) does not exist' % moduledir)

    excludes = options.get('apidoc_excludes', [])
    if isinstance(excludes, basestring):
        excludes = [excludes]

    if options.get('apidoc_overwrite', True):
        args = ['sphinx-apidoc', '-f']
    else:
        args = ['sphinx-apidoc']

    from sphinx.apidoc import main
    args.extend(['-o', outputdir, moduledir] + excludes)
    print(' '.join(args))
    main(args)


def html(options):
    pass


if has_paver:
    apidoc = task(apidoc)
    html = task(needs('sphinxcontrib.napoleon.pavertasks.apidoc',
                      'paver.doctools.html')(html))
else:
    class _Task(object):
        def __init__(self, func):
            self.func = func

        def __call__(self, *args, **kwargs):
            self.func(*args, **kwargs)

    apidoc = _Task(apidoc)
    html = _Task(html)
