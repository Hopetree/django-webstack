# -*- coding:utf-8 -*-
# Author: https://github.com/Hopetree
# Date: 2023/7/24
from setuptools import find_packages, setup

VERSION = '1.2.0'

with open('README.md', 'r', encoding='utf-8') as fp:
    long_description = fp.read()

setup(
    name='django-webstack',
    version=VERSION,
    author='Hopetree',
    author_email='zlwork2014@163.com',
    description='webstack of Django',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/Hopetree/django-webstack',
    keywords='django webstack navigation',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Django >= 2.2',
        'Pillow >= 9.3.0',
        'django-imagekit >= 4.0.2'
    ],
    python_requires='>=3.5',
    classifiers=[
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 1.10',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 2.1',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.0',
    ],
)
