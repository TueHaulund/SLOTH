import re

from sloth.grammar import LexicalGrammar
from sloth.token import Token


class LexerError(Exception):
    def __init__(self, pos):
        self.pos = pos
        self.description = 'LexerError at Line {}, Column {}'.format(
            self.pos[0], self.pos[1]
        )

    def __str__(self):
        return self.description

    def __repr__(self):
        return 'LexerError {}'.format(self.pos)


class Lexer(object):
    def __init__(self, buf):
        self.buffer = buf.strip()
        self.pos = 0
        self.line = 1
        self.column = 1

        grouped_rules = ['(?P<{}>{})'.format(t.name, t.value) for t in LexicalGrammar]

        self.regex = re.compile('|'.join(grouped_rules))

    def skip_ws(self):
        while self.buffer[self.pos] in [' ', '\t']:
            self.pos += 1
            self.column += 1

    def next_token(self):
        while self.pos < len(self.buffer):
            self.skip_ws()

            match = self.regex.match(self.buffer[self.pos :])

            if not match:
                raise LexerError((self.line, self.column))

            lexeme = match.group(match.lastgroup)

            token = Token(match.lastgroup, lexeme, (self.line, self.column))

            if '\n' in lexeme:
                self.line += 1
                self.column = 1
            else:
                self.column += match.end() - match.start()

            self.pos += match.end()
            yield token

    def all_tokens(self):
        return list(self.next_token())
