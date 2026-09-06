# validkit

Eine kleine, eigenständige Python-Bibliothek (nur Standardbibliothek) mit neun
unabhängigen Prüf- und Normalisierungsfunktionen: E-Mail-Validierung,
Luhn-Prüfung, IBAN- und ISBN-13-Validierung, Telefonnummer-Normalisierung,
Akzent-Entfernung, Secret-Maskierung, Slug-Erzeugung und Clamping.

## Tech Stack

- Python 3.10+
- Build: `pyproject.toml` (setuptools)
- Tests: pytest
- Abhängigkeiten: keine (nur Standardbibliothek)

## Installation

```bash
pip install -e .
```

## Nutzung

```python
from validkit import is_valid_email, luhn_check, is_valid_iban, is_valid_isbn13
from validkit import normalize_phone, strip_accents, mask_secret, slugify, clamp
```

## Beispiele

```python
is_valid_email("test@example.com")  # → True
luhn_check("79927398713")  # → True
is_valid_iban("DE89 3704 0044 0532 0130 00")  # → True
is_valid_isbn13("978-3-16-148410-0")  # → True
normalize_phone("0176 12345678", "DE")  # → '+4917612345678'
strip_accents("crème brûlée")  # → 'creme brulee'
mask_secret("geheim123", 4)  # → 'gehe*****'
slugify("Héllo Wörld!")  # → 'hello-world'
clamp(5, 0, 10)  # → 5
```

## Entwicklung

```bash
python -m validkit   # gibt die neun Funktionsnamen aus
pytest -q            # führt die Tests aus
```

## Funktionen

| Funktion | Beschreibung |
| --- | --- |
| `is_valid_email(text)` | Prüft eine E-Mail-Adresse |
| `luhn_check(digits)` | Prüft eine Ziffernfolge per Luhn-Algorithmus |
| `is_valid_iban(text)` | Prüft eine IBAN |
| `is_valid_isbn13(text)` | Prüft eine ISBN-13 |
| `normalize_phone(text, country_code)` | Normalisiert eine Telefonnummer |
| `strip_accents(text)` | Entfernt Akzente aus Text |
| `mask_secret(text, keep)` | Maskiert ein Secret bis auf `keep` Zeichen |
| `slugify(text)` | Erzeugt einen URL-freundlichen Slug |
| `clamp(value, low, high)` | Begrenzt einen Wert auf ein Intervall |
