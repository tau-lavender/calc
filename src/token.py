from enum import Enum, IntEnum, auto


class TokenTypes(Enum):
    NUMBER = auto()
    OPERATION = auto()
    BRACKET= auto()


class BracketTypes(IntEnum):
    OPEN = 1
    CLOSE = -1


class OperationTypes(Enum):
    UNARY_PLUS = auto()
    UNARY_MINUS = auto()
    ADDITION = auto()
    SUBSTRACTION = auto()
    MULTIPLICATION = auto()
    DIVISION = auto()
    DIVISION_WITHOUT_MOD = auto()
    MOD_ = auto()
    POWER = auto()


class OperationPriority(IntEnum):
    FIRST = 1
    SECOND = 2
    THIRD = 3
    FOURTH = 4


class Token():
    def __init__(self, type: TokenTypes):
        self.type = type
    

    def is_number(self):
        return self.type == TokenTypes.NUMBER
    

    def is_operation(self):
        return self.type == TokenTypes.OPERATION
    

    def __str__(self):
        return str(self.type)


    def __repr__(self):
        return self.__str__()


class NumberToken(Token):
    def __init__(self, value: float):
        super().__init__(type = TokenTypes.NUMBER, value = value)
        self.value = value
    

    def __str__(self):
        return str(self.value)


class BracketToken(Token):
    def __init__(self, type = TokenTypes.BRACKET, ):
        super().__init__(type)
        self.bracket_type = type


class AdditionToken(Token):
    def __init__(self, type: TokenTypes):
        super().__init__(type)
        self.operation_type = OperationTypes.ADDITION
        self.operation_priority = OperationPriority.FOURTH
    

    def calculate_operation(self, x: NumberToken, y: NumberToken):
        return x.value + y.value


class SubstractionToken(Token):
    def __init__(self, type: TokenTypes):
        super().__init__(type)
        self.operation_type = OperationTypes.SUBSTRACTION
        self.operation_priority = OperationPriority.FOURTH
    

    def calculate_operation(self, x: NumberToken, y: NumberToken):
        return x.value - y.value


class MultiplicationToken(Token):
    def __init__(self, type: TokenTypes):
        super().__init__(type)
        self.operation_type = OperationTypes.MULTIPLICATION
        self.operation_priority = OperationPriority.THIRD
    

    def calculate_operation(self, x: NumberToken, y: NumberToken):
        return x.value * y.value


class DivisionToken(Token):
    def __init__(self, type: TokenTypes):
        super().__init__(type)
        self.operation_type = OperationTypes.DIVISION
        self.operation_priority = OperationPriority.THIRD
    

    def calculate_operation(self, x: NumberToken, y: NumberToken):
        return x.value / y.value


class DivisionWithoutModToken(Token):
    def __init__(self, type: TokenTypes):
        super().__init__(type)
        self.operation_type = OperationTypes.DIVISION_WITHOUT_MOD
        self.operation_priority = OperationPriority.THIRD
    

    def calculate_operation(self, x: NumberToken, y: NumberToken):
        return x.value // y.value
    


class ModToken(Token):
    def __init__(self, type: TokenTypes):
        super().__init__(type)
        self.operation_type = OperationTypes.MOD_
        self.operation_priority = OperationPriority.THIRD
    

    def calculate_operation(self, x: NumberToken, y: NumberToken):
        return x.value % y.value
    

class PowerToken(Token):
    def __init__(self, type: TokenTypes):
        super().__init__(type)
        self.operation_type = OperationTypes.POWER
        self.operation_priority = OperationPriority.SECOND
    

    def calculate_operation(self, x: NumberToken, y: NumberToken):
        return x.value ** y.value


