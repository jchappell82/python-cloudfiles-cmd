#!/usr/bin/env python
from distutils.core import setup
from cf import version
from setuptools import find_packages

setup(
    name='cf',
    version=version,
    author='Jon Chappell',
    author_email='jon@jchome.us',
    description='Provides an interface to Rackspace Cloud Files.  Modified from https://github.com/sandeep-sidhu/python-cloudfiles-cmd',
    license='MIT',
    url='https://github.com/jchappell82/python-cloudfiles-cmd',

    install_requires='python-cloudfiles',
    provides=[
        'cf',
    ],

    packages=find_packages(),
    scripts=[
        'scripts/cf_list_containers',
        'scripts/cf_upload_file',
        'scripts/cf_download_file',
        'scripts/cf_list_files',
    ],
)