#!/usr/bin/env python


try:
    from setuptools import setup, Extension
    setup, Extension
except ImportError:
    from distutils.core import setup
    from distutils.extension import Extension
    setup, Extension

import os
import sys
sys.path.append(os.path.dirname(__file__))

import daft


setup(
    name="daft",
    version=daft.__version__,
    author="David W. Hogg & Daniel Foreman-Mackey",
    author_email="danfm@nyu.edu",
    packages=["daft"],
    description="PGM rendering at its finest.",
    long_description=open("README.rst").read(),
    install_requires=[
                        "numpy",
                        "matplotlib"
                     ],
)