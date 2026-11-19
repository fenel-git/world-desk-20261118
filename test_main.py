import os
from pathlib import Path
import shutil
import struct
import subprocess
import sys
import tempfile
import unittest
import zlib


class SandboxEntry(unittest.TestCase):
    def test_rejects_crc_correct_but_undecodable_image(self):
        root = Path(__file__).resolve().parent
        with tempfile.TemporaryDirectory() as directory:
            sandbox = Path(directory)
            shutil.copyfile(root / 'main.py', sandbox / 'main.py')
            def chunk(tag, data):
                return (struct.pack('>I', len(data)) + tag + data
                        + struct.pack('>I', zlib.crc32(tag + data)))

            header = struct.pack('>IIBBBBB', 1024, 1024, 8, 2, 0, 0, 0)
            (sandbox / 'frontpage.png').write_bytes(
                b'\x89PNG\r\n\x1a\n' + chunk(b'IHDR', header)
                + chunk(b'IDAT', zlib.compress(b'not enough scanlines'))
                + chunk(b'IEND', b''))
            output = sandbox / 'output'
            run = subprocess.run(
                [sys.executable, '-P', '-s', str(sandbox / 'main.py')],
                env={**os.environ, 'MAKEFUN_OUTPUT_DIR': str(output)},
                capture_output=True,
            )
            self.assertNotEqual(run.returncode, 0)
            self.assertFalse((output / 'entry.png').exists())
