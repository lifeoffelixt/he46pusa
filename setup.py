from distutils.core import setup
from setuptools import find_packages
setup(name='he46pusa',
 version='0.1',
 author='Felix Bueppelmann',
 author_email='felix.bueppelmann@fau.de',
 packages=find_packages(),
 install_requires=['numpy', 'Pillow', 'ipywidgets'])
