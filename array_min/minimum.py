def minimum(array):
    """
    Returns a string, which will be padded on the left with characters if necessary. If the input string is longer
    than the specified length, it will be returned unchanged.

    >>> minimum([2,4,5])
    2

    >>> minimum([3,57,1])
    1

    >>> minimum([53,5,13,56,100])
    5

    >>> minimum([79,56,245,22,46])
    22


    :param array:
    :rtype int:
    """

    return min(array)
