# Copyright 2026 Yusuf Kaya and Jan Moser
# SPDX-License-Identifier: Apache-2.0
import random
import unittest

from dawn_codec import FORMATS, N, decode, encode, enumerative_decode, enumerative_encode


class TestCodec(unittest.TestCase):
    def test_roundtrips_and_boundaries(self):
        random.seed(20260927)
        for name, fmt in FORMATS.items():
            with self.subTest(name=name):
                vectors = [[0] * N, [fmt.alphabet - 1] * N]
                vectors += [[random.randrange(fmt.alphabet) for _ in range(N)] for _ in range(20)]
                for pos in (0, 1, 6, 7, 16, 17, 509, 510, 511):
                    vec = [0] * N
                    vec[pos] = fmt.alphabet - 1
                    vectors.append(vec)
                for vec in vectors:
                    blob = encode(name, vec)
                    self.assertEqual(len(blob), fmt.length)
                    self.assertEqual(decode(name, blob), vec)
                    short = enumerative_encode(name, vec)
                    self.assertEqual(len(short), fmt.length - 1)
                    self.assertEqual(enumerative_decode(name, short), vec)

    def test_invalid_length_and_padding(self):
        for name, fmt in FORMATS.items():
            with self.subTest(name=name):
                z = encode(name, [0] * N)
                for bad in (z[:-1], z + b"\0", bytes([255]) * fmt.length):
                    with self.assertRaises(ValueError):
                        decode(name, bad)
                short = enumerative_encode(name, [0] * N)
                with self.assertRaises(ValueError):
                    enumerative_decode(name, b"\xff" * len(short))

    def test_invalid_group_field(self):
        for name, fmt in FORMATS.items():
            # First group uses fewer than 2^width legal values.
            base, group = fmt.factors[0], fmt.groups[0]
            width = (base**group - 1).bit_length()
            bad = base**group
            self.assertLess(bad, 1 << width)
            data = bad.to_bytes(fmt.length, "little")
            with self.subTest(name=name), self.assertRaises(ValueError):
                decode(name, data)


if __name__ == "__main__":
    unittest.main()
