from sloth.lexer import Lexer
from sloth.lexer import LexerError

bar = Lexer('foo 1 2\nbar 1 k').all_tokens()

try:
    for tok in bar:
        print(tok)
except LexerError as e:
    print(e)
