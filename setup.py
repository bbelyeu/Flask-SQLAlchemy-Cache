#!/usr/bin/env python

from setuptools import setup

setup(
    name='Flask-SQLAlchemy-Cache',
    version='0.1',
    description='CachingQuery implementation to Flask using Flask-SQLAlchemy and Flask-Cache',
    author='Iuri de Silvio',
    author_email='iurisilvio@gmail.com',
    url='http://www.github.com/iurisilvio/Flask-SQLAlchemy-Cache',
    license='MIT',
    platforms='any',
    package=['flask_cache_sqlalchemy'],
    install_requires=[
        'Flask',
        'Flask-Cache',
        'Flask-SQLAlchemy',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)