#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
		required = f.read().splitlines()

setup(
	name='PyRegexGen',
	version='0.1',
	author="LaPiova",
	author_email='schrodinghauer@gmail.com',
	install_requires=required,
	classifiers=[
		'License :: OSI Approved :: MIT License',
		'Programming Language :: Python :: 3.7',
	],
	packages=find_packages(),
	description="A trie generator and search tool.",
	python_requires=">=3.6",
	license="MIT license",
	zip_safe=False,
)