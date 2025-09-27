import sys
from tokenizer import get_tokens
from constants import SAMPLE_CONSTANT


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

if __name__ == "__main__":
    main()
