import enum

"""TOKENS."""

class TokenTypes(enum.Enum):
    LEFT_PAREN = '\('
    RIGHT_PAREN = '\)'
    COMMA = '\,'
    PERIOD = '\.'

    MULTIPLY = '\*'
    ADDITION = '\+'
    SUBTRACTION = '\-'
    DIVISION = '\\\\'

    GREATER_EQUAL = '\>\='
    GREATER_THAN = '\>'

    LESS_EQUAL = '\<\='
    LESS_THAN = '\<'

    EQUAL = '\=\='

    ASSIGNMENT = '\:\='

    NUMBER = '\d+'

    IDENTIFIER = '[a-zA-Z_][a-zA-Z0-9_]*'

    EOL = '\n'

class Token(object):
    def __init__(self, type_name, lexeme, pos):
        self.type = TokenTypes[type_name]
        self.lexeme = lexeme
        self.pos = pos

    def __str__(self):
        return '{}({}) at Line {}, Column {}'.format(self.type.name, self.lexeme, self.pos[0], self.pos[1])

    def __repr__(self):
        return self.type.name
