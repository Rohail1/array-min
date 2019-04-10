from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='array_min',
    version='1.0.0',
    packages=['array_min'],
    url='https://github.com/Rohail1/array-min/',
    license='MIT',
    author='Rohail Najam',
    author_email='rohaiil_najam@hotmail.com',
    description='It is used to find minimum of a monotonically diverging arrays.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    test_suite='nose.collector',
    tests_require=['nose'],
)
