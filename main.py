"""R4 entry: validate and copy the deterministic 1024px World Desk image."""
from os import environ
from pathlib import Path
from struct import unpack
from zlib import crc32

SIGNATURE = b"\x89PNG\r\n\x1a\n"
EXPECTED_SIZE = (1024, 1024)
MAX_BYTES = 1_048_576


def read_chunk(blob: bytes, start: int):
    """Return (tag, payload, next_position), rejecting damaged chunks."""
    if start + 12 > len(blob):
        raise ValueError("truncated PNG chunk header")
    length = unpack(">I", blob[start:start + 4])[0]
    finish = start + 12 + length
    if finish > len(blob):
        raise ValueError("truncated PNG chunk payload")
    tag = blob[start + 4:start + 8]
    payload = blob[start + 8:start + 8 + length]
    checksum = unpack(">I", blob[start + 8 + length:finish])[0]
    if crc32(tag + payload) & 0xffffffff != checksum:
        raise ValueError("PNG checksum mismatch")
    return tag, payload, finish


def validate_png(blob: bytes) -> None:
    """Check dimensions, legal color depth, ordered data, and exact termination."""
    if not blob.startswith(SIGNATURE):
        raise ValueError("frontpage.png is not a PNG")
    if len(blob) > MAX_BYTES:
        raise ValueError("frontpage.png exceeds the one MiB limit")
    position = len(SIGNATURE)
    header = False
    saw_data = False
    closed_data = False
    while position < len(blob):
        tag, payload, position = read_chunk(blob, position)
        if not header:
            if tag != b"IHDR" or len(payload) != 13:
                raise ValueError("PNG must start with a single IHDR")
            width, height = unpack(">II", payload[:8])
            depth, color, compression, filtering, interlace = payload[8:13]
            depths = {0: {1, 2, 4, 8, 16}, 2: {8, 16}, 3: {1, 2, 4, 8}, 4: {8, 16}, 6: {8, 16}}
            if (width, height) != EXPECTED_SIZE:
                raise ValueError("frontpage.png must be 1024 by 1024")
            if color not in depths or depth not in depths[color]:
                raise ValueError("PNG bit depth is illegal for its color type")
            if (compression, filtering) != (0, 0) or interlace not in (0, 1):
                raise ValueError("PNG header method is unsupported")
            header = True
        elif tag == b"IHDR":
            raise ValueError("PNG has duplicate IHDR")
        if tag == b"IDAT":
            if closed_data:
                raise ValueError("PNG IDAT chunks must be consecutive")
            saw_data = True
        elif saw_data and tag != b"IEND":
            closed_data = True
        if tag == b"IEND":
            if payload or not saw_data or position != len(blob):
                raise ValueError("PNG has an invalid or trailing IEND")
            return
    raise ValueError("PNG is missing IEND")


def render(output_root: Path) -> Path:
    """Copy the checked-in render to the sandbox output path."""
    source = Path(__file__).with_name("frontpage.png")
    image = source.read_bytes()
    validate_png(image)
    output_root.mkdir(parents=True, exist_ok=True)
    target = output_root / "entry.png"
    target.write_bytes(image)
    return target


def main() -> None:
    destination = Path(environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    render(destination)


if __name__ == "__main__":
    main()
