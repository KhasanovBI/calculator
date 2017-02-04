from distutils.core import setup

from setuptools import find_packages

setup(
    name='Calculator',
    version='0.0.1',
    packages=find_packages(exclude=('tests',)),
    url='https://github.com/KhasanovBI/calculator',
    license='BSD',
    author='bkhasanov',
    author_email='afti@yandex.ru',
    description='Super puper calculator'
)
