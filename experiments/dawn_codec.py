# Copyright 2026 Yusuf Kaya and Jan Moser
# SPDX-License-Identifier: Apache-2.0
"""Independent *model* of the DAWN Table 8 grouping, not an official wire codec.

Coefficient vectors have length 512. Group fields are concatenated little-endian.
For beta, a coefficient is split by CRT into residues modulo 3 and 86/43.
The spec's exact field ordering and bit ordering need official code/test vectors.
"""
from __future__ import annotations

import math
from dataclasses import dataclass

N = 512


@dataclass(frozen=True)
class Format:
    name: str
    alphabet: int
    length: int
    factors: tuple[int, ...]
    groups: tuple[int, ...]


FORMATS = {
    "alpha_pk": Format("alpha_pk", 769, 615, (769,), (5,)),
    "alpha_ct": Format("alpha_ct", 110, 436, (110,), (5,)),
    "beta_pk": Format("beta_pk", 258, 514, (3, 86), (17, 7)),
    "beta_ct": Format("beta_ct", 129, 450, (3, 43), (17, 7)),
}


def group_widths(fmt: Format):
    for radix, group in zip(fmt.factors, fmt.groups):
        for start in range(0, N, group):
            count = min(group, N - start)
            yield radix, start, count, (radix**count - 1).bit_length()


def _residues(coeffs: list[int], fmt: Format) -> list[list[int]]:
    if len(coeffs) != N or any(not 0 <= x < fmt.alphabet for x in coeffs):
        raise ValueError("coefficient out of range or wrong length")
    return [[x % radix for x in coeffs] for radix in fmt.factors]


def encode(name: str, coeffs: list[int]) -> bytes:
    fmt = FORMATS[name]
    streams = _residues(coeffs, fmt)
    accum = offset = 0
    for stream, radix, group in zip(streams, fmt.factors, fmt.groups):
        for start in range(0, N, group):
            values = stream[start:start + group]
            field = sum(x * radix**i for i, x in enumerate(values))
            width = (radix**len(values) - 1).bit_length()
            accum |= field << offset
            offset += width
    if (offset + 7) // 8 != fmt.length:
        raise AssertionError("unexpected bit budget")
    return accum.to_bytes(fmt.length, "little")


def decode(name: str, data: bytes) -> list[int]:
    fmt = FORMATS[name]
    if len(data) != fmt.length:
        raise ValueError("noncanonical byte length")
    value = int.from_bytes(data, "little")
    total = sum(width for _, _, _, width in group_widths(fmt))
    if value >> total:
        raise ValueError("nonzero padding")
    streams: list[list[int]] = []
    offset = 0
    for radix, group in zip(fmt.factors, fmt.groups):
        stream = []
        for start in range(0, N, group):
            count = min(group, N - start)
            width = (radix**count - 1).bit_length()
            field = (value >> offset) & ((1 << width) - 1)
            if field >= radix**count:
                raise ValueError("invalid mixed-radix field")
            for _ in range(count):
                stream.append(field % radix)
                field //= radix
            offset += width
        streams.append(stream)
    if len(streams) == 1:
        return streams[0]
    low, high = streams
    modulus = fmt.factors[1]
    inv3 = pow(3, -1, modulus)
    return [a + 3 * (((b - a) * inv3) % modulus) for a, b in zip(low, high)]


def enumerative_encode(name: str, coeffs: list[int]) -> bytes:
    """Whole-vector base-M bijection; fixed-length theoretical bound."""
    fmt = FORMATS[name]
    _residues(coeffs, fmt)
    number = 0
    for x in reversed(coeffs):
        number = number * fmt.alphabet + x
    return number.to_bytes(theoretical_bytes(fmt), "little")


def enumerative_decode(name: str, data: bytes) -> list[int]:
    fmt = FORMATS[name]
    if len(data) != theoretical_bytes(fmt):
        raise ValueError("wrong length")
    value = int.from_bytes(data, "little")
    if value >= fmt.alphabet**N:
        raise ValueError("noncanonical vector")
    out = []
    for _ in range(N):
        value, x = divmod(value, fmt.alphabet)
        out.append(x)
    return out


def theoretical_bytes(fmt: Format) -> int:
    return ((fmt.alphabet**N - 1).bit_length() + 7) // 8


def ledger():
    for name, fmt in FORMATS.items():
        bits = sum(width for _, _, _, width in group_widths(fmt))
        entropy = N * math.log2(fmt.alphabet)
        lower = theoretical_bytes(fmt)
        print(f"{name}: grouped_bits={bits} actual={fmt.length}B "
              f"entropy={entropy:.6f}bits minimum={lower}B slack={fmt.length-lower}B")


if __name__ == "__main__":
    ledger()
