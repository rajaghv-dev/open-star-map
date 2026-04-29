---
name: OpenEmbedded
url: https://github.com/openembedded/openembedded-core
license: MIT
language: Python, Shell, BitBake
difficulty: intermediate
status: active
---

## What it does

Build framework for custom embedded Linux distributions. You write "recipes" (metadata) and BitBake builds a complete Linux image from source — kernel, toolchain, rootfs, packages — for any target hardware. The Yocto Project is the umbrella; OpenEmbedded-Core (OE-Core) is the recipe layer underneath it.

Used in: OpenBMC, automotive (AGL), industrial IoT, network appliances, OpenWrt alternatives.

## Why contribute

- Teaches the entire embedded Linux build pipeline: cross-compilation, rootfs construction, package feeds
- BitBake (Python) is its own build system — understanding it is a rare, high-value skill
- Bridge between software and hardware: you touch kernel configs, device trees, BSPs
- OpenBMC is built on OE — contributing here directly feeds OpenBMC skills

## Dev environment setup

```bash
# Requires Linux host (or WSL2 with enough disk — builds are large, 50–100 GB)
git clone https://github.com/openembedded/openembedded-core oe-core
cd oe-core

# Quick build (uses kas or manual init)
source oe-init-build-env build
bitbake core-image-minimal

# For a specific machine (e.g. QEMU ARM64):
MACHINE=qemuarm64 bitbake core-image-minimal
runqemu qemuarm64 nographic
```

## Where to find good first issues

- OE-Core mailing list patches: https://lists.openembedded.org/g/openembedded-core
- Recipe upgrades (bump package versions): tracked at https://www.yoctoproject.org/bugzilla/
- Bugzilla: https://bugzilla.yoctoproject.org/ — filter `Status=NEW`

## Community

- Mailing list (primary): openembedded-core@lists.openembedded.org
- IRC: #yocto on Libera.Chat
- Yocto Project: https://www.yoctoproject.org/
- Patch submission: email patches to mailing list (no GitHub PRs for OE-Core)

## Learning resources

- Yocto overview: https://docs.yoctoproject.org/overview-manual/
- BitBake manual: https://docs.yoctoproject.org/bitbake/
- Dev quick start: https://docs.yoctoproject.org/brief-yoctoprojectqs/
- Start with: upgrade a recipe (change `SRC_URI` + `SRCREV`, test build, send patch to mailing list)
