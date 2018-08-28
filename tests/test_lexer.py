import pytest

from sloth.lexer import Lexer
from sloth.token import Token

@pytest.mark.parametrize('test_str', [
    '', ' ', ' \t ', '\n\n', '\n\t ', '        ',
])
def test_empty(test_str):
    tokens = Lexer(test_str).all_tokens()
    assert tokens == []

@pytest.mark.parametrize('test_str, expected', [
    (
        '1',
        [
            Token('NUMBER', '1', (1, 1)),
        ],
    ),
    (
        'foobar',
        [
            Token('IDENTIFIER', 'foobar', (1, 1)),
        ],
    ),
    (
        'foo 1 2',
        [
            Token('IDENTIFIER', 'foo', (1, 1)),
            Token('NUMBER', '1', (1, 5)),
            Token('NUMBER', '2', (1, 7)),
        ],
    ),
])
def test_valid_input(test_str, expected):
    tokens = Lexer(test_str).all_tokens()
    assert tokens == expected
