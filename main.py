from sloth.lexer import Lexer
from sloth.lexer import LexerError

# bar = Lexer('foo12 #1 2\nbar 1 k# a\n2').all_tokens()

with open('example.sl', 'r') as myfile:
    data = myfile.read()

bar = Lexer(data).all_tokens()

try:
    for tok in bar:
        print(tok)
except LexerError as e:
    print(e)
