import pytest

from sloth.lexer import Lexer

@pytest.mark.parametrize('test_str, expected', [
    ('foo 1 2', [])
])
def test_valid_input(test_str, expected):
    lexer = iter(Lexer(test_str))
    assert list(lexer) == expected
