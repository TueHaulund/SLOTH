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

    IDENTIFIER = '[a-zA-Z_][a-zA-Z0-9_]*'

    EOL = '\n'

class Token(object):
    def __init__(self, token_name, lexeme, pos):
        self.type = LexicalGrammar[token_name]
        self.lexeme = lexeme
        self.pos = pos

    def __str__(self):
        return '{}({}) at Line {}, Column {}'.format(
            self.type.name,
            self.lexeme.replace('\n', '\\n'),
            self.pos[0],
            self.pos[1]
        )

    def __repr__(self):
        return self.type.name

    def __eq__(self, other):
        return self.type == other.type and self.lexeme == other.lexeme and self.pos == other.pos
