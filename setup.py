# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='module_name',
    version='0.1',
    description='yada yada yada',
    long_description=readme,
    author='Francisco Ribeiro',
    author_email='francisco@ironik.org',
    url='https://github.com/blackthorne/libcall',
    license=license,
    packages=find_packages(exclude=('tests', 'docs', 'logs'))
)