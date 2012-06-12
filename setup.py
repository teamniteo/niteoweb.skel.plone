# -*- coding: utf-8 -*-
"""Installer for this package."""

from setuptools import find_packages
from setuptools import setup

import os


# shamlessly stolen from Hexagon IT guys
def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

version = read('src', 'niteoweb', 'zulu', 'version.txt').strip()

setup(name='niteoweb.zulu',
      version=version,
      description="Enter description of what this project is all about.",
      long_description=read('README.rst') +
                       read('docs', 'HISTORY.rst') +
                       read('docs', 'LICENSE.rst'),
      # Get more strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
          "Framework :: Plone",
          "Programming Language :: Python",
      ],
      keywords='Plone Python',
      author='NiteoWeb Ltd.',
      author_email='info@niteoweb.com',
      url='http://www.niteoweb.com',
      license='BSD',
      packages=find_packages('src', exclude=['ez_setup']),
      namespace_packages=['niteoweb'],
      package_dir={'': 'src'},
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'niteoweb.loginas',
          'niteoweb.fabfile',
          'plone.app.caching',
          'plone.app.theming',
          'setuptools',
          'z3c.jbot',
          'Plone',
          'Pillow',
          'five.pt',
      ],
      extras_require={
          'test': [
              'mock',
              'plone.app.testing',
              'unittest2',
          ],
          'develop': [
              'plone.reload',
              'plone.app.debugtoolbar',
              'Products.Clouseau',
              'Products.DocFinderTab',
              'Products.PDBDebugMode',
              'Products.PrintingMailHost',
              'zptlint',
              'pep8',
              'setuptools-flakes',  # this install "python setup.py flakes" command
              'zest.releaser',
              'jarn.mkrelease',
          ],
      },
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
)
