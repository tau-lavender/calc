import sys
from src.tokenizer import get_tokens, check_tokens
from src.shunting_yard import get_rpn
from src.calc import calc_rpn


def main() -> None:
    """
    Функция считывает строку из консоли.
    Если строка является корректным арифметическим выражением, в консоль возвращается его решение
    Если в выражении допущена ошибка, возвращается пояснение почему выражение не обработано
    :return: Данная функция ничего не возвращает
    """

    for line in sys.stdin:
        tokens = get_tokens(line.strip())
        print(tokens)
        check_tokens(tokens)
        rpn = get_rpn(tokens)
        print(rpn)
        answer = calc_rpn(rpn)
        print(answer)

if __name__ == "__main__":
    main()
