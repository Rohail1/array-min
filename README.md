# Array-min

Package use to find the smallest element of a monotonically diverging array.

## Requirements
It is built on python 3.6 It uses type hinting as well.

## How to use

I have uploaded it on testpypi. It is very common that they remove modules and accounts after sometime since 
it only serves as a testing ground.

```bash
pip install -i https://test.pypi.org/simple/ array-min
```

## How to run

```python

from array_min.minimum import find_minimum

find_minimum([85,53,23,22,1,5,7,9,25]) 


```

## Tests

There are two types of tests in this module. 

1) Doctests
2) Unittests

### Doctests
To run the Doctests simply import the module if there is no output it means module was load successfully without any 
errors and all the doctests ran perfectly.

```bash
python3 array_min/minimum.py 
``` 

### Unittests

To run the unit test you must install nose.

```bash
pip install nose
nosetests
```

You can also run it using the setup.py

```bash
python3 setup.py test
```