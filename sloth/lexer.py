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
        # Initialise position state
        self.pos = 0
        self.line = 1
        self.column = 1

        # Remove trailing whitespace from buffer
        self.buffer = buf.rstrip()

        # Remove leading whitespace from buffer
        # But advance lexer position accordingly
        # Ensures token positions are accurate
        if self.buffer:
            self.skip_whitespace([' ', '\t', '\n'])

        # Compile regex for lexing
        grouped_rules = ['(?P<{}>{})'.format(t.name, t.value) for t in LexicalGrammar]
        self.regex = re.compile('|'.join(grouped_rules))

    def advance(self):
        if self.buffer[self.pos] == '\n':
            self.line += 1
            self.column = 1
        else:
            self.column += 1
        self.pos += 1

    def skip_whitespace(self, whitespace):
        while self.buffer[self.pos] in whitespace:
            self.advance()

    def next_token(self):
        while self.pos < len(self.buffer):
            # Advance past whitespace
            self.skip_whitespace([' ', '\t'])

            # Apply lexing regex at current positon
            match = self.regex.match(self.buffer[self.pos :])

            if not match:
                raise LexerError((self.line, self.column))

            lexeme = match.group(match.lastgroup)

            # Build token
            token = Token(match.lastgroup, lexeme, (self.line, self.column))

            # Advance lexer position past current lexeme
            for _ in lexeme:
                self.advance()

            yield token

    def all_tokens(self):
        return list(self.next_token())
