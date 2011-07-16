#!/usr/bin/env python

from distutils.core import setup

version = '1.5'

setup(
    name = 'colorbash',
    packages = ['colorbash'],
    version = version,
    url = 'https://github.com/horejsek/colorbash',
    description = 'Python library for color the output of program in Bash.',
    author = 'Michal Horejsek',
    author_email = 'horejsekmichal@gmail.com',
    license = 'GNU General Public License (GPL)',
    classifiers = [
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing :: Filters',
        'Topic :: Terminals',
    ],
)
