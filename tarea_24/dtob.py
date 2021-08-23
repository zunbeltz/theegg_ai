#!/usr/bin/python3
"""Calcuate the binary expansion of a decimal number.

   Fist the decimal part is separated in the integer and in the fraction.
   The integer parrt is calculated using the itob_* functions.
   The fraction part is calcualted using the ftob function. For this fucntion
   we need a integer number $k$, which gives the precision of the representation.
   Them, we join both binary strings.

   This module containcs a recurseve and a iterative function.
"""

import math

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

def ftob(fraction: float, k: int) -> str:
    """
    Covert fractional part to binary with precision k.
    Args:
        fraction (float): fractional part
        k (int): precision (>0)
    Returns:
        str: binary representation
    """
    bit_string = ""
    while k > 0:
        fraction = fraction*2
        fraction, integer = math.modf(fraction)
        bit_string = bit_string + str(int(integer))
        k = k-1
    return bit_string

def dtob(decimal: float, precision: int = 8, algo: str = "i") -> str:
    """
    Cnvert decimal number to binary representation with precision
    Args:
        decimal (float): Decimal number to be converted
        precision (int): (default: 8) precision.
        algo (str): (default "i"): Algortihm (recursive o iterative
        to compute integer part.
    Returns:
        str:
    """
    fraction, integer = math.modf(decimal)
    integer = int(integer)
    fraction_binary = ftob(fraction, precision)
    if algo == "r":
        integer_binary = itob_recurse(integer)
    elif algo == "i":
        integer_binary = itob_iterative(integer)
    else:
        raise ValueError("Algorithm type error")

    return f"{integer_binary}.{fraction_binary}"


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Binary expansion of decimal number.")
    parser.add_argument('decimal', type=float, help='Decimal number to be converted')
    parser.add_argument('precision', type=int, help='Precision for fractional part')
    parser.add_argument('--type', type=str, help='Algorithm type: recursive (r) or iterative (i) ',
                        default="i")
    args = parser.parse_args()
    number_to_convert = args.decimal
    algo = args.type
    precision = args.precision
    print(dtob(number_to_convert, precision, algo))
