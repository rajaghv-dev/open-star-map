---
name: OpenBMC
url: https://github.com/openbmc/openbmc
license: Apache-2.0
language: C++, Python, Meson
difficulty: advanced
status: active
---

## What it does

Complete firmware stack for Baseboard Management Controllers (BMCs) — the microcontrollers embedded in servers that handle out-of-band management (power, thermal, IPMI, Redfish). Used by Meta, Google, IBM, and major ODMs.

## Why contribute

- Deep systems programming: hardware interfaces, IPMI/Redfish protocols, D-Bus IPC
- Teaches you how real datacenter servers are managed at the firmware level
- Builds rare, highly valued skills in infrastructure hardware
- Used in production at hyperscalers

## Dev environment setup

```bash
# Requires Linux host with Docker or a Yocto build environment
git clone https://github.com/openbmc/openbmc
cd openbmc

# Build for a specific machine (e.g., QEMU simulation)
. setup romulus build
bitbake obmc-phosphor-image

# Run in QEMU (much faster than real hardware for dev)
# See: https://github.com/openbmc/openbmc/blob/master/docs/development/dev-environment.md
```

## Where to find good first issues

- https://github.com/openbmc/openbmc/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22
- Phosphor D-Bus interfaces: https://github.com/openbmc/phosphor-dbus-interfaces
- Python tooling repos are easier entry points than the core firmware

## Community

- Mailing list: openbmc@lists.ozlabs.org
- IRC: #openbmc on OFTC
- Discord: https://discord.gg/69Km47zH98
- Gerrit code review: https://gerrit.openbmc.org

## Learning resources

- Architecture overview: https://github.com/openbmc/docs/blob/master/architecture.md
- Redfish API: https://redfish.dmtf.org/
- D-Bus tutorial: https://dbus.freedesktop.org/doc/dbus-tutorial.html
- Start with: read the phosphor-host-ipmid or phosphor-webserver repo — smaller scope
