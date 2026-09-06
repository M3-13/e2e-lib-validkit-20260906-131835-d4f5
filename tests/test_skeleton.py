import inspect
import io
from contextlib import redirect_stdout

import validkit
from validkit.__main__ import main

EXPECTED = {
    "is_valid_email": "(text: str) -> bool",
    "luhn_check": "(digits: str) -> bool",
    "is_valid_iban": "(text: str) -> bool",
    "is_valid_isbn13": "(text: str) -> bool",
    "normalize_phone": "(text: str, country_code: str) -> str",
    "strip_accents": "(text: str) -> str",
    "mask_secret": "(text: str, keep: int = 4) -> str",
    "slugify": "(text: str) -> str",
    "clamp": "(value: float, low: float, high: float) -> float",
}


def test_all_nine_names_exported() -> None:
    assert set(validkit.__all__) == set(EXPECTED)


def test_all_nine_names_importable_and_callable() -> None:
    for name in EXPECTED:
        obj = getattr(validkit, name)
        assert callable(obj), f"{name} is not callable"


def test_signatures_match_contract() -> None:
    for name, expected_sig in EXPECTED.items():
        obj = getattr(validkit, name)
        actual_sig = str(inspect.signature(obj))
        assert actual_sig == expected_sig, f"{name}: expected {expected_sig}, got {actual_sig}"


def test_cli_prints_nine_names() -> None:
    buf = io.StringIO()
    with redirect_stdout(buf):
        main()
    lines = buf.getvalue().splitlines()
    assert len(lines) == len(EXPECTED)
    assert set(lines) == set(EXPECTED)
