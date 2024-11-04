import pytest
from string_utils import StringUtils

su = StringUtils()

@pytest.mark.parametrize('string, result', [
    ("hello", "Hello"),
    ("привет", "Привет"),
    ("hello world", "Hello world"),
    ("Hello", "Hello"),
    (" ", " "),
    ("123hello", "123hello"),
    ("!hello", "!hello"),
    (" hello", " hello")
])
def test_capitilize(string, result):
    assert su.capitilize(string) == result


@pytest.mark.parametrize('string, result', [
    ("  hello", "hello"),
    ("hello", "hello"),
    ("hello ", "hello "),
    ("  ", ""),
    ("", ""),
    ("  .hello", ".hello"),
    (" 123", "123"),
    ("  hello world", "hello world"),
    ("  %ˆ(*", "%ˆ(*")
])
def test_trim(string, result):
    assert su.trim(string) == result


@pytest.mark.parametrize('string, delimeter, result', [
        ("a,b,c,d", ",", ["a", "b", "c", "d"]),
        ("1:2:3:4", ":", ["1", "2", "3", "4"]),
        ("1a2a3a4", "a", ["1", "2", "3", "4"]),
        ("apple|honor|samsung", "|", ["apple", "honor", "samsung"]),
        ("", ",", []),
        ("apple", ",", ["apple"]),
        (",,,", ",", ["", "", "", ""]),
        ("   skypro   ", " ", ["", "", "", "skypro", "", "", ""]),
        (":::", ":", ["", "", "", ""]),
        ("apple,honor,samsung", ";", ["apple,honor,samsung"])
])
def test_to_list(string, delimeter, result):
    assert su.to_list(string, delimeter) == result

@pytest.mark.parametrize('string, symbol, result', [
    ("Skypro", "y", True),
    ("Skypro", "v", False),
    ("SKYPRO", "v", False),
    ("Skypro", "Y", False),
    ("SkyPro", "P", True),
    ("Sky1pro", "1", True),
    ("Skypro", "", False),
    ("Sky pro", "r", True),
    ("Sky pro", " ", True),
    ("1286", "8", True),
    ("", "", True)
])
def test_contains(string, symbol, result):
    assert su.contains(string, symbol) == result

@pytest.mark.parametrize('string, symbol, result', [
    ("SkyPro", "k", "SyPro"),
    ("SkyPro", "Sky", "Pro"),
    ("SkyPro", "Pro", "Sky"),
    ("aaaaa", "a", ""),
    ("skyproskyskypro", "sky", "propro"),
    ("", "f", ""),
    ("Sky, Pro", "f", "Sky, Pro"),
    ("Sky Pro", " ", "SkyPro"),
    ("SkyPro", "skypro", "SkyPro"),
    ("sky   pro", " ", "skypro"),
    ("222%333", "%", "222333"),
    ("single character", "e", "singl charactr"),
    ("Sky@Pro", "@", "SkyPro")
])
def test_delete_symbol(string, symbol, result):
    assert su.delete_symbol(string, symbol) == result

@pytest.mark.parametrize('string, symbol, result', [
    ("SkyPro", "S", True),
    ("SkyPro", "P", False),
    ("sky pro", "sky", True),
    ("sky pro", "pro", False),
    ("SkyPro", "s", False),
    ("", "", True),
    ("Test", "", True),
    ("", "a", False),
    ("12345", "123", True),
    ("12345", "234", False),
    ("   leading spaces", "   ", True),
    ("Special@Symbol", "Special@", True),
    ("@Symbol", "@", True),
    (".skypro", ".", True),
    ("MixedCASE", "mixed", False)
])
def test_starts_with(string, symbol, result):
    assert su.starts_with(string, symbol) == result

@pytest.mark.parametrize('string, symbol, result', [
     ("SkyPro", "o", True),
     ("SkyPro", "P", False),
     ("sky pro", "sky", False),
     ("sky pro", "pro", True),
     ("SkyPro", "s", False),
     ("", "", True),
     ("Test", "", True),
     ("", "a", False),
     ("12345", "345", True),
     ("12345", "234", False),
     ("leading spaces   ", "   ", True),
     ("Special@Symbol", "@Symbol", True),
     ("Symbol@", "@", True),
     ("skypro.", ".", True),
     ("MixedCASE", "mixed", False)
])
def test_end_with(string, symbol, result):
    assert su.end_with(string, symbol) == result

@pytest.mark.parametrize('string, resault', [
    ("", True),
    (" ", True),
    ("Skypro", False),
    ("  Skypro", False),
    ("Skypro  ", False),
    ("123", False),
    ("Sky Pro", False),
    ("*&@$%@!", False)
])
def test_is_empty(string, resault):
    assert su.is_empty(string) == resault

@pytest.mark.parametrize('lst, joiner, result', [
    ([1, 2, 3, 4], ". ", "1. 2. 3. 4"),
    (["Sky", "Pro"], "", "SkyPro"),
    (["Sky", "Pro", "Automation"], " ", "Sky Pro Automation"),
    (["Sk", "Pro"], "y", "SkyPro"),
    (["Sky", "Pro"], "AQA", "SkyAQAPro"),
    (["Sky", "Pro"], "-", "Sky-Pro"),
    (["Sky", "Pro"], "@", "Sky@Pro")
])
def test_list_to_string(lst, joiner, result):
    assert su.list_to_string(lst, joiner) == result
