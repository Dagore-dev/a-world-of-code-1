def full_hour_to_seconds(full_hour: str) -> int:
    """
    Takes an hour as input and convert it to seconds
    :param: full_hour: Full hour with "00:00:00" (hh:mm:ss) pattern
    :return: The input hour converted to seconds

    >>> full_hour_to_seconds('01:30:30')
    5430
    >>> full_hour_to_seconds('00:00:00')
    0
    >>> full_hour_to_seconds('some_random_str')
    Traceback (most recent call last):
     ...
    Exception: Expected format: "00:00:00"
    """
    import re

    if re.match("^\\d\\d:\\d\\d:\\d\\d$", full_hour) is None:
        raise Exception('Expected format: "00:00:00"')

    hours, minutes, seconds = map(lambda item: int(item), full_hour.split(':'))
    return hours * 3600 + minutes * 60 + seconds


def seconds_to_full_hour(seconds: int) -> str:
    """
    Takes a certain number of seconds as input and return a fortatted hour (hh:mm:ss)
    :param seconds: The number of seconds that represents a concrete hour
    :return: The corresponding hour with format "00:00:00" (hh:mm:ss)

    >>> seconds_to_full_hour(0)
    '00:00:00'
    >>> seconds_to_full_hour(5430)
    '01:30:30'
    >>> seconds_to_full_hour(-10)
    Traceback (most recent call last):
    ...
    Exception: Expected a positive integer as value for "seconds" parameter
    """
    if seconds < 0:
        raise Exception('Expected a positive integer as value for "seconds" parameter')

    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds_remaining = (seconds % 3600) % 60

    return f'{str(hours).rjust(2, "0")}:{str(minutes).rjust(2, "0")}:{str(seconds_remaining).rjust(2, "0")}'


def sum_hours(hour_1: str, hour_2: str) -> str:
    """
    Given two hours return a string with its sum
    :param hour_1: Hour in format "00:00:00" (hh:mm:ss)
    :param hour_2: Hour in format "00:00:00" (hh:mm:ss)
    :return: Sum of hour_1 and hour_2 in the same format

    >>> sum_hours('01:01:01', '10:10:10')
    '11:11:11'
    >>> sum_hours('abc', '01:01:01')
    Traceback (most recent call last):
     ...
    Exception: Expected format: "00:00:00"
    """
    seconds = full_hour_to_seconds(hour_1) + full_hour_to_seconds(hour_2)

    return seconds_to_full_hour(seconds)


def get_hour(prompt: str = '') -> str:
    """
    Ask user for hours, minutes and seconds and return a string representing the hour.
    :return: An hour in format "00:00:00" (hh:mm:ss)
    """
    print(prompt)

    hours = int(input('Hour: '))
    if hours < 0:
        raise Exception('Expected a positive integer')
    minutes = int(input('Minutes: '))
    if minutes < 0:
        raise Exception('Expected a positive integer')
    seconds = int(input('Seconds: '))
    if seconds < 0:
        raise Exception('Expected a positive integer')

    total_seconds = hours * 3600 + minutes * 60 + seconds

    return seconds_to_full_hour(total_seconds)


if __name__ == '__main__':
    import doctest

    doctest.testmod()
