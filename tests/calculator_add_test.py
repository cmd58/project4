"""Testing the Calculator"""
from calculator import Calculator


def test_calculator_add_method():
    """Testing the Calculator"""
    calculator = Calculator()
    assert calculator.add(1) == 1

