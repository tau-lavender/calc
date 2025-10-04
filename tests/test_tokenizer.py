import pytest

from src.tokenizer import InputException
from src.tokenizer import get_tokens, check_tokens


class TestGetTokens:
    """
    Проверяет преобразование в токены
    :return: ничего не возвращает
    """

    def test_simple_cases(self) -> None:
        get_tokens("1 + 1")
        get_tokens("-1 + 1")
        get_tokens("-11 * 2 + (-3) - 4 + 5/2 - (4 // 3 + 4 % 3 + 2 ** 2)")
        get_tokens("1")
        get_tokens("-1")
        get_tokens("1.1")
        get_tokens("0")
        get_tokens("0.1")

    def test_format_errors(self) -> None:
        with pytest.raises(InputException):
            get_tokens(" ")
        with pytest.raises(InputException):
            get_tokens("0,1")
        with pytest.raises(InputException):
            get_tokens("2 2 +")
        with pytest.raises(InputException):
            get_tokens("0021")
        with pytest.raises(InputException):
            get_tokens("00.21")
        with pytest.raises(InputException):
            get_tokens("1.2.1")
        with pytest.raises(InputException):
            get_tokens(".")
        with pytest.raises(InputException):
            get_tokens("pablo")


class TestCheckTokens:
    def test_toens_errors(self) -> None:
        with pytest.raises(InputException):
            check_tokens(get_tokens("2 + 2 +"))
        with pytest.raises(InputException):
            check_tokens(get_tokens("* 2 + 2"))
        with pytest.raises(InputException):
            check_tokens(get_tokens("2 + + 2"))
        with pytest.raises(InputException):
            check_tokens(get_tokens("2 2"))

    def test_check_brackets(self) -> None:
        with pytest.raises(InputException):
            check_tokens(get_tokens("2 + (2 * )"))
        with pytest.raises(InputException):
            check_tokens(get_tokens("2 * (* 2 + 2)"))
        with pytest.raises(InputException):
            check_tokens(get_tokens("2+2 (2 + 2)"))
        with pytest.raises(InputException):
            check_tokens(get_tokens("(2 + 2) 2 + 2"))
        with pytest.raises(InputException):
            check_tokens(get_tokens("(2 + 2) (2 + 2)"))
        with pytest.raises(InputException):
            check_tokens(get_tokens("()"))
        with pytest.raises(InputException):
            check_tokens(get_tokens("(2 + 2"))
        with pytest.raises(InputException):
            check_tokens(get_tokens("2 + 2)"))
