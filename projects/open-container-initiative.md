---
name: runc
url: https://github.com/opencontainers/runc
license: Apache-2.0
language: Go
difficulty: intermediate
status: active
---

## What it does

The reference implementation of the OCI Runtime Specification — the low-level Go binary that actually starts and stops containers. Docker, containerd, and Podman all call runc (or a compatible runtime like crun) underneath. Also: `image-spec` (container image format) and `distribution-spec` (registry wire protocol) live under OCI.

## Why contribute

- Teaches container internals: cgroups, namespaces, seccomp, Linux capabilities, pivot_root
- Go systems programming at the Linux kernel interface level
- Small, focused codebase — the spec is the truth, the code implements it exactly
- Understanding runc makes everything from Kubernetes to Kata Containers legible

## Dev environment setup

```bash
git clone https://github.com/opencontainers/runc
cd runc

# Build (requires libseccomp-dev)
sudo apt install libseccomp-dev
make

# Run tests (requires root or rootless setup)
sudo make test

# Try it manually:
mkdir -p /tmp/mycontainer/rootfs
docker export $(docker create busybox) | tar -C /tmp/mycontainer/rootfs -xf -
cd /tmp/mycontainer
runc spec   # generates config.json
sudo runc run mycontainer
```

## Where to find good first issues

- https://github.com/opencontainers/runc/labels/good%20first%20issue
- OCI image-spec: https://github.com/opencontainers/image-spec/labels/good%20first%20issue
- Test coverage and documentation improvements

## Community

- Slack: https://communityinviter.com/apps/opencontainers/oci
- Dev mailing list: https://groups.google.com/a/opencontainers.org/g/dev
- OCI specs: https://github.com/opencontainers

## Learning resources

- OCI Runtime Spec: https://github.com/opencontainers/runtime-spec/blob/main/spec.md
- Linux namespaces: `man 7 namespaces`
- cgroups v2: https://www.kernel.org/doc/html/latest/admin-guide/cgroup-v2.html
- Start with: read `libcontainer/` — the core Linux process lifecycle code
