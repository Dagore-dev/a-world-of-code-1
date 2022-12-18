def max_product(*numbers: int) -> int:
    """
    :param numbers: List of at least two numbers
    :return: Maximum product between two numbers in the list

    >>> max_product(1, 5, -2, -4)
    8

    >>> max_product(2)
    Traceback (most recent call last):
    ...
    Exception: Expected at least two numbers
    """
    length = len(numbers)

    if length < 2:
        raise Exception('Expected at least two numbers')

    smallest_numbers_product = numbers[0] * numbers[1]
    largest_numbers_product = numbers[length - 2] * numbers[length - 1]

    if smallest_numbers_product > largest_numbers_product:
        return smallest_numbers_product

    return largest_numbers_product


if __name__ == '__main__':
    import doctest

    doctest.testmod()
