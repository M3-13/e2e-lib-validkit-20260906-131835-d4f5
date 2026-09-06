import numbers


def _check_number(name: str, arg: float) -> None:
    if isinstance(arg, bool) or not isinstance(arg, numbers.Real):
        raise TypeError(f"clamp() expected '{name}' to be a number, got {type(arg).__name__}")


def clamp(value: float, low: float, high: float) -> float:
    _check_number("value", value)
    _check_number("low", low)
    _check_number("high", high)
    if low > high:
        raise ValueError(f"clamp() requires low <= high, got low={low} and high={high}")
    return min(max(value, low), high)
