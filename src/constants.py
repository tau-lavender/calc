import src.token as tkn
from typing import Any

OPERATIONS: dict[str, Any] = {
    "+": tkn.AdditionToken,
    "-": tkn.SubstractionToken,
    "*": tkn.MultiplicationToken,
    "/": tkn.DivisionToken,
    "//": tkn.DivisionWithoutModToken,
    "%": tkn.ModToken,
    "**": tkn.PowerToken,
}
HELP_MSG = """
###### Calc lab M2 ######
Калькулятор поддерживает целые числа и дробные через точку
Унарные "+" и "-" не должны стоять перед другими операциями,
только в начале выражения, перед или после скобки
Допустимые операции ["+", "-", "*", "/", "//", "%", "**"]
Команды:
help - для вывода этого сообщения
exit - для завершения из программы
#########################
"""
