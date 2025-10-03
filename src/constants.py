import src.token as tkn
from typing import Any

SAMPLE_CONSTANT: int = 10
OPERATIONS: dict[str, Any] = {
    "+": tkn.AdditionToken,
    "-": tkn.SubstractionToken,
    "*": tkn.MultiplicationToken,
    "/": tkn.DivisionToken,
    "//": tkn.DivisionWithoutModToken,
    "%": tkn.ModToken,
    "**": tkn.PowerToken,
}
