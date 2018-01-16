#!/usr/bin/python


def Mutiplesof3and5(number):
    """Finds the sum of all the multiples of 3 or 5 below a given number.

    Args:
        number - Sets the range of natural numbers to search, exclusive.
    Returns:
        Integer sum of the all multiples of 3 or 5 below the stated number.
    """
    summation = int(0)
    for n in range(1, number, 1):
        if n % 3 == 0 or n % 5 == 0:
            summation += n
    return summation


if __name__ == '__main__':
    print(Mutiplesof3and5(1000))
