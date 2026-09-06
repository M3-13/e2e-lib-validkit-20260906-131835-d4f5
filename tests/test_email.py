import pytest

from validkit.email import is_valid_email


def test_valid_email_returns_true() -> None:
    assert is_valid_email("test@example.com") is True


def test_valid_email_with_subdomain() -> None:
    assert is_valid_email("user@mail.example.com") is True


def test_invalid_email_without_at() -> None:
    assert is_valid_email("nicht-gültig") is False


def test_invalid_email_missing_local_part() -> None:
    assert is_valid_email("@example.com") is False


def test_invalid_email_missing_domain_dot() -> None:
    assert is_valid_email("test@localhost") is False


def test_invalid_email_multiple_at() -> None:
    assert is_valid_email("a@b@c.com") is False


def test_invalid_email_empty_string() -> None:
    assert is_valid_email("") is False


def test_invalid_email_domain_starts_with_dot() -> None:
    assert is_valid_email("test@.example.com") is False


def test_non_string_raises_type_error() -> None:
    with pytest.raises(TypeError):
        is_valid_email(123)  # type: ignore[arg-type]


def test_non_string_error_message_names_function() -> None:
    with pytest.raises(TypeError, match="is_valid_email"):
        is_valid_email(None)  # type: ignore[arg-type]
