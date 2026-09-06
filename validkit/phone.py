import re

_COUNTRY_CODES = {
    "DE": "+49",
    "AT": "+43",
    "CH": "+41",
}


def normalize_phone(text: str, country_code: str) -> str:
    if not isinstance(text, str):
        raise TypeError("normalize_phone: 'text' must be a string")
    if not isinstance(country_code, str):
        raise TypeError("normalize_phone: 'country_code' must be a string")

    prefix = _COUNTRY_CODES.get(country_code.strip().upper())
    if prefix is None:
        raise ValueError(f"normalize_phone: unsupported country code '{country_code}'")

    cleaned = text.strip()
    if not cleaned:
        raise ValueError("normalize_phone: cannot normalize an empty phone number")

    digits = re.sub(r"\D", "", cleaned)
    if not digits:
        raise ValueError("normalize_phone: phone number contains no digits")

    if cleaned.startswith("+"):
        return "+" + digits
    if cleaned.startswith("00"):
        rest = digits[2:]
        if not rest or not rest.lstrip("0"):
            raise ValueError("normalize_phone: phone number has no meaningful digits")
        return "+" + rest

    country_digits = prefix[1:]
    if digits.startswith(country_digits):
        return "+" + digits

    national = digits.lstrip("0")
    if not national:
        raise ValueError("normalize_phone: phone number has no meaningful digits")

    return prefix + national
