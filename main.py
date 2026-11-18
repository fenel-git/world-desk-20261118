"""Offline entrypoint for the 18 November 2026 World Desk front page."""

from os import environ
from pathlib import Path
from struct import unpack


def main() -> None:
    """Write the pre-rendered editorial PNG without any runtime dependencies."""
    image = Path(__file__).with_name("frontpage.png").read_bytes()
    output = Path(environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output.mkdir(parents=True, exist_ok=True)
    if not image.startswith(b"\x89PNG\r\n\x1a\n") or len(image) > 1_048_576:
        raise ValueError("The bundled front page must be a PNG under 1 MiB")
    if image[12:16] != b"IHDR" or len(image) < 33:
        raise ValueError("The bundled front page needs a complete PNG header")
    if unpack(">II", image[16:24]) != (1024, 1024):
        raise ValueError("The bundled front page must be exactly 1024 by 1024")
    (output / "entry.png").write_bytes(image)


if __name__ == "__main__":
    main()
