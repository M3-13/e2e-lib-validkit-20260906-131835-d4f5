"""Tests for validkit.iban."""

import pytest

from validkit.iban import is_valid_iban


def test_valid_german_iban_with_spaces() -> None:
    assert is_valid_iban("DE89 3704 0044 0532 0130 00") is True


def test_valid_german_iban_without_spaces() -> None:
    assert is_valid_iban("DE89370400440532013000") is True


def test_changed_check_digit_is_false() -> None:
    assert is_valid_iban("DE88 3704 0044 0532 0130 00") is False


def test_changed_account_part_is_false() -> None:
    assert is_valid_iban("DE89 3704 0044 0532 0130 01") is False


def test_lowercase_country_code_is_false() -> None:
    assert is_valid_iban("de89 3704 0044 0532 0130 00") is False


def test_invalid_characters_are_false() -> None:
    assert is_valid_iban("DE89 3704 0044 0532 0130 0!") is False


def test_too_short_iban_is_false() -> None:
    assert is_valid_iban("DE89") is False


def test_too_long_iban_is_false() -> None:
    assert is_valid_iban("DE89" + "0" * 40) is False


def test_country_length_mismatch_is_false() -> None:
    assert is_valid_iban("DE89 3704 0044 0532 0130 0000") is False


def test_no_country_letters_is_false() -> None:
    assert is_valid_iban("1289 3704 0044 0532 0130 00") is False


def test_empty_string_is_false() -> None:
    assert is_valid_iban("") is False


def test_whitespace_only_is_false() -> None:
    assert is_valid_iban("   ") is False


def test_non_string_raises_type_error() -> None:
    with pytest.raises(TypeError):
        is_valid_iban(1234567890)  # type: ignore[arg-type]


def test_none_raises_type_error() -> None:
    with pytest.raises(TypeError):
        is_valid_iban(None)  # type: ignore[arg-type]
