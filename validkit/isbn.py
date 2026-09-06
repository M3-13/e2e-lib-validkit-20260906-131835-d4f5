def is_valid_isbn13(text: str) -> bool:
    """Return True if *text* is a valid ISBN-13.

    Hyphens and spaces are tolerated as separators; every other character
    must be a digit and there must be exactly 13 of them. The last digit is
    validated as the check digit.
    """
    if not isinstance(text, str):
        raise TypeError(f"is_valid_isbn13: expected a string, got {type(text).__name__}")

    cleaned = text.replace("-", "").replace(" ", "")

    if len(cleaned) != 13 or not cleaned.isdigit():
        return False

    total = 0
    for i, digit in enumerate(cleaned[:-1]):
        weight = 1 if i % 2 == 0 else 3
        total += int(digit) * weight

    check = (10 - total % 10) % 10

    return check == int(cleaned[-1])
