# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages


def read(*paths):
    with open(os.path.join(*paths), 'r') as f:
        return f.read()

setup(
    name='twitterbot_utils',
    version='0.0.01',
    # author='Oleg Strizhechenko',
    author='MuradTcen',
    # author_email='oleg.strizhechenko@gmail.com',
    author_email='muradtcen@gmail.com',
    license='GPL',
    url='https://github.com/muradtcen/twibot_utils',
    keywords='twitter api bot',
    description='wrapper around the Tweepy',
    long_description=(read('README.rst')),
    packages=find_packages(exclude=['tests*']),
    install_requires=['tweepy', 'requests',
                      'requests-oauthlib', 'pymorphy2', 'dictator'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Operating System :: MacOS',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development',
        'Topic :: Utilities',
    ],
)
