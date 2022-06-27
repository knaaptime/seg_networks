import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="seg_networks",

    description="measuring the effect of pedestrian network structure on segregation measurement",

    author="ek",

    packages=find_packages(exclude=['data', 'figures', 'output', 'notebooks']),

    long_description=read('README.md'),
)
