---
name: OpenBao
url: https://github.com/openbao/openbao
license: MPL-2.0
language: Go
difficulty: intermediate
status: active
---

## What it does

Linux Foundation fork of HashiCorp Vault, governed openly after Vault's BSL relicense. Provides secrets management, encryption-as-a-service, dynamic database/cloud credentials, PKI, and identity brokering. Wire-compatible with the Vault API where possible. Preserves the open-source community's ability to receive patches without proprietary restrictions.

## Why contribute

- Secrets management is foundational to every cloud and AI workload — high learning leverage
- Fork is in active divergence — early contributors shape direction
- Go codebase with clear plugin boundaries (auth methods, secret engines, storage backends)
- LF governance: explicit contributor ladder and TSC

## Dev environment setup

```bash
git clone https://github.com/openbao/openbao
cd openbao
make bootstrap
make dev

# Run dev server
./bin/bao server -dev
export VAULT_ADDR=http://127.0.0.1:8200
./bin/bao kv put secret/hello value=world
```

## Where to find good first issues

- https://github.com/openbao/openbao/labels/good%20first%20issue
- https://github.com/openbao/openbao/labels/help%20wanted
- Plugin parity work (porting Vault plugins forward) is a constant need

## Community

- LF Edge Slack: `#openbao`
- Bi-weekly TSC meetings (calendar in repo)
- Mailing list: https://lists.openssf.org/g/openbao

## Learning resources

- Architecture (inherited from Vault): https://openbao.org/docs/internals/architecture/
- Plugin system: read `sdk/plugin/` and `vault/plugin_catalog.go`
- Suggested entry: write or improve a secret engine or auth method plugin
