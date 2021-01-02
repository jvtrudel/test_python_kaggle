#!/usr/bin/env python

from distutils.core import setup

setup(name='test_python_kaggle',
      version='1.0',
      description='test',
      author='j',
      author_email='j@test.net',
      url='none',
      packages=['pkutils'],
      requires=['numpy','pandas', 'geopandas','matplotlib']
     )
