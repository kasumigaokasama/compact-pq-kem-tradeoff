# Copyright 2026 Yusuf Kaya and Jan Moser
# SPDX-License-Identifier: Apache-2.0
"""Regression checks for published model arithmetic, not cryptographic security."""
import contextlib
import io
import math
from dawn_codec import FORMATS, theoretical_bytes
from reproduce_dawn_dfr_model import run
from qc_entropy_frontier import support_bits
from ring_structure import run as ring_run


def main():
    expected = {"alpha_pk": (615, 614), "alpha_ct": (436, 435),
                "beta_pk": (514, 513), "beta_ct": (450, 449)}
    for name, (grouped, whole) in expected.items():
        assert FORMATS[name].length == grouped
        assert theoretical_bytes(FORMATS[name]) == whole
    with contextlib.redirect_stdout(io.StringIO()):
        alpha = run(512, 769, 160, 64, 96, 160, range(-3, 4))
        beta = run(512, 257, 64, 32, 48, 64, range(0, 2))
        ring_run()
    assert abs(math.log2(alpha) - (-132.676946974)) < 1e-8
    assert abs(math.log2(beta) - (-130.133613254)) < 1e-8
    assert abs(support_bits(17669, 66) - 622.952) < 0.0005
    assert abs(support_bits(17669, 75) - 694.542) < 0.0005
    assert abs(support_bits(24646, 134) - 1196.018) < 0.0005
    print("All deterministic result checks passed. This is not a security test.")


if __name__ == "__main__":
    main()
