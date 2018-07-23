#!/usr/bin/env python
from setuptools import find_packages, setup

setup(
    name='zeronet',
    version='0.6.2',
    author='HelloZeroNet',
    author_email='',
    description='Decentralized websites using BitCoin crypto and BitTorrent network',
    url='https://github.com/HelloZeroNet/ZeroNet',
    install_requires=[
        'gevent>=1.1.0',
        'msgpack>=0.4.4',
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src", exclude=('src/Test', )),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS :: MacOS X',
    ],
    entry_points={
        'console_scripts': [
            'zeronet = zeronet.__main__:main',
        ],
    }
)
