from sloth.lexer import Lexer
from sloth.lexer import LexerError

bar = Lexer('foo 1 2\nbar 1 k').all_tokens()

try:
    for tok in bar:
        print(tok)
except LexerError as e:
    print(e)


"""LEFT_PAREN, RIGHT_PAREN, LEFT_BRACE, RIGHT_BRACE,
COMMA, DOT, MINUS, PLUS, SEMICOLON, SLASH, STAR,

// One or two character tokens.
BANG, BANG_EQUAL,
EQUAL, EQUAL_EQUAL,
GREATER, GREATER_EQUAL,
LESS, LESS_EQUAL,

// Literals.
IDENTIFIER, STRING, NUMBER,

// Keywords.
AND, CLASS, ELSE, FALSE, FUN, FOR, IF, NIL, OR,
PRINT, RETURN, SUPER, THIS, TRUE, VAR, WHILE,

EOF

rules = [
    '(?P<LEFT_PAREN>)\(',
    '(?P<RIGHT_PAREN>)\(',
    '(?P<NUMBER>)\d+',
]

"""
