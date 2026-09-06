import pytest

from validkit import normalize_phone


def test_normalize_phone_basic() -> None:
    assert normalize_phone("0176 12345678", "DE") == "+4917612345678"


def test_normalize_phone_with_special_characters() -> None:
    assert normalize_phone("(0176) 123-456 78", "DE") == "+4917612345678"
    assert normalize_phone("0176/123456.78", "DE") == "+4917612345678"


def test_normalize_phone_already_international_plus() -> None:
    assert normalize_phone("+49 176 12345678", "DE") == "+4917612345678"


def test_normalize_phone_already_international_double_zero() -> None:
    assert normalize_phone("0049 176 12345678", "DE") == "+4917612345678"


def test_normalize_phone_already_has_country_code_digits() -> None:
    assert normalize_phone("49 176 12345678", "DE") == "+4917612345678"


def test_normalize_phone_other_country() -> None:
    assert normalize_phone("0664 1234567", "AT") == "+436641234567"


def test_normalize_phone_trims_whitespace() -> None:
    assert normalize_phone("  0176 12345678  ", "DE") == "+4917612345678"


def test_normalize_phone_empty_text_raises_value_error() -> None:
    with pytest.raises(ValueError):
        normalize_phone("", "DE")


def test_normalize_phone_whitespace_only_raises_value_error() -> None:
    with pytest.raises(ValueError):
        normalize_phone("   ", "DE")


def test_normalize_phone_no_digits_raises_value_error() -> None:
    with pytest.raises(ValueError):
        normalize_phone("(keine Nummer)", "DE")


def test_normalize_phone_only_double_zero_raises_value_error() -> None:
    with pytest.raises(ValueError):
        normalize_phone("00", "DE")


def test_normalize_phone_triple_zero_raises_value_error() -> None:
    with pytest.raises(ValueError):
        normalize_phone("000", "DE")


def test_normalize_phone_many_zeros_raises_value_error() -> None:
    with pytest.raises(ValueError):
        normalize_phone("0000000", "DE")


def test_normalize_phone_unsupported_country_raises_value_error() -> None:
    with pytest.raises(ValueError):
        normalize_phone("0176 12345678", "XX")


def test_normalize_phone_non_string_text_raises_type_error() -> None:
    with pytest.raises(TypeError):
        normalize_phone(17612345678, "DE")


def test_normalize_phone_non_string_country_raises_type_error() -> None:
    with pytest.raises(TypeError):
        normalize_phone("0176 12345678", 49)
