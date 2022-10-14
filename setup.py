#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
		required = f.read().splitlines()

setup(
	author="LaPiova",
	author_email='schrodinghauer@gmail.com',
	install_requires=required,
	classifiers=[
		'License :: OSI Approved :: MIT License',
		'Programming Language :: Python :: 3.7',
	],
	description="Says hello",
	license="MIT license",
	include_package_data=True,
	name='PyRegexGen',
	version='0.1',
	zip_safe=False,
)