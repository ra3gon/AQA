from types import NoneType

import pytest
from string_utils import StringUtils

su = StringUtils()

# @pytest.mark.parametrize('string, result', [
#     ("hello", "Hello"),
#     ("привет", "Привет"),
#     ("hello world", "Hello world"),
#     ("Hello", "Hello"),
#     (" ", " "),
#     ("123hello", "123hello"),
#     ("!hello", "!hello"),
#     (" hello", " hello")
#     ])
# def test_capitilize(string, result):
#     res = su.capitilize(string)
#     assert res == result


@pytest.mark.parametrize('string, result', [
    ("  hello", "hello"),
    ("  ", ""),
    ("  .hello",".hello"),
    (" 123", "123"),
    ("  hello world", "hello world"),
    ("  %ˆ(*", "%ˆ(*")
    ])
def test_trim(string, result):
    res = su.trim(string)
    assert res == result




