from setuptools import setup, find_packages
from auth_service import __version__

setup(
    name='currint',
    version=__version__,
    description='Integer-based, fixed precision currency calculation',
    packages=find_packages(),
)

