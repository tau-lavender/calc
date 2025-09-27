from src.token import *

SAMPLE_CONSTANT: int = 10
OPERATIONS: dict[str] = {"+": AdditionToken, 
                         "-": SubstractionToken, 
                         "*": MultiplicationToken, 
                         "/": DivisionToken,
                         "//": DivisionWithoutModToken, 
                         "%": ModToken, 
                         "**": PowerToken}