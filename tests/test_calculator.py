import pytest
from src.calculator import calculate


def test_addition() -> None:
    """Тестирование сложения"""
    tokens = [2.0, '+', 3.0]
    result = calculate(tokens)
    assert result == 5.0


def test_subtraction() -> None:
    """Тестирование вычитания"""
    tokens = [5.0, '-', 2.0]
    result = calculate(tokens)
    assert result == 3.0


def test_multiplication() -> None:
    """Тестирование умножения"""
    tokens = [3.0, '*', 4.0]
    result = calculate(tokens)
    assert result == 12.0


def test_division() -> None:
    """Тестирование деления"""
    tokens = [10.0, '/', 2.0]
    result = calculate(tokens)
    assert result == 5.0


def test_division_by_zero() -> None:
    """Тестирование деления на ноль"""
    tokens = [5.0, '/', 0.0]
    with pytest.raises(ZeroDivisionError, match="Деление на ноль"):
        calculate(tokens)


def test_operator_priority() -> None:
    """Тестирование приоритета операций"""
    tokens = [2.0, '+', 3.0, '*', 4.0] 
    result = calculate(tokens)
    assert result == 14.0


def test_complex_expression() -> None:
    """Тестирование сложного выражения"""
    tokens = [10.0, '-', 2.0, '*', 3.0, '+', 4.0]
    result = calculate(tokens)
    assert result == 8.0
