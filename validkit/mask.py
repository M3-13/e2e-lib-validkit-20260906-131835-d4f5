def mask_secret(text: str, keep: int = 4) -> str:
    if not isinstance(text, str):
        raise TypeError(f"mask_secret: 'text' must be a string, got {type(text).__name__}")
    if not isinstance(keep, int) or isinstance(keep, bool):
        raise TypeError(f"mask_secret: 'keep' must be an integer, got {type(keep).__name__}")
    if keep < 0:
        raise ValueError(f"mask_secret: 'keep' must be non-negative, got {keep}")
    return text[:keep] + "*" * (len(text) - keep)
