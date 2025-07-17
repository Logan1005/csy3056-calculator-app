
# File: calculator.py
# Purpose: Simple calculator logic
# Dependencies: None
# Description: This module provides basic arithmetic operations.

def add(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Inputs must be numbers.")
    return a + b

def subtract(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Inputs must be numbers.")
    return a - b

def multiply(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Inputs must be numbers.")
    return a * b

def divide(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Inputs must be numbers.")
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

