def is_valid_email(text: str) -> bool:
    if not isinstance(text, str):
        raise TypeError("is_valid_email() expects a str, got " + type(text).__name__)

    if text.count("@") != 1:
        return False

    local, domain = text.split("@")
    if not local:
        return False

    if "." not in domain:
        return False

    if domain.startswith(".") or domain.endswith("."):
        return False

    return ".." not in domain
