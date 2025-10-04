from typing import Any
from src.token import OperationTypes, NumberToken
from src.tokenizer import InputException
from src.tokenizer import get_tokens, check_tokens
from src.shunting_yard import get_rpn


def calc_rpn(rpn: list[Any]) -> NumberToken:
    stack: list[NumberToken] = []

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


def calc_infix(line: str) -> int | float:
    tokens = get_tokens(line.strip())
    check_tokens(tokens)
    rpn = get_rpn(tokens)
    answer: NumberToken = calc_rpn(rpn)
    return answer.value
