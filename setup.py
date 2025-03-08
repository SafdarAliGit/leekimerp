from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in leekimerp/__init__.py
from leekimerp import __version__ as version

setup(
	name="leekimerp",
	version=version,
	description="A",
	author="A",
	author_email="A",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
