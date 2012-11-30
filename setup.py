#!/usr/bin/env python

from distutils.core import setup

setup(name='python-jtl',
      version='0.1.0',
      description='Python module for parsing JMeter test results',
      long_description=open('README.txt').read(),
      author='Victor Klepikovskiy',
      author_email='vklepikovskiy@gmail.com',
      url='http://code.google.com/p/python-jtl/',
      license='LICENSE.txt',
      packages=['tests'],
      py_modules=['jtl'],
     )
