import sys
from src.constants import HELP_MSG
from src.calc import calc_infix
from src.token import CalculationException
from src.tokenizer import InputException


def main() -> None:
    """
    Функция считывает строку из консоли.

    Если строка является командой "help" выводится краткая документация
    Если строка является командой "exit" программа завершает работу
    Если строка является корректным арифметическим выражением, в консоль возвращается его решение
    Если в выражении допущена ошибка, возвращается пояснение почему выражение не обработано
    :return: Данная функция ничего не возвращает
    """

    print(HELP_MSG)

    for line in sys.stdin:
        if line.strip() == "exit":
            exit(0)
        if line.strip() == "help":
            print(HELP_MSG)
            continue

        try:
            print(calc_infix(line))
        except InputException as e:
            print("Error:", str(e))
        except CalculationException as e:
            print("Error:", str(e))


if __name__ == "__main__":
    main()
