"""
Module containing test cases for the Calculator class
"""
import pytest

from calculator import Calculator

def test_calculator_addition():
    """
    Asserts addition works correctly.
    """
    assert Calculator(1, 2).sum() == 3

def test_calculator_subtraction():
    """
    Asserts subtraction works correctly.
    """
    assert Calculator(1, 2).subtract() == -1

def test_calculator_multiplication():
    """
    Asserts multiplication works correctly.
    """
    assert Calculator(3, 4).multiply() == 12

def test_calculator_division():
    """
    Asserts division works correctly.
    """
    assert Calculator(3, 4).divide() == 0.75

def test_calculator_division_by_zero_throws_exception():
    """
    Asserts that division by zero throws exception.
    """
    with pytest.raises(ZeroDivisionError):
        Calculator(3, 0).divide()
