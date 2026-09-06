import unicodedata


def slugify(text: str) -> str:
    if not isinstance(text, str):
        raise TypeError(f"slugify() erwartet einen String, erhielt {type(text).__name__}")

    normalized = unicodedata.normalize("NFKD", text)
    ascii_text = "".join(c for c in normalized if not unicodedata.combining(c))
    lowered = ascii_text.lower()

    parts = []
    for ch in lowered:
        if ch.isalnum():
            parts.append(ch)
        else:
            parts.append("-")
    joined = "".join(parts)

    slug = "-".join(segment for segment in joined.split("-") if segment)
    return slug
