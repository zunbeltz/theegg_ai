"""
Test for the dectimal to binary converter.
"""
import unittest

import pytest

from dtob import itob_recurse, itob_iterative, ftob, dtob


INTEGER_DATA = [(8,"1000"), (11,"1011"), (5, "101"),
             (25, "11001"), (101, "1100101")]


@pytest.mark.parametrize(
    "test_input,expected",
    INTEGER_DATA
)
def test_output_integer_recurse(test_input, expected):
    output = itob_recurse(test_input)
    assert output == expected

@pytest.mark.parametrize(
    "test_input,expected",
    INTEGER_DATA
)
def test_output_integer_iteration(test_input, expected):
    output = itob_iterative(test_input)
    assert output == expected

FRACTION_DATA = [(0.47, 3, "011"), (0.375, 3, "011"),
                 (0.8125, 4, "1101")]
@pytest.mark.parametrize(
    "test_input,test_precision,expected",
    FRACTION_DATA
    )
def test_output_fraction(test_input, test_precision, expected):
    output = ftob(test_input, test_precision)
    assert output == expected

TEST_DATA = [(54.6875, 4, "r", "110110.1011")]

@pytest.mark.parametrize(
    "test_input,test_precision,test_algo,expected",
    TEST_DATA
    )
def test_output_decimal(test_input, test_precision, test_algo, expected):
    output = dtob(test_input, test_precision)
    assert output == expected
