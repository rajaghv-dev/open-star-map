---
name: OpenROAD
url: https://github.com/The-OpenROAD-Project/OpenROAD
license: BSD-3-Clause
difficulty: advanced
language: C++, Python, TCL
status: active
---

## What it does

End-to-end RTL-to-GDSII open EDA flow: synthesis (via Yosys), floorplanning, placement, clock tree synthesis, routing, timing analysis. Used in academic chip tapeouts and increasingly in production-adjacent flows.

## Why contribute

- Teaches every stage of chip design automation
- C++ algorithms: graph problems, geometric algorithms, LP/ILP optimization
- Python scripting layer — easier entry than the C++ core
- Chip design skill is extremely rare; EDA is a $10B+ industry

## Dev environment setup

```bash
git clone --recursive https://github.com/The-OpenROAD-Project/OpenROAD
cd OpenROAD
mkdir build && cd build
cmake ..
make -j$(nproc)

# Or use the Docker image — much easier:
docker pull openroad/flow-ubuntu22.04-builder
```

## Where to find good first issues

- https://github.com/The-OpenROAD-Project/OpenROAD/labels/good%20first%20issue
- Python scripting tests
- Documentation for specific tools/passes

## Community

- Slack: https://openroad.slack.com
- Mailing list: openroad@eng.ucsd.edu
- Tapeout community: https://efabless.com/open_shuttle_program

## Learning resources

- Flow overview: https://openroad.readthedocs.io/
- Companion: OpenLane wraps OpenROAD into a simpler flow
- Start with: run the flow on a small design (e.g. `gcd`), then look at failing timing reports
