# -*- coding: utf-8 -*-
#!/usr/bin/env python

from setuptools import setup, find_packages

version = "1.0.0"
readme = open('README.rst').read()

setup(
    name='django-genesis',
    version=version,
    description='Management command that calls every INSTALLED_APPS {app_name}_bootstrap management command',
    long_description=readme,
    author='Charlie Quinn',
    author_email='charlesquinn1984@gmail.com',
    url='https://github.com/TwigWorld/django-genesis',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'django>=1.6',
    ],
    zip_safe=False,
    keywords='django-genesis',
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
    ],
)
