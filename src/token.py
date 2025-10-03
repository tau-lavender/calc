from enum import Enum, IntEnum, auto


class TokenTypes(Enum):
    NUMBER = auto()
    OPERATION = auto()
    BRACKET = auto()


class BracketTypes(IntEnum):
    OPEN = 1
    CLOSE = -1


class OperationTypes(Enum):
    EMPTY = auto()
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


class AssociativityType(Enum):
    LEFT = auto()
    RIGHT = auto()


class Token:
    def __init__(self, type: TokenTypes) -> None:
        self.type = type
        self.operation_type = OperationTypes.EMPTY

    def is_number(self) -> bool:
        return self.type == TokenTypes.NUMBER

    def is_operation(self) -> bool:
        return self.type == TokenTypes.OPERATION

    def is_bracket(self) -> bool:
        return self.type == TokenTypes.BRACKET

    def __str__(self) -> str:
        return str(self.operation_type.name)

    def __repr__(self) -> str:
        return self.__str__()


class OperationToken(Token):
    def __init__(self) -> None:
        super().__init__(type=TokenTypes.OPERATION)
        self.operation_priority = OperationPriority.FIRST
        self.associativity_type = AssociativityType.LEFT


class NumberToken(Token):
    def __init__(self, value: float) -> None:
        super().__init__(type=TokenTypes.NUMBER)
        self.value = value

    def __str__(self) -> str:
        return str(self.value)


class BracketToken(Token):
    def __init__(self, bracket_type: BracketTypes) -> None:
        super().__init__(type=TokenTypes.BRACKET)
        self.bracket_type = bracket_type

    def __str__(self) -> str:
        return str(self.type.name) + " " + str(self.bracket_type.name)

    def is_open(self) -> bool:
        return self.bracket_type == BracketTypes.OPEN

    def is_close(self) -> bool:
        return self.bracket_type == BracketTypes.CLOSE


class UnaryMinusToken(Token):
    def __init__(self) -> None:
        super().__init__(type=TokenTypes.OPERATION)
        self.operation_type = OperationTypes.UNARY_MINUS
        self.operation_priority = OperationPriority.FIRST

    def calculate_operation(self, x: NumberToken) -> NumberToken:
        return NumberToken(-x.value)


class AdditionToken(Token):
    def __init__(self) -> None:
        super().__init__(type=TokenTypes.OPERATION)
        self.operation_type = OperationTypes.ADDITION
        self.operation_priority = OperationPriority.FOURTH

    def calculate_operation(self, x: NumberToken, y: NumberToken) -> NumberToken:
        return NumberToken(x.value + y.value)


class SubstractionToken(Token):
    def __init__(self) -> None:
        super().__init__(type=TokenTypes.OPERATION)
        self.operation_type = OperationTypes.SUBSTRACTION
        self.operation_priority = OperationPriority.FOURTH

    def calculate_operation(self, x: NumberToken, y: NumberToken) -> NumberToken:
        return NumberToken(x.value - y.value)


class MultiplicationToken(Token):
    def __init__(self) -> None:
        super().__init__(type=TokenTypes.OPERATION)
        self.operation_type = OperationTypes.MULTIPLICATION
        self.operation_priority = OperationPriority.THIRD

    def calculate_operation(self, x: NumberToken, y: NumberToken) -> NumberToken:
        return NumberToken(x.value * y.value)


class DivisionToken(Token):
    def __init__(self) -> None:
        super().__init__(type=TokenTypes.OPERATION)
        self.operation_type = OperationTypes.DIVISION
        self.operation_priority = OperationPriority.THIRD

    def calculate_operation(self, x: NumberToken, y: NumberToken) -> NumberToken:
        return NumberToken(x.value / y.value)


class DivisionWithoutModToken(Token):
    def __init__(self) -> None:
        super().__init__(type=TokenTypes.OPERATION)
        self.operation_type = OperationTypes.DIVISION_WITHOUT_MOD
        self.operation_priority = OperationPriority.THIRD

    def calculate_operation(self, x: NumberToken, y: NumberToken) -> NumberToken:
        return NumberToken(x.value // y.value)


class ModToken(Token):
    def __init__(self) -> None:
        super().__init__(type=TokenTypes.OPERATION)
        self.operation_type = OperationTypes.MOD_
        self.operation_priority = OperationPriority.THIRD

    def calculate_operation(self, x: NumberToken, y: NumberToken) -> NumberToken:
        return NumberToken(x.value % y.value)


class PowerToken(Token):
    def __init__(self) -> None:
        super().__init__(type=TokenTypes.OPERATION)
        self.operation_type = OperationTypes.POWER
        self.operation_priority = OperationPriority.SECOND

    def calculate_operation(self, x: NumberToken, y: NumberToken) -> NumberToken:
        return NumberToken(x.value**y.value)
