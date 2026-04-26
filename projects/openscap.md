---
name: OpenSCAP
url: https://github.com/OpenSCAP/openscap
license: LGPL-2.1
language: C, Python
difficulty: intermediate
status: active
---

## What it does

Open-source implementation of the SCAP (Security Content Automation Protocol) standard. Scans systems against CIS Benchmarks, DISA STIGs, and other security profiles using OVAL and XCCDF content. Generates compliance reports in HTML, XML, and ARF formats. Used in RHEL, Fedora, and enterprise security automation pipelines.

## Why contribute

- Teaches compliance-as-code: OVAL, XCCDF, SCAP data streams, ARF reporting
- C library + Python bindings — clear separation between core and tooling
- Real enterprise impact: every RHEL system uses OpenSCAP for compliance
- Pairs with OPA for a policy-gate + compliance-scan pipeline

## Dev environment setup

```bash
git clone https://github.com/OpenSCAP/openscap
cd openscap

# Dependencies (Fedora/RHEL)
sudo dnf install cmake libxml2-devel libxslt-devel libcurl-devel \
     pcre-devel libacl-devel libselinux-devel bzip2-devel

mkdir build && cd build
cmake ..
make -j$(nproc)

# Run a scan with a SCAP content file
./utils/oscap xccdf eval \
  --profile xccdf_org.ssgproject.content_profile_cis \
  /usr/share/xml/scap/ssg/content/ssg-fedora-ds.xml
```

## Where to find good first issues

- https://github.com/OpenSCAP/openscap/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22
- SCAP Security Guide (content side): https://github.com/ComplianceAsCode/content/labels/good%20first%20issue
- Documentation and Python bindings improvements

## Community

- Mailing list: open-scap-list@redhat.com
- GitHub: https://github.com/OpenSCAP
- SCAP Security Guide (content): https://github.com/ComplianceAsCode/content

## Learning resources

- SCAP overview: https://csrc.nist.gov/projects/security-content-automation-protocol
- XCCDF tutorial: https://www.open-scap.org/resources/documentation/
- Demo chain: `oscap xccdf eval` → ARF report → OPA policy checks results → OpenTelemetry span
- Start with: improving Python binding tests or adding a new OVAL test definition
