---
name: Kata Containers
url: https://github.com/kata-containers/kata-containers
license: Apache-2.0
language: Go, Rust
difficulty: advanced
status: active
---

## What it does

OCI-compatible container runtime that runs each container inside a lightweight VM (QEMU, Cloud Hypervisor, Firecracker) instead of a shared kernel namespace. Gives you container UX with VM-level isolation. Used at hyperscalers, telcos, and anywhere multi-tenant workloads need strong isolation.

## Why contribute

- Teaches the full container↔VM intersection: OCI runtime spec, virtio, vsock, KVM, agent protocol
- Rust (kata-agent) + Go (runtime-rs, containerd shim) in one codebase
- CNCF sandbox → graduated trajectory; rigorous review culture
- Rare skills: hypervisor integration, secure container runtimes

## Dev environment setup

```bash
git clone https://github.com/kata-containers/kata-containers
cd kata-containers

# Build the runtime (Go)
cd src/runtime
make

# Build the agent (Rust)
cd src/agent
cargo build --release

# CI environment (easiest dev loop)
# See: https://github.com/kata-containers/kata-containers/blob/main/docs/Developer-Guide.md
# Requires: KVM-capable host (WSL2 with nested virt or bare Linux)

# Check KVM availability
ls /dev/kvm
```

## Where to find good first issues

- https://github.com/kata-containers/kata-containers/labels/good%20first%20issue
- https://github.com/kata-containers/kata-containers/labels/help%20wanted
- Documentation and CI test improvements are accessible entry points

## Community

- Slack: https://katacontainers.slack.com
- Weekly calls: https://github.com/kata-containers/community
- Mailing list: kata-dev@lists.katacontainers.io

## Learning resources

- Architecture: https://github.com/kata-containers/kata-containers/blob/main/docs/design/architecture/
- OCI Runtime Spec: https://github.com/opencontainers/runtime-spec
- virtio overview: https://www.redhat.com/en/blog/introduction-virtio-networking-and-vhost-net
- Start with: read `src/runtime/virtcontainers/` — the VM lifecycle management layer
