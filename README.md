# open* — An end-to-end open systems stack

> *Open\* is not a naming pattern; it is an end-to-end open systems stack — from silicon root of trust, firmware, racks, cloud, containers, observability, policy, security, AI inference, and data governance.*

A curated, structured map of **100 open\* projects** — verified as truly open source — for learning and contributing. Every project has an OSI-approved license and a public contribution process.

---

## Strategic framing

This repository covers the entire stack:

```
Silicon RoT → Firmware → Racks → Cloud → Containers → Observability → Policy → Security → AI Inference → Data Governance
   OpenTitan    OpenBMC     OCP    OpenStack  OCI/Kata   OpenTelemetry   OPA    OpenSSF     ONNX/OpenVINO   OpenLineage
```

**Demo chain** you can build:
```
AI workload → ONNX (model format) → OpenVINO (inference) → OpenTelemetry (traces)
            → OpenSearch (logs) → OPA (policy gate) → OpenSCAP (compliance) → OpenSSF Scorecard
```

---

## My priority tiers

### Strategic — track deeply
OpenInfra, OpenStack, StarlingX, Kata Containers, OpenBMC, OCP, OpenTitan, OpenROAD,
OpenTelemetry, OPA, OpenAPI, OCI, OpenSSF, OpenChain, OpenSCAP, OpenSearch, ONNX,
OpenVINO, OpenCV, OpenEmbedded.

### Practical — build demos
OpenTelemetry · OpenSearch · OPA · OpenAPI · ONNX · OpenVINO · OpenCV · OpenBMC · OpenSCAP · OpenSSF Scorecard

### Watchlist — positioning
OpenTitan · OpenROAD · OpenLane · OpenSBI · OpenHW · OCP · StarlingX · OpenDataHub ·
OpenLineage · OpenMetadata · OpenTofu · OpenBao · OpenFGA

---

## Jump to category

- [Infra Foundations & Cloud Platforms](#infra-foundations--cloud-platforms)
- [OpenStack Services](#openstack-services)
- [Edge & Telco Cloud](#edge--telco-cloud)
- [Firmware & Hardware Platforms](#firmware--hardware-platforms)
- [Silicon & EDA](#silicon--eda)
- [HPC & Open Compute](#hpc--open-compute)
- [Observability](#observability)
- [Policy, Security & Compliance](#policy-security--compliance)
- [Containers & Orchestration](#containers--orchestration)
- [Storage & Distributed FS](#storage--distributed-fs)
- [Networking & SDN](#networking--sdn)
- [Operating Systems](#operating-systems)
- [AI, Inference & ML](#ai-inference--ml)
- [Data Platform & Governance](#data-platform--governance)
- [APIs, Identity & DevOps Standards](#apis-identity--devops-standards)
- [Open Data & Collaboration](#open-data--collaboration)
- [Not truly open (listed for awareness)](#not-truly-open-listed-for-awareness)

---

## Infra Foundations & Cloud Platforms

| # | Project | Description | Lang | Difficulty | License | Repo |
|---|---------|-------------|------|------------|---------|------|
| 1 | **OpenInfra Foundation** | Umbrella for open infrastructure ecosystems | Multi | — | Apache-2.0 | [openinfra.dev](https://openinfra.dev) |
| 2 | **OpenStack** | Private/public cloud IaaS platform | Python | Intermediate | Apache-2.0 | [opendev.org/openstack](https://opendev.org/openstack) |
| 59 | **OpenNebula** | Lightweight cloud/edge management | C++/Ruby | Intermediate | Apache-2.0 | [github.com/OpenNebula/one](https://github.com/OpenNebula/one) |
| 56 | **OpenTofu** | Terraform-compatible open IaC | Go | Intermediate | MPL-2.0 | [github.com/opentofu/opentofu](https://github.com/opentofu/opentofu) |
| 57 | **OpenBao** | Vault-derived secrets management | Go | Intermediate | MPL-2.0 | [github.com/openbao/openbao](https://github.com/openbao/openbao) |

---

## OpenStack Services

| # | Project | Description | Lang | Difficulty | License | Repo |
|---|---------|-------------|------|------------|---------|------|
| 3 | **Nova** | VM lifecycle and compute scheduling | Python | Intermediate | Apache-2.0 | [opendev.org/openstack/nova](https://opendev.org/openstack/nova) |
| 4 | **Neutron** | Virtual networking for cloud | Python | Intermediate | Apache-2.0 | [opendev.org/openstack/neutron](https://opendev.org/openstack/neutron) |
| 5 | **Cinder** | Block storage for cloud | Python | Intermediate | Apache-2.0 | [opendev.org/openstack/cinder](https://opendev.org/openstack/cinder) |
| 6 | **Swift** | Object storage | Python | Intermediate | Apache-2.0 | [opendev.org/openstack/swift](https://opendev.org/openstack/swift) |
| 7 | **Ironic** | Bare-metal provisioning | Python | Advanced | Apache-2.0 | [opendev.org/openstack/ironic](https://opendev.org/openstack/ironic) |
| 8 | **Keystone** | Cloud identity/authentication | Python | Intermediate | Apache-2.0 | [opendev.org/openstack/keystone](https://opendev.org/openstack/keystone) |
| 9 | **Heat** | Infrastructure orchestration | Python | Intermediate | Apache-2.0 | [opendev.org/openstack/heat](https://opendev.org/openstack/heat) |
| 10 | **Magnum** | Kubernetes/container cluster mgmt | Python | Intermediate | Apache-2.0 | [opendev.org/openstack/magnum](https://opendev.org/openstack/magnum) |

**Good entry point:** Pick one service, run it with devstack (`git clone https://opendev.org/openstack/devstack`), find a `low-hanging-fruit` bug, and submit via Gerrit.

---

## Edge & Telco Cloud

| # | Project | Description | Lang | Difficulty | License | Repo |
|---|---------|-------------|------|------------|---------|------|
| 11 | **StarlingX** | Edge/telco cloud infrastructure | Python/Ansible | Advanced | Apache-2.0 | [opendev.org/starlingx](https://opendev.org/starlingx) |
| 12 | **Kata Containers** | VM-isolated OCI containers | Go/Rust | Advanced | Apache-2.0 | [github.com/kata-containers/kata-containers](https://github.com/kata-containers/kata-containers) |
| 13 | **Zuul** | Gated CI/CD across repos | Python | Intermediate | Apache-2.0 | [opendev.org/zuul/zuul](https://opendev.org/zuul/zuul) |
| 14 | **OpenInfra Labs** | Experimental infra patterns | Multi | Beginner | Apache-2.0 | [openinfralabs.org](https://openinfralabs.org) |
| 51 | **OpenYurt** | Edge-cloud Kubernetes management | Go | Intermediate | Apache-2.0 | [github.com/openyurtio/openyurt](https://github.com/openyurtio/openyurt) |

---

## Firmware & Hardware Platforms

| # | Project | Description | Lang | Difficulty | License | Repo |
|---|---------|-------------|------|------------|---------|------|
| 16 | **OpenBMC** | Open server BMC firmware | C++/Python | Advanced | Apache-2.0 | [github.com/openbmc/openbmc](https://github.com/openbmc/openbmc) |
| 18 | **OpenSBI** | RISC-V supervisor firmware layer | C | Advanced | BSD-2 | [github.com/riscv-software-src/opensbi](https://github.com/riscv-software-src/opensbi) |
| 19 | **OpenOCD** | JTAG/SWD debug tooling | C | Advanced | GPL-2.0 | [sourceforge.net/p/openocd](https://sourceforge.net/p/openocd/code/) |
| 24 | **OpenPOWER** | POWER ISA ecosystem | C/Verilog | Advanced | Apache-2.0 | [openpowerfoundation.org](https://openpowerfoundation.org) |
| 26 | **OpenHPC** | HPC software stack | Shell/Ansible | Intermediate | Apache-2.0 | [github.com/openhpc/ohpc](https://github.com/openhpc/ohpc) |
| 75 | **OpenEmbedded** | Build framework behind Yocto | Python/Shell | Intermediate | MIT | [github.com/openembedded/openembedded-core](https://github.com/openembedded/openembedded-core) |

---

## Silicon & EDA

| # | Project | Description | Lang | Difficulty | License | Repo |
|---|---------|-------------|------|------------|---------|------|
| 20 | **OpenTitan** | Open silicon root of trust | SystemVerilog/C | Advanced | Apache-2.0 | [github.com/lowRISC/opentitan](https://github.com/lowRISC/opentitan) |
| 21 | **Open Compute Project (OCP)** | Open server, rack, power, cooling designs | Specs/CAD | — | OCP License | [opencompute.org](https://www.opencompute.org) |
| 27 | **OpenHW Group** | Open processor cores and verification | SystemVerilog | Advanced | Apache-2.0 | [github.com/openhwgroup](https://github.com/openhwgroup) |
| 28 | **OpenRISC** | Open RISC CPU ISA | Verilog | Advanced | LGPL | [openrisc.io](https://openrisc.io) |
| 30 | **OpenPiton** | Open manycore processor research | Verilog | Advanced | BSD | [github.com/PrincetonUniversity/openpiton](https://github.com/PrincetonUniversity/openpiton) |
| 31 | **OpenROAD** | RTL-to-GDS open EDA flow | C++/Python | Advanced | BSD-3 | [github.com/The-OpenROAD-Project/OpenROAD](https://github.com/The-OpenROAD-Project/OpenROAD) |
| 32 | **OpenLane** | ASIC design automation flow | Python/TCL | Advanced | Apache-2.0 | [github.com/efabless/openlane](https://github.com/efabless/openlane) |
| 33 | **OpenFASOC** | Analog/mixed-signal SoC generators | Python | Advanced | Apache-2.0 | [github.com/idea-fasoc/OpenFASOC](https://github.com/idea-fasoc/OpenFASOC) |
| 34 | **OpenRAM** | SRAM compiler | Python | Advanced | BSD-3 | [github.com/VLSIDA/OpenRAM](https://github.com/VLSIDA/OpenRAM) |
| 35 | **OpenCores** | Repository of open HDL IP cores | VHDL/Verilog | Advanced | LGPL | [opencores.org](https://opencores.org) |
| 36 | **OpenFPGA** | FPGA architecture/toolflow research | C++/Python | Advanced | MIT | [github.com/lnis-uofu/OpenFPGA](https://github.com/lnis-uofu/OpenFPGA) |

---

## HPC & Open Compute

| # | Project | Description | Lang | Difficulty | License | Repo |
|---|---------|-------------|------|------------|---------|------|
| 22 | **Open Rack** | Rack architecture from OCP | Specs | — | OCP License | [opencompute.org](https://www.opencompute.org/wiki/Rack) |
| 23 | **Open Rack Wide (ORv3)** | Rack-scale AI/data-center design | Specs | — | OCP License | [opencompute.org](https://www.opencompute.org) |
| 26 | **OpenHPC** | HPC software stack on Linux | Shell/Ansible | Intermediate | Apache-2.0 | [github.com/openhpc/ohpc](https://github.com/openhpc/ohpc) |

---

## Observability

| # | Project | Description | Lang | Difficulty | License | Repo |
|---|---------|-------------|------|------------|---------|------|
| 39 | **OpenTelemetry** | Logs, metrics, traces standard | Go/Multi | **Beginner** | Apache-2.0 | [github.com/open-telemetry](https://github.com/open-telemetry) |
| 40 | **OpenMetrics** | Metrics exposition standard | Go | Beginner | Apache-2.0 | [github.com/OpenObservability/OpenMetrics](https://github.com/OpenObservability/OpenMetrics) |
| 43 | **OpenSearch** | Search, logs, analytics | Java | Intermediate | Apache-2.0 | [github.com/opensearch-project/OpenSearch](https://github.com/opensearch-project/OpenSearch) |
| 44 | **OpenSearch Dashboards** | Dashboarding for OpenSearch | TypeScript | Intermediate | Apache-2.0 | [github.com/opensearch-project/OpenSearch-Dashboards](https://github.com/opensearch-project/OpenSearch-Dashboards) |

*(OpenTracing #41 and OpenCensus #42 are archived — merged into OpenTelemetry)*

---

## Policy, Security & Compliance

| # | Project | Description | Lang | Difficulty | License | Repo |
|---|---------|-------------|------|------------|---------|------|
| 45 | **Open Policy Agent (OPA)** | Policy-as-code engine | Go | Intermediate | Apache-2.0 | [github.com/open-policy-agent/opa](https://github.com/open-policy-agent/opa) |
| 61 | **OpenSSF** | Open-source software security foundation | Multi | **Beginner** | Apache-2.0 | [github.com/ossf](https://github.com/ossf) |
| 62 | **OpenSSF Scorecard** | Repository security scoring | Go | Beginner | Apache-2.0 | [github.com/ossf/scorecard](https://github.com/ossf/scorecard) |
| 63 | **OpenSSF SLSA** | Build/provenance supply-chain framework | Spec/Go | Intermediate | Apache-2.0 | [github.com/slsa-framework/slsa](https://github.com/slsa-framework/slsa) |
| 64 | **OpenChain** | OSS license compliance standard | Spec | Beginner | CC0 | [openchainproject.org](https://openchainproject.org) |
| 65 | **OpenSCAP** | Security compliance scanning | C | Intermediate | LGPL-2.1 | [github.com/OpenSCAP/openscap](https://github.com/OpenSCAP/openscap) |
| 66 | **OpenVAS / Greenbone** | Vulnerability scanning | C/Python | Intermediate | AGPL-3.0 | [github.com/greenbone/openvas-scanner](https://github.com/greenbone/openvas-scanner) |
| 67 | **OpenSSL** | TLS/crypto foundation | C | Advanced | Apache-2.0 | [github.com/openssl/openssl](https://github.com/openssl/openssl) |
| 68 | **OpenSSH** | Secure remote login/admin | C | Advanced | BSD | [github.com/openssh/openssh-portable](https://github.com/openssh/openssh-portable) |
| 70 | **OpenID Connect** | Authentication federation standard | Spec | Beginner | Apache-2.0 | [openid.net](https://openid.net) |
| 71 | **OpenFGA** | Fine-grained authorization model | Go | Intermediate | Apache-2.0 | [github.com/openfga/openfga](https://github.com/openfga/openfga) |
| 72 | **OpenTDF** | Trusted data format / data-centric access | Go/Python | Intermediate | Apache-2.0 | [github.com/opentdf](https://github.com/opentdf) |
| 46 | **OpenCost** | Kubernetes cost visibility | Go | Intermediate | Apache-2.0 | [github.com/opencost/opencost](https://github.com/opencost/opencost) |
| 47 | **OpenFeature** | Feature flag standard | Go/Multi | **Beginner** | Apache-2.0 | [github.com/open-feature](https://github.com/open-feature) |

---

## Containers & Orchestration

| # | Project | Description | Lang | Difficulty | License | Repo |
|---|---------|-------------|------|------------|---------|------|
| 49 | **Open Container Initiative (OCI)** | Container image/runtime specs | Go | Intermediate | Apache-2.0 | [github.com/opencontainers/runc](https://github.com/opencontainers/runc) |
| 53 | **OpenFaaS** | Functions-as-a-service | Go | **Beginner** | MIT | [github.com/openfaas/faas](https://github.com/openfaas/faas) |
| 54 | **OpenWhisk** | Event-driven serverless platform | Scala/Go | Intermediate | Apache-2.0 | [github.com/apache/openwhisk](https://github.com/apache/openwhisk) |
| 52 | **OpenKruise** | Advanced Kubernetes workload mgmt | Go | Intermediate | Apache-2.0 | [github.com/openkruise/kruise](https://github.com/openkruise/kruise) |
| 55 | **Open Service Mesh (OSM)** | Lightweight SMI service mesh | Go | Intermediate | Apache-2.0 | [github.com/openservicemesh/osm](https://github.com/openservicemesh/osm) |
| 58 | **OpenShift (OKD)** | Red Hat Kubernetes platform | Go | Advanced | Apache-2.0 | [github.com/openshift/okd](https://github.com/openshift/okd) |

---

## Storage & Distributed FS

| # | Project | Description | Lang | Difficulty | License | Repo |
|---|---------|-------------|------|------------|---------|------|
| 50 | **OpenEBS** | Kubernetes-native storage | Go | Intermediate | Apache-2.0 | [github.com/openebs/openebs](https://github.com/openebs/openebs) |
| 73 | **OpenZFS** | Advanced filesystem / snapshots / integrity | C | Advanced | CDDL-1.0 | [github.com/openzfs/zfs](https://github.com/openzfs/zfs) |
| 80 | **OpenAFS** | Distributed filesystem (historical) | C | Advanced | IPL-1.0 | [github.com/openafs/openafs](https://github.com/openafs/openafs) |

---

## Networking & SDN

| # | Project | Description | Lang | Difficulty | License | Repo |
|---|---------|-------------|------|------------|---------|------|
| 74 | **OpenWrt** | Router/edge Linux distribution | C/Shell | Intermediate | GPL-2.0 | [github.com/openwrt/openwrt](https://github.com/openwrt/openwrt) |

---

## Operating Systems

| # | Project | Description | Lang | Difficulty | License | Repo |
|---|---------|-------------|------|------------|---------|------|
| 76 | **openSUSE** | Enterprise/dev Linux ecosystem | C/Shell | Intermediate | GPL | [github.com/openSUSE](https://github.com/openSUSE) |
| 77 | **OpenBSD** | Security-focused Unix-like OS | C | Advanced | BSD | [github.com/openbsd/src](https://github.com/openbsd/src) |
| 78 | **OpenIndiana** | Illumos/Solaris-descended OS | C | Advanced | CDDL | [github.com/openindiana/oi-userland](https://github.com/openindiana/oi-userland) |
| 79 | **OpenRC** | Lightweight service manager | C/Shell | Intermediate | BSD-2 | [github.com/OpenRC/openrc](https://github.com/OpenRC/openrc) |
| 81 | **OpenHarmony** | IoT/distributed OS ecosystem | C++/Java | Intermediate | Apache-2.0 | [gitee.com/openharmony](https://gitee.com/openharmony) |
| 75 | **OpenEmbedded** | Build framework behind Yocto | Python/Shell | Intermediate | MIT | [github.com/openembedded/openembedded-core](https://github.com/openembedded/openembedded-core) |

---

## AI, Inference & ML

| # | Project | Description | Lang | Difficulty | License | Repo |
|---|---------|-------------|------|------------|---------|------|
| 82 | **OpenCV** | Computer vision — CCTV, ANPR, robotics | C++/Python | Intermediate | Apache-2.0 | [github.com/opencv/opencv](https://github.com/opencv/opencv) |
| 83 | **ONNX** | ML model interoperability format | Python/C++ | Intermediate | Apache-2.0 | [github.com/onnx/onnx](https://github.com/onnx/onnx) |
| 84 | **OpenVINO** | Optimized inference on Intel CPU/GPU/NPU | C++/Python | Intermediate | Apache-2.0 | [github.com/openvinotoolkit/openvino](https://github.com/openvinotoolkit/openvino) |
| 85 | **OpenXLA** | XLA compiler ecosystem | C++/Python | Advanced | Apache-2.0 | [github.com/openxla/xla](https://github.com/openxla/xla) |
| 86 | **OpenML** | Datasets and experiment sharing | Python | **Beginner** | BSD-3 | [github.com/openml/OpenML](https://github.com/openml/OpenML) |
| 87 | **OpenMMLab** | CV model toolkits (MMDet, MMSeg…) | Python | **Beginner** | Apache-2.0 | [github.com/open-mmlab](https://github.com/open-mmlab) |
| 88 | **OpenLLM** | LLM deployment/serving | Python | Intermediate | Apache-2.0 | [github.com/bentoml/OpenLLM](https://github.com/bentoml/OpenLLM) |
| 89 | **OpenWebUI** | Local LLM UI (often with Ollama) | Python/Svelte | **Beginner** | MIT | [github.com/open-webui/open-webui](https://github.com/open-webui/open-webui) |
| 15 | **OpenStack for AI (OpenInfra AI)** | AI workloads on open infra stack | Python | Intermediate | Apache-2.0 | [openinfra.dev/ai](https://openinfra.dev/ai) |

*(OpenAssistant #90 is archived — dataset/model effort ended)*

---

## Data Platform & Governance

| # | Project | Description | Lang | Difficulty | License | Repo |
|---|---------|-------------|------|------------|---------|------|
| 96 | **OpenDataHub** | Open data/AI platform on Kubernetes | Python/Go | Intermediate | Apache-2.0 | [github.com/opendatahub-io/opendatahub-operator](https://github.com/opendatahub-io/opendatahub-operator) |
| 97 | **OpenLineage** | Data pipeline lineage metadata | Python/Java | Intermediate | Apache-2.0 | [github.com/OpenLineage/OpenLineage](https://github.com/OpenLineage/OpenLineage) |
| 98 | **OpenMetadata** | Metadata/catalog/governance platform | Java/Python | Intermediate | Apache-2.0 | [github.com/open-metadata/OpenMetadata](https://github.com/open-metadata/OpenMetadata) |
| 93 | **OpenRefine** | Dataset cleanup and transformation | Java | **Beginner** | BSD-3 | [github.com/OpenRefine/OpenRefine](https://github.com/OpenRefine/OpenRefine) |
| 94 | **OpenStreetMap** | Open map/geospatial data | Multi | **Beginner** | ODbL | [github.com/openstreetmap](https://github.com/openstreetmap) |
| 95 | **OpenAQ** | Open air-quality data | Python | **Beginner** | MIT | [github.com/openaq/openaq-api-v2](https://github.com/openaq/openaq-api-v2) |

---

## APIs, Identity & DevOps Standards

| # | Project | Description | Lang | Difficulty | License | Repo |
|---|---------|-------------|------|------------|---------|------|
| 48 | **OpenAPI** | API specification/tool contracts | Spec/Multi | **Beginner** | Apache-2.0 | [github.com/OAI/OpenAPI-Specification](https://github.com/OAI/OpenAPI-Specification) |
| 99 | **OpenProject** | Open project planning/collaboration | Ruby/Angular | Intermediate | GPL-3.0 | [github.com/opf/openproject](https://github.com/opf/openproject) |
| 100 | **OpenDocument Format (ODF)** | Open office/document format | Spec | Beginner | Apache-2.0 | [oasis-open.org/committees/tc_home.php?wg_abbrev=office](https://www.oasis-open.org/committees/tc_home.php?wg_abbrev=office) |

---

## Not truly open (listed for awareness)

| # | Project | Note |
|---|---------|------|
| 17 | OpenBIOS | Concept/historical — see coreboot/SeaBIOS for active equivalents |
| 29 | OpenSPARC | Historical — released but not actively developed |
| 25 | OpenCAPI | Historical interconnect — superseded by CXL |
| 38 | OpenISA | Philosophy / advocacy, not a codebase |
| 41 | OpenTracing | Archived — merged into OpenTelemetry |
| 42 | OpenCensus | Archived — merged into OpenTelemetry |
| 90 | OpenAssistant | Archived — training data remains available |
| 91 | OpenRouter | Commercial API proxy — source not open |
| 92 | **OpenAI** | **Not OSI open source** — important AI platform but proprietary |
| 60 | OpenQRM | Legacy, low activity |

---

## Project deep-dives

Detailed contribution guides in [`projects/`](projects/):

| File | Project |
|------|---------|
| [opentelemetry.md](projects/opentelemetry.md) | OpenTelemetry |
| [openbmc.md](projects/openbmc.md) | OpenBMC |
| [opentofu.md](projects/opentofu.md) | OpenTofu |
| [opencv.md](projects/opencv.md) | OpenCV |
| [open-policy-agent.md](projects/open-policy-agent.md) | OPA |
| [opensearch.md](projects/opensearch.md) | OpenSearch |

---

## Ontology

The projects in this repo form a **knowledge graph**, not just a flat list.

The graph IS the live ontology (Apache AGE / Cypher). OWL export is inspection-only.

```
Stack Layer (order) → Projects at that layer → Edges between them
```

Key edge types: `RUNS_ON`, `DEPENDS_ON`, `COMPLEMENTS`, `SUPERSEDES`, `MERGES_INTO`, `IMPLEMENTS_SPEC`, `TEACHES`, `IN_TIER`

See [`ontology/`](ontology/) for:
- [`ontology/README.md`](ontology/README.md) — full ontology design and node/edge reference
- [`ontology/seed_concepts.json`](ontology/seed_concepts.json) — hand-authored taxonomy (stack layers, skills, foundations, concepts)
- [`ontology/relationships.json`](ontology/relationships.json) — known edges between specific projects
- [`ontology/schema.cypher`](ontology/schema.cypher) — Apache AGE DDL + query examples
- [`ontology/bootstrap.cypher`](ontology/bootstrap.cypher) — one-time graph init
- [`ontology/export.py`](ontology/export.py) — generates `open_star.owl` for Protégé (never edit the OWL directly)

---

## My journey

Track contributions in [`MY_JOURNEY.md`](MY_JOURNEY.md).

## Contributing to this list

See [`CONTRIBUTING.md`](CONTRIBUTING.md).

## Discovery script

```bash
python3 scripts/discover.py --min-stars 500 --topic kubernetes
python3 scripts/discover.py --token <github-pat> --min-stars 100 --json
```
