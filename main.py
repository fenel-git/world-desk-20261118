"""Publish the offline World Desk raster after checking its complete RGB payload."""

import os
from pathlib import Path
from struct import Struct
from tempfile import NamedTemporaryFile
import zlib

PNG_MAGIC = bytes.fromhex('89504e470d0a1a0a')
SIDE = 1024
BYTE_LIMIT = 1 << 20
ROW_BYTES = 1 + SIDE * 3  # Filter selector followed by RGB triples.
CHUNK_HEADER = Struct('>I4s')
UINT = Struct('>I')
RGB_HEADER = Struct('>IIBBBBB').pack(SIDE, SIDE, 8, 2, 0, 0, 0)


def png_records(image):
    """Yield verified chunk name and data as views rather than copying each record."""
    if len(image) > BYTE_LIMIT or not image.startswith(PNG_MAGIC):
        raise ValueError('Expected a PNG of at most 1 MiB')
    view = memoryview(image)
    cursor = len(PNG_MAGIC)
    while cursor < len(view):
        if len(view) - cursor < 12:
            raise ValueError('Incomplete PNG chunk framing')
        count, name = CHUNK_HEADER.unpack_from(view, cursor)
        end = cursor + CHUNK_HEADER.size + count
        if end + UINT.size > len(view):
            raise ValueError('Incomplete PNG chunk data')
        if zlib.crc32(view[cursor + UINT.size:end]) != UINT.unpack_from(view, end)[0]:
            raise ValueError(f'Bad checksum for {name!r}')
        payload = view[cursor + CHUNK_HEADER.size:end]
        cursor = end + UINT.size
        if name == b'IEND' and (payload or cursor != len(view)):
            raise ValueError('IEND must be empty and end the image')
        yield name, payload


def check_scanlines(compressed):
    expected = ROW_BYTES * SIDE
    inflater = zlib.decompressobj()
    try:
        scanlines = inflater.decompress(compressed, expected + 1)
    except zlib.error as error:
        raise ValueError('Corrupt PNG pixel stream') from error
    if len(scanlines) != expected or not inflater.eof or inflater.unused_data:
        raise ValueError('PNG pixel stream does not match its header')
    if max(scanlines[::ROW_BYTES]) > 4:
        raise ValueError('Invalid PNG row filter')


def inspect_frontpage(image):
    """Accept the raster profile emitted by the frontpage export, not arbitrary PNGs."""
    records = iter(png_records(image))
    if next(records, None) != (b'IHDR', RGB_HEADER):
        raise ValueError('Expected 1024×1024, eight-bit RGB, non-interlaced')
    compressed = bytearray()
    data_closed = False
    for name, payload in records:
        if name == b'IEND':
            if not compressed:
                raise ValueError('PNG has no pixel data')
            check_scanlines(compressed)
            return
        if name == b'IDAT':
            if data_closed:
                raise ValueError('Image data chunks must be adjacent')
            compressed.extend(payload)
        elif name in (b'sRGB', b'gAMA', b'cHRM', b'pHYs', b'iCCP', b'sBIT'):
            if compressed and name != b'pHYs':
                raise ValueError('Color metadata must precede pixel data')
            data_closed |= bool(compressed)
        else:
            raise ValueError(f'Unexpected frontpage chunk: {name!r}')
    raise ValueError('PNG has no end marker')


def publish(image, directory):
    """Install a validated complete file without leaving a partial final artifact."""
    inspect_frontpage(image)
    directory.mkdir(parents=True, exist_ok=True)
    target = directory / 'entry.png'
    with NamedTemporaryFile(dir=directory, prefix='.frontpage-', delete=False) as spool:
        staged = Path(spool.name)
        try:
            spool.write(image)
            spool.close()
            staged.replace(target)
        finally:
            staged.unlink(missing_ok=True)
    return target


def main():
    repository = Path(__file__).resolve().parent
    with (repository / 'frontpage.png').open('rb') as source:
        image = source.read(BYTE_LIMIT + 1)
    publish(image, Path(os.environ.get('MAKEFUN_OUTPUT_DIR', '/output')))


if __name__ == '__main__':
    main()
