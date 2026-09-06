import pytest

from validkit.mask import mask_secret


def test_masks_all_but_first_keep_chars() -> None:
    assert mask_secret("geheim123", 4) == "gehe*****"


def test_keep_larger_than_length_masks_nothing() -> None:
    assert mask_secret("abc", 5) == "abc"


def test_keep_equal_to_length_masks_nothing() -> None:
    assert mask_secret("abc", 3) == "abc"


def test_keep_zero_masks_everything() -> None:
    assert mask_secret("geheim123", 0) == "*********"


def test_empty_text_returns_empty() -> None:
    assert mask_secret("", 4) == ""


def test_negative_keep_raises_value_error() -> None:
    with pytest.raises(ValueError):
        mask_secret("geheim123", -1)


def test_non_string_raises_type_error() -> None:
    with pytest.raises(TypeError):
        mask_secret(123)  # type: ignore[arg-type]


def test_non_integer_keep_raises_type_error() -> None:
    with pytest.raises(TypeError):
        mask_secret("geheim123", "4")  # type: ignore[arg-type]
