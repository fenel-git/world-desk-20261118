import unittest
from pathlib import Path
from zlib import crc32

import main


class TestPngValidation(unittest.TestCase):
    def setUp(self):
        self.image = Path(__file__).with_name("frontpage.png").read_bytes()

    def test_accepts_the_complete_rendered_front_page(self):
        main.validate_png(self.image)

    def test_rejects_a_corrupt_image_chunk(self):
        damaged = bytearray(self.image)
        offset = 8
        while damaged[offset + 4:offset + 8] != b"IDAT":
            offset += 12 + int.from_bytes(damaged[offset:offset + 4], "big")
        damaged[offset + 8] ^= 1
        with self.assertRaisesRegex(ValueError, "checksum"):
            main.validate_png(bytes(damaged))

    def test_rejects_a_bit_depth_not_allowed_for_the_colour_type(self):
        damaged = bytearray(self.image)
        header = bytearray(damaged[16:29])
        header[8] = 1
        damaged[16:29] = header
        damaged[29:33] = crc32(b"IHDR" + header).to_bytes(4, "big")
        with self.assertRaisesRegex(ValueError, "bit depth"):
            main.validate_png(bytes(damaged))

    def test_rejects_data_after_the_image_end_marker(self):
        with self.assertRaisesRegex(ValueError, "trailing"):
            main.validate_png(self.image + b"extra")


if __name__ == "__main__":
    unittest.main()
