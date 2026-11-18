"""Offline entrypoint for the 18 November 2026 World Desk front page."""

from os import environ
from pathlib import Path


def main() -> None:
    """Write the pre-rendered editorial PNG without any runtime dependencies."""
    image = Path(__file__).with_name("frontpage.png").read_bytes()
    output = Path(environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output.mkdir(parents=True, exist_ok=True)
    if not image.startswith(b"\x89PNG\r\n\x1a\n") or len(image) > 1_048_576:
        raise ValueError("The bundled front page must be a PNG under 1 MiB")
    (output / "entry.png").write_bytes(image)


if __name__ == "__main__":
    main()
