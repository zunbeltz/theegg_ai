#!/usr/bin/python3
"""Calcuate the binary expansion of a decimal number.

   This module containcs a recurseve and a iterative function.
"""


def itob_recurse(integer: int) -> str:
    """
    Convert integer number to a binary string representation.

    This funcition recursevely calculated the division by 2 of the mumber.
    This remainder will be the lat bit value. We keep calculating
    recursevely with the quotient.
    Args:
        integer (int): Number to be converted.
    Returns:
        str: binary representation of integer
    """
    if integer == 0:
        return "0"
    if integer == 1:
        return "1"
    quotient, remainder = divmod(integer, 2)
    return itob_recurse(quotient) + str(remainder)


def itob_iterative(integer: int) -> str:
    """
    Convert integer number to a binary string representation.

    This funcition recursevely calculated the division by 2 of the mumber.
    This remainder will be the lat bit value. We keep calculating
    recursevely with the quotient.
    Args:
        integer (int): Number to be converted.
    Returns:
        str: binary representation of integer
    """
    bit_string = ""
    while integer > 1:
        quotient, remainder = divmod(integer, 2)
        bit_string = str(remainder)+ bit_string
        integer = quotient
    if integer == 1:
        bit_string = "1" + bit_string
    if integer == 0:
        bit_string = "0" + bit_string
    return bit_string



if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Binary expansion of decimal number.")
    parser.add_argument('decimal', type=int, help='Decimal number to be converted')
    parser.add_argument('--type', type=str, help='Algorithm type: recursive (r) or iterative (i) ',
                        default="r")
    args = parser.parse_args()
    number_to_convert = args.decimal
    if args.type == "r":
        function = dtob_recurse
    elif args.type == "i":
        function = dtob_iterative
    else:
        raise ValueError("Algorithm type error")
    print(function(number_to_convert))
