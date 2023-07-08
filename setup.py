from setuptools import find_packages, setup

setup(
    name='dummy_model',
    version='0.1',
    description='My module',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
)
