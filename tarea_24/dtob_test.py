"""
Test for the dectimal to binary converter.
"""
import unittest

import pytest

from dtob import itob_recurse, itob_iterative


TEST_DATA = [(8,"1000"), (11,"1011"), (5, "101"),
             (25, "11001"), (101, "1100101")]


@pytest.mark.parametrize(
    "test_input,expected",
    TEST_DATA
)
def test_output_integer_recurse(test_input, expected):
    output = itob_recurse(test_input)
    assert output == expected

@pytest.mark.parametrize(
    "test_input,expected",
    TEST_DATA
)
def test_output_integer_iteration(test_input, expected):
    output = itob_iterative(test_input)
    assert output == expected
