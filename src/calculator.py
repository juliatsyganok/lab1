from src.constants import ERROR_MESSAGES
def calculate(tokens: list[float | str]) -> float:
    """
    Вычисляет значение выражения из токенов с учетом приоритета операций.
    
    Args:
        tokens: Список токенов 
        
    Returns:
        Результат вычисления выражения
        
    Raises:
        ZeroDivisionError: При делении на ноль
        ValueError: неправильное выражение
    """

    if len(tokens) == 0:
        raise ValueError("Неверное выражение")
    if len(tokens) % 2 == 0:
        raise ValueError("Неверное выражение")

    i = 0
    while i < len(tokens):
        if tokens[i] == '*' or tokens[i] == '/':
            a = tokens[i-1]
            b = tokens[i+1]
            if tokens[i] == '*':
                result = a * b
            else:
                if b == 0:
                    raise ZeroDivisionError("Деление на ноль")
                result = a / b
            tokens[i-1:i+2] = [result]
            i = 0
        else:
            i += 1
    i = 0
    while i < len(tokens):
        if tokens[i] == '-' or tokens[i] == '+':
            a = tokens[i-1]
            b = tokens[i+1]
            if tokens[i] == '+':
                result = a + b
            else:
                result = a - b
            tokens[i-1:i+2] = [result]
            i = 0
        else:
            i += 1
    return tokens[0]
