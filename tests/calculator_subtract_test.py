"""Testing the Calculator"""
from calculator import Calculator


def test_calculator_subtract_method():
    """Testing the Calculator Subtract"""
    calculator = Calculator()
    assert calculator.subtract(1) == -1