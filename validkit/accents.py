import unicodedata


def strip_accents(text: str) -> str:
    if not isinstance(text, str):
        raise TypeError(f"strip_accents() expected a string, got {type(text).__name__}")

    normalized = unicodedata.normalize("NFKD", text)
    return "".join(ch for ch in normalized if not unicodedata.combining(ch))
