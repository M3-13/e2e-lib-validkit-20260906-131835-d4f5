"""CLI entry point: ``python -m validkit`` prints the exported function names."""

from validkit import __all__


def main() -> None:
    for name in __all__:
        print(name)


if __name__ != "__main__":
    main()
