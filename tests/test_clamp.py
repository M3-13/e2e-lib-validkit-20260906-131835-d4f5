import pytest

from validkit.clamp import clamp


def test_value_within_range_unchanged() -> None:
    assert clamp(5, 0, 10) == 5
    assert clamp(5.0, 0.0, 10.0) == 5.0


def test_value_below_low_clamps_to_low() -> None:
    assert clamp(-1, 0, 10) == 0
    assert clamp(-100.5, -50.0, 50.0) == -50.0


def test_value_above_high_clamps_to_high() -> None:
    assert clamp(99, 0, 10) == 10
    assert clamp(1000, 0.0, 100.0) == 100.0


def test_value_equal_to_boundaries() -> None:
    assert clamp(0, 0, 10) == 0
    assert clamp(10, 0, 10) == 10
    assert clamp(0.0, 0.0, 10.0) == 0.0
    assert clamp(10.0, 0.0, 10.0) == 10.0


def test_low_greater_than_high_raises_value_error() -> None:
    with pytest.raises(ValueError, match="low <= high"):
        clamp(1, 5, 0)


def test_low_equal_to_high_returns_that_value() -> None:
    assert clamp(5, 7, 7) == 7
    assert clamp(9, 7, 7) == 7


def test_non_numeric_value_raises_type_error() -> None:
    with pytest.raises(TypeError, match="value"):
        clamp("5", 0, 10)
    with pytest.raises(TypeError, match="value"):
        clamp(None, 0, 10)


def test_non_numeric_low_raises_type_error() -> None:
    with pytest.raises(TypeError, match="low"):
        clamp(5, "0", 10)


def test_non_numeric_high_raises_type_error() -> None:
    with pytest.raises(TypeError, match="high"):
        clamp(5, 0, "10")


def test_bool_rejected_as_not_a_number() -> None:
    with pytest.raises(TypeError):
        clamp(True, 0, 10)
