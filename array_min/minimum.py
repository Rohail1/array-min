import doctest


def find_minimum(array: list, initial_index: int = None, last_index: int = None) -> int:
    """
    Returns the smallest element of a monotonically decreasing and monotonically increasing array

    >>> find_minimum([9,7,6,2,3,3,4,5,7])
    2

    >>> find_minimum([100,99,98,97,16,17,18,19,22])
    16

    >>> find_minimum([55,54,53,53,51,60,62,63])
    51

    >>> find_minimum([19,18,15,14,16,17,18,20])
    14

    :param array:
    :param initial_index:
    :param last_index:
    :rtype int:
    """
    distinct_list = array
    # Check if list do not contains duplicates If so remove them.
    if initial_index is None or last_index is None:
        distinct_list = list(dict.fromkeys(array))
        initial_index = 0
        last_index = len(distinct_list) - 1
    # check if list contain only one item
    if len(distinct_list) == 1:
        return distinct_list[initial_index]

    # check if there are two elements in the list

    if len(distinct_list) == 2:

        # Since list has two elements
        # if first element is smaller than the second return it.
        # else return the second element

        if distinct_list[initial_index] < distinct_list[last_index]:
            return distinct_list[initial_index]
        else:
            return distinct_list[last_index]
    else:

        # Since list has more than 2 elements we will find a midpoint.

        mid_point = (initial_index + last_index)//2

        # If mid_point it smaller than both of its neighbours it means its the where both series diverge
        # it is the smallest element of entire list.

        if distinct_list[mid_point] < distinct_list[initial_index] and \
                distinct_list[mid_point] < distinct_list[last_index]:
            return distinct_list[mid_point]

        # If mid_point is small than previous element but greater than next element then smallest element lies
        # in the right side of the list
        # else if mid_point is smaller than the next element but greater than the previous element so the
        # smallest element lies in the right side of the list

        if distinct_list[mid_point - 1] > distinct_list[mid_point] > distinct_list[mid_point + 1]:
            return find_minimum(distinct_list, mid_point + 1, last_index)
        else:
            return find_minimum(distinct_list, initial_index, mid_point - 1)


if __name__ == "__main__":
    doctest.testmod()
