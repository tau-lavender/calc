import src.token as tkn

SAMPLE_CONSTANT: int = 10
OPERATIONS: dict[str] = {"+": tkn.AdditionToken, 
                         "-": tkn.SubstractionToken, 
                         "*": tkn.MultiplicationToken, 
                         "/": tkn.DivisionToken,
                         "//": tkn.DivisionWithoutModToken, 
                         "%": tkn.ModToken, 
                         "**": tkn.PowerToken}

