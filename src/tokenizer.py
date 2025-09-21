from src.constants import *
def get_tokens(case: str) -> list[float | str]:
    """  
    Разбивает входное выражение на токены, причем унарный знак является частью токена  

    Args:
        case: входная строка с выражением  
    Returns:
        tokens: список токенов  
    """  
    tokens = []
    i = 0
    
    while i < len(case) and case[i].isspace():
        i += 1
        
    while i < len(case):
        if case[i].isspace():
            i += 1
            
        elif case[i] in SECOND_PRI:
            if i == 0 or (tokens and tokens[-1] in OPERATORS):
                sign = case[i]
                i += 1
                while i < len(case) and case[i].isspace():
                    i += 1
                start = i
                while i < len(case) and (case[i].isdigit() or case[i] == '.'):
                    i += 1
                if i > start:
                    number_str = sign + case[start:i]
                    tokens.append(float(number_str))
                else:
                    raise ValueError("неправильный ввод")
            else:
                tokens.append(case[i])
                i += 1
                
        elif case[i] in FIRST_PRI:
            tokens.append(case[i])
            i += 1
            
        elif case[i].isdigit() or case[i] == '.':
            start = i
            while i < len(case) and (case[i].isdigit() or case[i] == '.'):
                i += 1
            tokens.append(float(case[start:i]))
            
        else:
            raise ValueError(f"Неизвестный символ: '{case[i]}'")
            
    return tokens
