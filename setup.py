#!/usr/bin/env python

from setuptools import setup


def reqs_from_file(filename):
    with open(filename) as f:
        lineiter = (line.rstrip() for line in f if not line.startswith("#"))
        return list(filter(None, lineiter))


setup(
    name='rewrite-cassandra-yaml',
    version='0.1.1',
    description='Script to rewrite a cassandra yaml file to allow remote access',
    author='Hugh Brown',
    author_email='hughdbrown@yahoo.com',

    # Required packages
    install_requires=reqs_from_file('requirements.txt'),
    # tests_require=reqs_from_file('test-requirements.txt'),

    # Main packages
    packages=[
        'src',
    ],

    zip_safe=False,

    scripts=[
        'bin/rewrite-cassandra-yaml',
    ],
    entry_points={
        'console_scripts': [
            'rewrite-cassandra-yaml = src.rewrite_cassandra_yaml:main',
        ],
    },
)
