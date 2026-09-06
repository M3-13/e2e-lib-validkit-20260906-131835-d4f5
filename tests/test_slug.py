import pytest

from validkit.slug import slugify


def test_slugify_normal():
    assert slugify("Héllo Wörld!") == "hello-world"


def test_slugify_basic_words():
    assert slugify("Hello World") == "hello-world"


def test_slugify_special_characters():
    assert slugify("Foo @ Bar # Baz") == "foo-bar-baz"


def test_slugify_multiple_hyphens_collapsed():
    assert slugify("a   b---c") == "a-b-c"


def test_slugify_leading_and_trailing_hyphens():
    assert slugify("  --Hello World--  ") == "hello-world"


def test_slugify_accents_and_umlauts():
    assert slugify("crème brûlée") == "creme-brulee"


def test_slugify_digits_and_mixed():
    assert slugify("Artikel 42 ist da!") == "artikel-42-ist-da"


def test_slugify_empty_string():
    assert slugify("") == ""


def test_slugify_only_special_characters():
    assert slugify("!!! --- ???") == ""


def test_slugify_non_string_raises_type_error():
    with pytest.raises(TypeError):
        slugify(123)


def test_slugify_none_raises_type_error():
    with pytest.raises(TypeError):
        slugify(None)
