from string import digits
from typing import Any
from itertools import product
from src.constants import OPERATIONS
from src.token import NumberToken, BracketToken, BracketTypes
from src.token import OperationTypes, UnaryMinusToken


class InputException(Exception):
    pass


def get_tokens(expr: str) -> list[Any]:
    """
    Токенизация выражения в строке.

    :expr: Строка пользовательского ввода с выражением которое нужно обработать
    :return: Список токенов
    """

    tokens: list[Any] = []
    curent_number = ""
    i = 0

    if "," in expr:
        raise InputException(
            "Для записи рациональных чисел нужно использовать точку: '.'"
        )
    expr = expr.strip()
    while "  " in expr:
        expr = expr.replace("  ", " ")
    incorrect_combos = [" ".join(el) for el in product(digits + ".", repeat=2)]
    for combo in incorrect_combos:
        if combo in expr:
            raise InputException("Лишний пробел между числами")

    expr = expr.replace(" ", "") + " "  # буферный пробел для избегания ошибок индексов
    if expr == " ":
        raise InputException("Пустое выражение")
    while i < len(expr):
        curent_symbol = expr[i]

        if curent_symbol.isdigit() or curent_symbol == ".":
            curent_number = curent_symbol

            while expr[i + 1].isdigit() or expr[i + 1] == ".":
                i += 1
                curent_number += expr[i]

            if curent_number[0] == "0" and len(curent_number) >= 2:
                if curent_number[:2] != "0.":
                    raise InputException("В числе присутствуют ведущие нули")

            if curent_number.count(".") > 1:
                raise InputException("В числе несколько точек")
            elif curent_number.count(".") == 1:
                if len(curent_number) != 1:
                    tokens.append(NumberToken(value=float(curent_number)))
                else:
                    raise InputException("Точка не является числом")
            else:
                tokens.append(NumberToken(value=int(curent_number)))
            curent_number = ""
            i += 1
            continue

        if expr[i : i + 2] in OPERATIONS.keys():
            tokens.append(OPERATIONS[expr[i : i + 2]]())
            i += 2
            continue

        if curent_symbol in OPERATIONS.keys():
            if i == 0:
                if curent_symbol == "+":
                    i += 1
                    continue
                elif curent_symbol == "-":
                    tokens.append(UnaryMinusToken())
                    i += 1
                    continue
            else:
                if tokens[-1].is_bracket():
                    if tokens[-1].is_open():
                        if curent_symbol == "+":
                            i += 1
                            continue
                        elif curent_symbol == "-":
                            tokens.append(UnaryMinusToken())
                            i += 1
                            continue
            tokens.append(OPERATIONS[curent_symbol]())
            i += 1
            continue

        if curent_symbol == "(":
            tokens.append(BracketToken(BracketTypes.OPEN))
            i += 1
            continue

        if curent_symbol == ")":
            tokens.append(BracketToken(BracketTypes.CLOSE))
            i += 1
            continue

        if curent_symbol == " ":
            break

        raise InputException("Выражение содержит лишние символы")

    return tokens


def check_tokens(tokens: list[Any]) -> None:
    """
    Проверка токенов вместе.

    :tokens: Список токенов
    :return: ничего не возвращает и не меняет аргументы
    """

    if tokens[-1].is_operation():
        raise InputException("Оператор не может быть последним токеном")

    i = 0
    bracket_counter = 0

    while i < len(tokens):
        if i == 0:
            if tokens[i].is_operation():
                if tokens[i].operation_type != OperationTypes.UNARY_MINUS:
                    raise InputException("Выражение не может начинаться с оператора")
        else:
            if tokens[i - 1].is_operation() and tokens[i].is_operation():
                raise InputException("Два оператора не могут идти подряд")

            if tokens[i - 1].is_bracket() and tokens[i].is_operation():
                if (
                    tokens[i - 1].is_open()
                    and tokens[i].operation_type != OperationTypes.UNARY_MINUS
                ):
                    raise InputException("Нет числа между скобкой и оператором")

            if tokens[i].is_bracket() and tokens[i - 1].is_operation():
                if tokens[i].is_close():
                    raise InputException("Нет числа между скобкой и оператором")

            if tokens[i - 1].is_bracket() and tokens[i].is_number():
                if tokens[i - 1].bracket_type == BracketTypes.CLOSE:
                    raise InputException("Нет оператора между скобкой и числом")

            if tokens[i].is_bracket() and tokens[i - 1].is_number():
                if tokens[i].bracket_type == BracketTypes.OPEN:
                    raise InputException("Нет оператора между скобкой и числом")

            if tokens[i - 1].is_number() and tokens[i].is_number():
                raise InputException("Нет оператора между числами")

            if tokens[i - 1].is_bracket() and tokens[i].is_bracket():
                if tokens[i - 1].bracket_type != tokens[i].bracket_type:
                    raise InputException("Между разными скобками нет оператора")
        if tokens[i].is_bracket():
            bracket_counter += tokens[i].bracket_type
            if bracket_counter < 0:
                raise InputException(
                    "В выражении присутстуют закрывающие скобки без открывающих"
                )
        i += 1

    if bracket_counter > 0:
        raise InputException("В выражении присутстуют незакрытые открывающие скобки")
    if bracket_counter < 0:
        raise InputException(
            "В выражении присутстуют закрывающие скобки без открывающих"
        )
