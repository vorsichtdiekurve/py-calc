import pytest

from calculator import Calculator

def test_calculator_addition():
    assert Calculator(1, 2).sum() == 3

def test_calculator_subtraction():
    assert Calculator(1, 2).subtract() == -1

def test_calculator_multiplication():
    assert Calculator(3, 4).multiply() == 12

def test_calculator_division():
    assert Calculator(3, 4).divide() == 0.75

def test_calculator_division_by_zero_throws_exception():
    with pytest.raises(ZeroDivisionError):
        Calculator(3, 0).divide()