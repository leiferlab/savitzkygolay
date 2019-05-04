#!/usr/bin/env python

from distutils.core import setup

setup(name='savitzkygolay',
      version='1.0',
      description='Providing Savitzky-Golay filters',
      author='Francesco Randi',
      author_email='francesco.randi@gmail.com',
      packages=['savitzkygolay'],
      package_data={'savitzkygolay': ['filters/1DSavitzkyGolayFilters/*.dat',
                                      'filters/2DSavitzkyGolayFilters/*.dat',
                                      'filters/3DSavitzkyGolayFilters/*.dat',]}
)
