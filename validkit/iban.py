"""IBAN validation."""

import re

_IBAN_PATTERN = re.compile(r"^[A-Z]{2}[0-9]{2}[A-Z0-9]{11,30}$")

# ISO 3166-1 country code -> expected total IBAN length (incl. country + checksum).
_COUNTRY_LENGTHS: dict[str, int] = {
    "AD": 24,
    "AE": 23,
    "AL": 28,
    "AT": 20,
    "AZ": 28,
    "BA": 20,
    "BE": 16,
    "BG": 22,
    "BH": 22,
    "BR": 29,
    "BY": 28,
    "CH": 21,
    "CR": 22,
    "CY": 28,
    "CZ": 24,
    "DE": 22,
    "DK": 18,
    "DO": 28,
    "EE": 20,
    "EG": 29,
    "ES": 24,
    "FI": 18,
    "FO": 18,
    "FR": 27,
    "GB": 22,
    "GE": 22,
    "GI": 23,
    "GL": 18,
    "GR": 27,
    "GT": 28,
    "HR": 21,
    "HU": 28,
    "IE": 22,
    "IL": 23,
    "IQ": 23,
    "IS": 26,
    "IT": 27,
    "JO": 30,
    "KW": 30,
    "KZ": 20,
    "LB": 28,
    "LC": 32,
    "LI": 21,
    "LT": 20,
    "LU": 20,
    "LV": 21,
    "MC": 27,
    "MD": 24,
    "ME": 22,
    "MK": 19,
    "MR": 27,
    "MT": 31,
    "MU": 30,
    "NL": 18,
    "NO": 15,
    "PK": 24,
    "PL": 28,
    "PS": 29,
    "PT": 25,
    "QA": 29,
    "RO": 24,
    "RS": 22,
    "SA": 24,
    "SC": 31,
    "SE": 24,
    "SI": 19,
    "SK": 24,
    "SM": 27,
    "ST": 25,
    "SV": 28,
    "TL": 23,
    "TN": 24,
    "TR": 26,
    "UA": 29,
    "VA": 22,
    "VG": 24,
    "XK": 20,
}


def _to_numeric(iban: str) -> str:
    """Map A-Z to 10-35 and concatenate the digits of the rearranged IBAN."""
    rearranged = iban[4:] + iban[:4]
    return "".join(str(ord(ch) - 55) if ch.isalpha() else ch for ch in rearranged)


def is_valid_iban(text: str) -> bool:
    if not isinstance(text, str):
        raise TypeError(f"is_valid_iban: expected a string, got {type(text).__name__}")

    cleaned = "".join(text.split())

    if not _IBAN_PATTERN.match(cleaned):
        return False

    country = cleaned[:2]
    expected = _COUNTRY_LENGTHS.get(country)
    if expected is not None and len(cleaned) != expected:
        return False

    return int(_to_numeric(cleaned)) % 97 == 1
