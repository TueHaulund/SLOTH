from sloth.grammar import LexicalGrammar


class Token(object):
    def __init__(self, token_name, lexeme, pos):
        self.type = LexicalGrammar[token_name]
        self.lexeme = lexeme
        self.pos = pos

    def __str__(self):
        return '{}({}) at Line {}, Column {}'.format(
            self.type.name, self.lexeme.replace('\n', '\\n'), self.pos[0], self.pos[1]
        )

    def __repr__(self):
        return self.type.name

    def __eq__(self, other):
        if isinstance(other, Token):
            return (
                self.type == other.type
                and self.lexeme == other.lexeme
                and self.pos == other.pos
            )
