"""
Setup
"""
import os

from setuptools import setup, find_packages

def package_files(directory):
    """package_files

    recursive method which will lets you set the
    package_data parameter in the setup call.
    """
    paths = []
    for (path, _, filenames) in os.walk(directory):
        for filename in filenames:
            paths.append(os.path.join('..', path, filename))
    return paths

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="time_series_generator",
    version="0.0.2",
    author="Daniel Kaminski de Souza",
    author_email="daniel@kryptonunite.com",
    description="Time Series Generator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=find_packages(exclude=("tests",)),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
    ],
    extras_require={
        'dev': [
            'wheel',
            'pylint',
            'autopep8',
            'bumpversion',
            'twine',
        ],
        'test': [
            'pytest>=4.6',
            'pytest-cov',
            'tensorflow'
        ]
    }
)
