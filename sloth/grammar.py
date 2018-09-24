import enum


class LexicalGrammar(enum.Enum):

    # Special Characters
    LEFT_PAREN = '\('
    RIGHT_PAREN = '\)'
    COMMA = '\,'
    COLON = '\:'
    SEMI_COLON = '\;'

    MULTIPLY = '\*'
    ADDITION = '\+'
    SUBTRACTION = '\-'
    DIVISION = '\/'

    GREATER_THAN = '\>'
    LESS_THAN = '\<'
    EQUALS = '\='

    COMMENT = '#(.*)(\n|\Z)'
    EOL = '\n'

    # Literals
    NUMBER = '\d+'
    TRUE = 'true'
    FALSE = 'false'

    # Keywords
    IF = 'if'
    THEN = 'then'
    ELIF = 'elif'
    ELSE = 'else'

    WHILE = 'while'
    FOR = 'for'
    END = 'end'

    NUM = 'num'
    BOOL = 'bool'
    VOID = 'void'

    DEF = 'def'
    RETURN = 'return'

    OR = 'or'
    AND = 'and'
    NOT = 'not'

    # Identifiers
    IDENTIFIER = '[a-zA-Z_][a-zA-Z0-9_]*'
