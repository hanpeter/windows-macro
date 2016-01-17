from __future__ import absolute_import
from setuptools import setup, find_packages

VERSION = '0.0.1'

REPO_URL = 'https://github.com/hanpeter/windows-macro'

DOWNLOAD_URL = '{repo_url}/tarball/release/{version}'.format(repo_url=REPO_URL, version=VERSION)


setup(
    name='windows_macro',
    version=VERSION,
    author='Peter Han',
    description='Utility library to run macro files',
    url=REPO_URL,
    download_url=DOWNLOAD_URL,
    packages=find_packages(),
    install_requires=[
        'pypiwin32'
    ],
    entry_points={
        'console_scripts': [
            'windows-macro = windows_macro.cli:main'
        ]
    },
)
