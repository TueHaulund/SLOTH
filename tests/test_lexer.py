import pytest

from sloth.lexer import Lexer
from sloth.lexer import LexerError
from sloth.token import Token


@pytest.mark.parametrize('test_str', ['', ' ', ' \t ', '\n\n', '\n\t ', '        '])
def test_empty(test_str):
    tokens = Lexer(test_str).all_tokens()
    assert tokens == []


@pytest.mark.parametrize(
    'test_str, token_name',
    [
        ('(', 'LEFT_PAREN'),
        (')', 'RIGHT_PAREN'),
        (',', 'COMMA'),
        (':', 'COLON'),
        (';', 'SEMI_COLON'),
        ('*', 'MULTIPLY'),
        ('+', 'ADDITION'),
        ('-', 'SUBTRACTION'),
        ('/', 'DIVISION'),
        ('>', 'GREATER_THAN'),
        ('<', 'LESS_THAN'),
        ('=', 'EQUALS'),
        ('1', 'NUMBER'),
        ('true', 'TRUE'),
        ('false', 'FALSE'),
        ('if', 'IF'),
        ('then', 'THEN'),
        ('elif', 'ELIF'),
        ('else', 'ELSE'),
        ('while', 'WHILE'),
        ('for', 'FOR'),
        ('end', 'END'),
        ('num', 'NUM'),
        ('bool', 'BOOL'),
        ('void', 'VOID'),
        ('def', 'DEF'),
        ('return', 'RETURN'),
        ('or', 'OR'),
        ('and', 'AND'),
        ('not', 'NOT'),
        ('f', 'IDENTIFIER'),
    ],
)
def test_valid_single_token(test_str, token_name):
    tokens = Lexer(test_str).all_tokens()
    assert tokens == [Token(token_name, test_str, (1, 1))]


@pytest.mark.parametrize('test_str', ['1 ', '1 \t ', '1\n\n', '1\n\t ', '1        '])
def test_trailing_whitespace(test_str):
    tokens = Lexer(test_str).all_tokens()
    assert tokens == [Token('NUMBER', '1', (1, 1))]


@pytest.mark.parametrize(
    'test_str, expected_pos',
    [
        (' 1', (1, 2)),
        (' \t 1', (1, 4)),
        ('\n\n1', (3, 1)),
        ('\n\t 1', (2, 3)),
        ('        1', (1, 9)),
        (' \n \n \n \t1', (4, 3)),
    ],
)
def test_leading_whitespace(test_str, expected_pos):
    tokens = Lexer(test_str).all_tokens()
    assert tokens == [Token('NUMBER', '1', expected_pos)]


@pytest.mark.parametrize(
    'test_str, expected',
    [
        (
            'foo 1 2',
            [
                Token('IDENTIFIER', 'foo', (1, 1)),
                Token('NUMBER', '1', (1, 5)),
                Token('NUMBER', '2', (1, 7)),
            ],
        ),
        (
            'foo 1 2\nbar 1 k',
            [
                Token('IDENTIFIER', 'foo', (1, 1)),
                Token('NUMBER', '1', (1, 5)),
                Token('NUMBER', '2', (1, 7)),
                Token('EOL', '\n', (1, 8)),
                Token('IDENTIFIER', 'bar', (2, 1)),
                Token('NUMBER', '1', (2, 5)),
                Token('IDENTIFIER', 'k', (2, 7)),
            ],
        ),
        (
            'if true then bar end',
            [
                Token('IF', 'if', (1, 1)),
                Token('TRUE', 'true', (1, 4)),
                Token('THEN', 'then', (1, 9)),
                Token('IDENTIFIER', 'bar', (1, 14)),
                Token('END', 'end', (1, 18)),
            ],
        ),
    ],
)
def test_valid_input(test_str, expected):
    tokens = Lexer(test_str).all_tokens()
    assert tokens == expected


@pytest.mark.parametrize('test_str', ['#', '&', '|', 'Ø'])
def test_invalid_single_token(test_str):
    with pytest.raises(LexerError) as exc_info:
        Lexer(test_str).all_tokens()

    assert exc_info.value.pos == (1, 1)


@pytest.mark.parametrize(
    'test_str, expected_pos',
    [
        (' #', (1, 2)),
        (' \t #', (1, 4)),
        ('\n\n#', (3, 1)),
        ('\n\t #', (2, 3)),
        ('        #', (1, 9)),
        (' \n \n \n \t#', (4, 3)),
    ],
)
def test_error_pos(test_str, expected_pos):
    with pytest.raises(LexerError) as exc_info:
        Lexer(test_str).all_tokens()

    assert exc_info.value.pos == expected_pos
