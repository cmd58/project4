"""Testing the Calculator"""
from calculator import Calculator


def test_calculator_add_method():
    """Testing the Calculator Add"""
    calculator = Calculator()
    assert calculator.add(1) == 1

