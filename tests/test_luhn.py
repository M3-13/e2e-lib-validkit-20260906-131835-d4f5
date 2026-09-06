import pytest

from validkit import luhn_check


def test_valid_number_returns_true() -> None:
    assert luhn_check("79927398713") is True


def test_changed_digit_returns_false() -> None:
    assert luhn_check("79927398714") is False


def test_spaces_are_removed() -> None:
    assert luhn_check("7992 7398 713") is True


def test_non_digit_raises_value_error() -> None:
    with pytest.raises(ValueError):
        luhn_check("7992739871X")


def test_empty_string_raises_value_error() -> None:
    with pytest.raises(ValueError):
        luhn_check("")


def test_whitespace_only_raises_value_error() -> None:
    with pytest.raises(ValueError):
        luhn_check("   ")


def test_non_string_raises_type_error() -> None:
    with pytest.raises(TypeError):
        luhn_check(79927398713)  # type: ignore[arg-type]


def test_single_digit() -> None:
    assert luhn_check("0") is True
    assert luhn_check("1") is False
