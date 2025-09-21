import pytest
from src.tokenizer import get_tokens

def test_basic_tokens() -> None:
    """Тестирование обыччной токенизации"""
    case = "2 + 3 * 4"
    tokens = get_tokens(case)
    assert tokens == [2.0, '+', 3.0, '*', 4.0]


def test_unary_minus() -> None:
    """Тестирование унарного минуса"""
    case = "-5 + 3"
    tokens = get_tokens(case)
    assert tokens == [-5.0, '+', 3.0]


def test_unary_plus() -> None:
    """Тестирование унарного плюса"""
    case = "+5 - 3"
    tokens = get_tokens(case)
    assert tokens == [5.0, '-', 3.0]


def test_decimal_numbers() -> None:
    """Тестирование десятичных чисел"""
    case = "2.5 * 3.14"
    tokens = get_tokens(case)
    assert tokens == [2.5, '*', 3.14]


def test_multiple_operators() -> None:
    """Тестирование нескольких знаков подряд"""
    case = "2 + -3 * +4"  # 2 + (-3) * (+4)
    tokens = get_tokens(case)
    assert tokens == [2.0, '+', -3.0, '*', 4.0]


def test_invalid_character() -> None:
    """Тестирование недопустимого символа"""
    case = "2 + a * 3"
    with pytest.raises(ValueError, match="Неизвестный символ"):
        get_tokens(case)


def test_empty_case() -> None:
    """Тестирование пустого выражения"""
    case = ""
    tokens = get_tokens(case)
    assert tokens == []
