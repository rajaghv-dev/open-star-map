---
name: StarlingX
url: https://opendev.org/starlingx
license: Apache-2.0
language: Python, Go, C
difficulty: advanced
status: active
---

## What it does

OpenInfra Foundation distribution that combines OpenStack, Kubernetes, Ceph, and Linux into a single edge-cloud platform. Targets distributed and far-edge deployments where ultra-low latency, high availability, and remote management matter — telco RAN, industrial IoT, retail edge. Adds patching, configuration management, fault management, and host-deploy services on top of stock upstreams.

## Why contribute

- Real distributed-systems exposure: multi-region orchestration, etcd, PXE boot, redundant controllers
- Touches every layer of the cloud stack — kernel, network, OpenStack services, Kubernetes operators
- Telco-grade requirements (5-nines, fault tolerance) teach production hardening
- OpenInfra contributor governance is well-documented and welcoming to new contributors

## Dev environment setup

```bash
# Mirror sources (~50 GB, allow time)
git clone https://opendev.org/starlingx/tools
cd tools
./build-tools/build-iso/build-iso.sh --help

# Or use pre-built ISO + virtual deployment
# https://docs.starlingx.io/deploy_install_guides/release/virtual/index.html
```

For lightweight contribution work, clone individual service repos (e.g. `starlingx/config`, `starlingx/fault`) and follow their tox-based test instructions:

```bash
git clone https://opendev.org/starlingx/config
cd config
tox -e py3
```

## Where to find good first issues

- Launchpad bugs: https://bugs.launchpad.net/starlingx (filter by `low-hanging-fruit`)
- Storyboard: https://storyboard.openstack.org/#!/project_group/starlingx
- Documentation gaps: https://opendev.org/starlingx/docs

## Community

- Mailing list: starlingx-discuss@lists.starlingx.io
- IRC: #starlingx on OFTC
- Weekly TSC and project calls: https://wiki.openstack.org/wiki/Starlingx/Meetings
- Gerrit: https://review.opendev.org (StarlingX projects)

## Learning resources

- Architecture overview: https://docs.starlingx.io/introduction/index.html
- Subsystem guides: fault management, software management, host management
- Read order: `metal/` (host provisioning) → `config/` (config orchestration) → `nfv/` (workload mgmt)
