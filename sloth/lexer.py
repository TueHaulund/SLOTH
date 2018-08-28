import re

from sloth.token import LexicalGrammar
from sloth.token import Token

class LexerError(Exception):
    def __init__(self, pos):
        self.pos = pos
        self.description = 'LexerError at Line {}, Column {}'.format(self.pos[0], self.pos[1])

    def __str__(self):
        return self.description

    def __repr__(self):
        return 'LexerError {}'.format(self.pos)

class Lexer(object):
    def __init__(self, buf):
        self.buffer = buf.strip()
        self.line = 1
        self.column = 1

        grouped_rules = ['(?P<{}>{})'.format(t.name, t.value) for t in LexicalGrammar]

        self.regex = re.compile('|'.join(grouped_rules))

    def skip_ws(self):
        stripped = self.buffer.lstrip(' \t')
        self.column += len(self.buffer) - len(stripped)
        self.buffer = stripped

    def escape_lexeme(self, lexeme):
        return lexeme.replace('\n', '\\n')

    def next_token(self):
        while self.buffer:
            self.skip_ws()

            match = self.regex.match(self.buffer)
            pos = (self.line, self.column)

            if not match:
                print(self.buffer)
                raise LexerError(pos)

            lexeme = self.escape_lexeme(match.group(match.lastgroup))

            token = Token(
                match.lastgroup,
                lexeme,
                pos,
            )

            if match.lastgroup == 'EOL':
                self.line += 1
                self.column = 1
            else:
                self.column += match.end() - match.start()

            self.buffer = self.buffer[match.end():]
            yield token

    def all_tokens(self):
        return [token for token in self.next_token()]
