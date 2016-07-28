#!/usr/bin/python

from distutils.core import setup

setup(
	# Basic package information.
	name = 'hipchat',
	version = '0.0.0',
	packages = ['hipchat'],
	include_package_data = True,
	install_requires = ['httplib2', 'simplejson'],
	url = 'https://github.com/alexcchan/hipchat/tree/master',
	keywords = 'hipchat api',
	description = 'HipChat API v2 Wrapper for Python',
	classifiers = [
		'Development Status :: 4 - Beta',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: MIT License',
		'Topic :: Software Development :: Libraries :: Python Modules',
		'Topic :: Internet'
	],
)


