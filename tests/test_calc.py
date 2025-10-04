import pytest

from src.token import CalculationException
from src.calc import calc_infix


class TestCalcIndex:
    """
    Проверяет вычисление инфиксной нотации
    """

    def test_simple_use(self) -> None:
        assert calc_infix("- 1") == -1
        assert calc_infix("+ 1") == 1
        assert calc_infix("1 + 1") == 2
        assert calc_infix("2 - 1") == 1
        assert calc_infix("2 * 3") == 6
        assert calc_infix("5 / 2") == 2.5
        assert calc_infix("5 // 2") == 2
        assert calc_infix("5 % 2") == 1
        assert calc_infix("5 ** 2") == 25
        assert calc_infix("5 ** 0") == 1
        assert calc_infix("0 ** 0") == 1
        assert calc_infix("0 ** 1") == 0

    def test_float(self) -> None:
        assert calc_infix("- 1.5") == -1.5
        assert calc_infix("+ 1.5") == 1.5
        assert calc_infix("1 + 1.5") == 2.5
        assert calc_infix("2 - 1.5") == 0.5
        assert calc_infix("2 * 3.5") == 7.0
        assert calc_infix("5.2 / 2") == 2.6
        assert calc_infix("25 ** 0.5") == 5.0
        assert calc_infix("0 ** 0.5") == 0.0

    def test_priority(self) -> None:
        assert calc_infix("2 + 2 * 2") == 6
        assert calc_infix("2 - 8 / 2 ** 2") == 0
        assert calc_infix("2 ** 2 ** 3") == 256
        assert calc_infix("1 + 2 + 3 + 4") == 10
        assert calc_infix("-1 + 2") == 1
        assert calc_infix("2 - (2 + 2)") == -2
        assert calc_infix("2 * (-2 + 2)") == 0
        assert calc_infix("2 * (1 + 1)") == 4

    def test_devizion_by_0(self) -> None:
        with pytest.raises(CalculationException):
            calc_infix("2 / 0")
        with pytest.raises(CalculationException):
            calc_infix("2 // 0")
        with pytest.raises(CalculationException):
            calc_infix("2 % 0")

    def test_dev_with_mod_float(self) -> None:
        with pytest.raises(CalculationException):
            calc_infix("2.1 // 2")
        with pytest.raises(CalculationException):
            calc_infix("2 // 2.1")
        with pytest.raises(CalculationException):
            calc_infix("2.1 // 2.2")

    def test_mod_float(self) -> None:
        with pytest.raises(CalculationException):
            calc_infix("2.1 % 2")
        with pytest.raises(CalculationException):
            calc_infix("2 % 2.1")
        with pytest.raises(CalculationException):
            calc_infix("2.1 % 2.2")

    def test_power(self) -> None:
        with pytest.raises(CalculationException):
            calc_infix("0 ** (-1)")
        with pytest.raises(CalculationException):
            calc_infix("-1 ** 0.5")
