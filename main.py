from sloth.lexer import Lexer
from sloth.lexer import LexerError

bar = iter(Lexer("12 4 ( 5)\n23eqweqweqwee 45"))

try:
    for tok in bar:
        print(tok)
except LexerError as e:
    print(e)
