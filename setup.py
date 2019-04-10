from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='array-min',
    version='0.9.2',
    packages=['array-min'],
    url='https://github.com/Rohail1/array-min/',
    license='MIT',
    author='Rohail Najam',
    author_email='rohaiil_najam@hotmail.com',
    description='It is used to find minimum of a monotonically diverging arrays.',
    long_description=long_description,
    long_description_content_type='text/markdown',
)
