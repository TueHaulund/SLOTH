import pytest

from sloth.lexer import Lexer
from sloth.token import Token


@pytest.mark.parametrize('test_str', ['', ' ', ' \t ', '\n\n', '\n\t ', '        '])
def test_empty(test_str):
    tokens = Lexer(test_str).all_tokens()
    assert tokens == []


@pytest.mark.parametrize(
    'test_str, expected',
    [
        ('1', [Token('NUMBER', '1', (1, 1))]),
        ('foobar', [Token('IDENTIFIER', 'foobar', (1, 1))]),
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
