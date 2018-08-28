import enum

class LexicalGrammar(enum.Enum):
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

    IF = 'if'
    THEN = 'then'
    ELIF = 'elif'
    ELSE = 'else'
    FI = 'fi'

    TRUE = 'true'
    FALSE = 'false'

    IDENTIFIER = '[a-zA-Z_][a-zA-Z0-9_]*'

    EOL = '\n'
