#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
from pkgutil import walk_packages

import cumulusci

def find_packages(path='.', prefix=""):
    yield prefix
    prefix = prefix + "."
    for _, name, ispkg in walk_packages(path, prefix):
        if ispkg:
            yield name

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='cumulusci',
    version='2.0.0-alpha1',
    description="Build and release tools for SSalesforce developers",
    long_description=readme + '\n\n' + history,
    author="Jason Lantz",
    author_email='jlantz@salesforce.com',
    url='https://github.com/SalesforceFoundation/CumulusCI',
    packages = list(find_packages(cumulusci.__path__, cumulusci.__name__)),
    package_dir={'cumulusci':
                 'cumulusci'},
    entry_points={
        'console_scripts': [
            'cumulusci=cumulusci.cli.cli:cli',
            'cumulusci2=cumulusci.newcli.cli:cli'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="BSD license",
    zip_safe=False,
    keywords='cumulusci',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
