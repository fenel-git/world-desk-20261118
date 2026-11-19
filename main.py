"""Offline entrypoint for the 18 November 2026 World Desk front page."""

from os import environ
from pathlib import Path
from struct import unpack
from zlib import crc32


PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
MAX_IMAGE_BYTES = 1_048_576


def validate_png(image: bytes) -> None:
    """Reject incomplete, corrupt, oversized, or incorrectly sized PNGs."""
    if len(image) < 33 or not image.startswith(PNG_SIGNATURE):
        raise ValueError("The bundled front page must be a complete PNG")
    if len(image) > MAX_IMAGE_BYTES:
        raise ValueError("The bundled front page must be a PNG under 1 MiB")

    offset = len(PNG_SIGNATURE)
    has_header = False
    has_data = False
    data_closed = False
    while offset < len(image):
        if len(image) - offset < 12:
            raise ValueError("The PNG has a truncated chunk header")
        length = unpack(">I", image[offset:offset + 4])[0]
        end = offset + 12 + length
        if end > len(image):
            raise ValueError("The PNG has a truncated chunk")
        kind = image[offset + 4:offset + 8]
        data = image[offset + 8:offset + 8 + length]
        checksum = unpack(">I", image[offset + 8 + length:end])[0]
        if crc32(kind + data) & 0xFFFFFFFF != checksum:
            raise ValueError("The PNG chunk checksum is invalid")

        if not has_header:
            if kind != b"IHDR" or length != 13:
                raise ValueError("The PNG must start with one complete IHDR chunk")
            width, height = unpack(">II", data[:8])
            bit_depth, color_type, compression, filter_method, interlace = data[8:13]
            valid_depths = {
                0: {1, 2, 4, 8, 16},
                2: {8, 16},
                3: {1, 2, 4, 8},
                4: {8, 16},
                6: {8, 16},
            }
            if color_type not in valid_depths or bit_depth not in valid_depths[color_type]:
                raise ValueError("The PNG bit depth is invalid for its color type")
            if compression != 0 or filter_method != 0 or interlace not in (0, 1):
                raise ValueError("The PNG uses an unsupported IHDR method")
            if (width, height) != (1024, 1024):
                raise ValueError("The bundled front page must be exactly 1024 by 1024")
            has_header = True
        elif kind == b"IHDR":
            raise ValueError("The PNG must contain only one IHDR chunk")

        if kind == b"IDAT":
            if data_closed:
                raise ValueError("The PNG image data chunks must be consecutive")
            has_data = True
        elif has_data and kind != b"IEND":
            data_closed = True

        offset = end
        if kind == b"IEND":
            if length != 0 or not has_data:
                raise ValueError("The PNG needs image data and a valid IEND chunk")
            if offset != len(image):
                raise ValueError("The PNG contains trailing data after IEND")
            return

    raise ValueError("The PNG is missing its IEND chunk")


def main() -> None:
    """Write the pre-rendered editorial PNG without any runtime dependencies."""
    image = Path(__file__).with_name("frontpage.png").read_bytes()
    output = Path(environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output.mkdir(parents=True, exist_ok=True)
    if not image.startswith(b"\x89PNG\r\n\x1a\n") or len(image) > 1_048_576:
        raise ValueError("The bundled front page must be a PNG under 1 MiB")
    if image[12:16] != b"IHDR" or len(image) < 33:
        raise ValueError("The bundled front page needs a complete PNG header")
    validate_png(image)
    (output / "entry.png").write_bytes(image)


if __name__ == "__main__":
    main()
