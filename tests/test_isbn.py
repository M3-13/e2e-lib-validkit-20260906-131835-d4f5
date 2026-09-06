import pytest

from validkit.isbn import is_valid_isbn13


def test_valid_isbn13_with_separators():
    assert is_valid_isbn13("978-3-16-148410-0") is True


def test_valid_isbn13_plain_digits():
    assert is_valid_isbn13("9783161484100") is True


def test_valid_isbn13_with_spaces():
    assert is_valid_isbn13("978 3 16 148410 0") is True


def test_valid_isbn13_979_prefix():
    assert is_valid_isbn13("979-10-90636-07-1") is True


def test_invalid_check_digit():
    assert is_valid_isbn13("978-3-16-148410-1") is False


def test_too_short():
    assert is_valid_isbn13("978-3-16-148410") is False


def test_too_long():
    assert is_valid_isbn13("978-3-16-148410-00") is False


def test_empty_string():
    assert is_valid_isbn13("") is False


def test_non_digit_character():
    assert is_valid_isbn13("978-3-16-14841X-0") is False


def test_only_separators():
    assert is_valid_isbn13("--- --- --- --") is False


def test_non_string_int():
    with pytest.raises(TypeError):
        is_valid_isbn13(9783161484100)


def test_non_string_none():
    with pytest.raises(TypeError):
        is_valid_isbn13(None)
