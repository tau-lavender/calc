from typing import Any
from src.token import OperationTypes
from src.tokenizer import InputException

def calc_rpn(rpn: list[Any]) -> int | float:

    stack: list[int | float] = []

    for token in rpn:
        if token.is_number():
            stack.append(token)

        elif token.is_operation():
            if token.operation_type == OperationTypes.UNARY_MINUS:
                result = token.calculate_operation(stack.pop())
            else:
                y = stack.pop()
                x = stack.pop()
                result = token.calculate_operation(x, y)
            stack.append(result)

    final_result = stack.pop()
    if stack:
        raise InputException("Выражение не корректно")

    return final_result
