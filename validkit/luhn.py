def luhn_check(digits: str) -> bool:
    if not isinstance(digits, str):
        raise TypeError(f"luhn_check: expected a string of digits, got {type(digits).__name__}")

    digits = digits.replace(" ", "")

    if not digits:
        raise ValueError("luhn_check: input has no digits")

    if not digits.isdigit():
        raise ValueError("luhn_check: input contains non-digit characters")

    total = 0
    for i, ch in enumerate(reversed(digits)):
        value = int(ch)
        if i % 2 == 1:
            value *= 2
            if value > 9:
                value -= 9
        total += value

    return total % 10 == 0
