
# File: test_calculator.py
# Purpose: Unit tests for calculator module
# Dependencies: pytest, calculator module
# Description: This script tests the arithmetic operations defined in the calculator module

from calculator import add, subtract, multiply, divide
import pytest

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(5, 3) == 2

def test_multiply():
    assert multiply(2, 3) == 6

def test_divide():
    assert divide(6, 3) == 2

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(5, 0)

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(5, 0)

# Advanced tests

def test_add_negative():
    assert add(-2, -3) == -5

def test_subtract_negative():
    assert subtract(-5, 3) == -8

def test_multiply_by_zero():
    assert multiply(0, 1000) == 0

def test_divide_floats():
    assert abs(divide(5.5, 2) - 2.75) < 1e-9  # float precision

@pytest.mark.parametrize("a,b,expected", [
    (1e10, 1e10, 2e10),
    (1e-10, 1e-10, 2e-10),
])
def test_add_large_small_numbers(a, b, expected):
    assert add(a, b) == expected

def test_invalid_types():
    with pytest.raises(TypeError):
        add("a", 1)
    with pytest.raises(TypeError):
        subtract(None, 1)
    with pytest.raises(TypeError):
        multiply(3, "b")
    with pytest.raises(TypeError):
        divide(5, "0")