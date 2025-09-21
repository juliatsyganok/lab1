from src.tokenizer import get_tokens
from src.calculator import calculate

def main() -> None:
    """
    Главная функция - точка входа в калькулятор.

    Пользовательский ввод обрабатывается до команды exit

    Returns:
        None: не возвращает значение, только счиатет результат выражения
    """
    while True:
        print("Начало работы. Введите выражение или 'exit' для выхода")
        case = input()

        if case.lower() == 'exit':
            break

        if not case:
            continue

        try:
            tokens = get_tokens(case)
            result = calculate(tokens)
            print(f"Результат: {result}")
        except Exception as e:
            print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()
