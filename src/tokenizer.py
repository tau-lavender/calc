from string import digits
from itertools import product
from src.constants import *
from src.token import *


class InputException(Exception):
    pass


def get_tokens(expr: str) -> list:
    """
    Токенизирует выражение в строке
    :expr: Строка пользовательского ввода с выражением которое нужно обработать
    :return:  
    """
    tokens = []
    curent_number = ""
    i = 0

    if "," in expr:
        raise InputException("Для записи рациональных чисел нужно использовать точку: '.'")
    expr = expr.strip()
    while "  " in expr:
        expr = expr.replace("  ", " ")
    incorrect_combos = [" ".join(el) for el in product(digits + ".", 2)]
    for combo in incorrect_combos:
        if combo in expr:
            raise InputException(f"Лишний пробел между числами")
    expr = expr.replace(" ", "")

    while i < len(expr):
        curent_symbol = expr[i]
        if curent_symbol.isdigit() or curent_symbol == '.':
            curent_number = curent_symbol

            while expr[i + 1].isdigit() or expr[i + 1] == '.':
                i += 1
                curent_number += expr[i]

            if curent_number.count(".") > 1:
                raise InputException(f"В числе несколько точек")
            elif curent_number.count(".") == 1:
                tokens.append(NumberToken(value=float(curent_number)))
            else:
                tokens.append(NumberToken(value=int(curent_number)))
            curent_number = ""
            i += 1
            pass

        if i < len(expr) - 1:
            if expr[i: i + 2] in OPERATIONS.keys():
                tokens.append(OPERATIONS[expr[i:i + 2]]())
                i += 2
                pass

        if expr[i] in OPERATIONS.keys():
            tokens.append(OPERATIONS[expr[i]]())
            i += 1
            pass

        raise InputException("Выражение содержит лишние символы")
    
    return tokens