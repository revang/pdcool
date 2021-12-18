#!/usr/bin/env python
# -*- coding:utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='kdcool',
    version='0.0.1',
    keywords='kdcool',
    description='a library for revang developer',
    license='MIT License',
    url='https://github.com/revang/kdcool',
    author='revang',
    author_email='revang.alternative@foxmail.com',
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    install_requires=[
        # 'request>=2.26.0',
    ],
)
