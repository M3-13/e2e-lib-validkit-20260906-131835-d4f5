import pytest

from validkit.accents import strip_accents


def test_strip_accents_normal_case() -> None:
    assert strip_accents("crème brûlée") == "creme brulee"


def test_strip_accents_various_accents() -> None:
    assert strip_accents("áéíóú ñ") == "aeiou n"
    assert strip_accents("Ångström") == "Angstrom"


def test_strip_accents_no_accents_unchanged() -> None:
    assert strip_accents("hello world") == "hello world"
    assert strip_accents("123") == "123"


def test_strip_accents_empty_string() -> None:
    assert strip_accents("") == ""


def test_strip_accents_non_string_raises_typeerror() -> None:
    for value in (None, 42, 3.14, ["crème"], b"caf\xc3\xa9"):
        with pytest.raises(TypeError):
            strip_accents(value)


def test_strip_accents_typeerror_message_names_function() -> None:
    with pytest.raises(TypeError) as excinfo:
        strip_accents(42)
    assert "strip_accents" in str(excinfo.value)
