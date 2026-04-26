---
name: OpenTitan
url: https://github.com/lowRISC/opentitan
license: Apache-2.0
language: SystemVerilog, C, Python
difficulty: advanced
status: active
---

## What it does

Open silicon root of trust (RoT) reference implementation. Provides a hardware security anchor — secure boot, attestation, key management, and cryptographic primitives — implemented in open-source RTL. Real chips have been manufactured.

## Why contribute

- Teaches hardware security at the silicon level: RoT, attestation, secure boot chain
- SystemVerilog + formal verification + DV (design verification) skills
- lowRISC runs it — rigorous, high-quality engineering culture
- Rare and extremely valuable skill intersection: hardware + security + open source

## Dev environment setup

```bash
git clone https://github.com/lowRISC/opentitan
cd opentitan

# Install dependencies (Verilator, OpenOCD, etc.)
./util/get-toolchain.sh

# Run simulation
cd hw/ip/aes/dv
make sim

# Software (runs on embedded RISC-V core in the chip)
cd sw/device/lib
```

## Where to find good first issues

- https://github.com/lowRISC/opentitan/issues?q=label%3A%22good+first+issue%22
- DV (design verification) test improvements
- Documentation and tooling scripts
- SW: device library tests

## Community

- Mailing list: opentitan@groups.io
- GitHub Discussions: https://github.com/lowRISC/opentitan/discussions
- lowRISC: https://lowrisc.org/community/

## Learning resources

- Docs: https://opentitan.org/book/
- Silicon RoT concepts: https://opentitan.org/book/doc/security/
- Start with: read the HMAC or AES IP block — smaller, well-documented blocks
