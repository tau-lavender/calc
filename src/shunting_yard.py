from typing import Any
from src.token import AssociativityTypes


def get_rpn(tokens: list[Any]) -> list[Any]:
    """
    Переводит переводит лист токенов в инфиксной записи в лист токенов в обратной польской нотации

    :tokens: Лист токенов в инфиксной нотации
    :return: Лист токенов в обратной польской нотации
    """

    res: list[Any] = []
    op_stack: list[Any] = []
    for tok in tokens:
        if tok.is_number():
            res.append(tok)

        if tok.is_operation():
            while (
                op_stack
                and op_stack[-1].is_operation()
                and (
                    tok.associativity_type == AssociativityTypes.RIGHT
                    and (op_stack[-1].operation_priority < tok.operation_priority)
                    or tok.associativity_type == AssociativityTypes.LEFT
                    and (op_stack[-1].operation_priority <= tok.operation_priority)
                )
            ):
                res.append(op_stack.pop())
            op_stack.append(tok)

        if tok.is_bracket():
            if tok.is_open():
                op_stack.append(tok)
            if tok.is_close():
                while op_stack:
                    if op_stack[-1].is_bracket():
                        if op_stack[-1].is_open():
                            break
                    res.append(op_stack.pop())
                if op_stack and op_stack[-1].is_bracket():
                    if op_stack[-1].is_open():
                        op_stack.pop()

    while op_stack:
        res.append(op_stack.pop())

    return res
