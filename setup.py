from setuptools import setup, find_packages

setup(
	name='PyRegexGen',
	version='0.1',
	author="LaPiova",
	author_email='schrodinghauer@gmail.com',
	classifiers=[
		'License :: OSI Approved :: MIT License',
		'Programming Language :: Python :: 3.7',
	],
	packages=find_packages(),
	description="A trie generator and search tool.",
	python_requires=">=3.6",
	include_package_data = True,
	license="MIT license",
	zip_safe=False,
)