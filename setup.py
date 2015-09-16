#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

import setuptools

setuptools.setup(
    name="gtjdbsync",
    version="0.1.0",
    url="https://github.com/ssheftel/gathernow-database-sync-service.git",

    author="Sam Getz Sheftel",
    author_email="sngsheftel@gmail.com",

    description="service for synchronizing gtj's database with gathernow's db",
    long_description=open('README.md').read(),

    packages=setuptools.find_packages(),

    install_requires=[],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
)
