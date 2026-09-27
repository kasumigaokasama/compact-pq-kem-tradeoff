# Security scope

This repository contains research/reproducibility code. It does not implement a new production KEM and **must not be used to protect production data**.

Model reproduction is not a security proof. Research code may intentionally omit production-hardening features, including constant-time execution and secret-memory handling. This is not an audited cryptographic library.

Software tests validate calculations; they do not validate cryptographic security. A green CI check means only that the deterministic research calculations reproduce successfully.

For errors in this report or its research calculations, open an issue with a minimal reproduction. Third-party cryptographic scheme vulnerabilities should follow the disclosure guidance of the original scheme authors where applicable; avoid posting undisclosed vulnerabilities publicly.
