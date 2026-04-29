---
name: OpenChain
url: https://github.com/OpenChain-Project
license: CC-BY-4.0 (specs), Apache-2.0 (tooling)
language: Markdown, Python
difficulty: beginner
status: active
---

## What it does

Linux Foundation project that defines the international standard (ISO/IEC 5230) for open-source license compliance programs in organizations. Provides specifications, self-certification questionnaires, reference materials, and tooling to help companies — and increasingly individual maintainers — produce trustworthy SBOMs and license attributions. Aligns with the SBOM/supply-chain security stack (SPDX, CycloneDX, in-toto, Sigstore).

## Why contribute

- Compliance is becoming legally mandated (EU CRA, US EO 14028) — early expertise is valuable
- Spec-driven: contributions are typically text edits, examples, or translations — beginner-friendly
- Connects directly to SuryaOS / hardware-software stack governance
- Multilingual community — translation contributions are accepted and visible

## Dev environment setup

No build required for spec work. Clone the repo, edit Markdown, submit a PR.

```bash
git clone https://github.com/OpenChain-Project/Reference-Material
cd Reference-Material
# Edit the relevant spec or guidance file
```

For tooling sub-projects (e.g., the OpenChain Telco SBOM Guide validator):

```bash
git clone https://github.com/OpenChain-Project/Telco-WG
# Follow per-tool README
```

## Where to find good first issues

- https://github.com/OpenChain-Project/Reference-Material/issues
- Translations: https://github.com/OpenChain-Project/Reference-Material/tree/master/Translations
- New industry guidance docs (Automotive, Telco, AI work groups)

## Community

- Mailing lists: https://lists.openchainproject.org
- Monthly all-hands and work-group calls: https://www.openchainproject.org/community
- Slack: https://www.openchainproject.org/community (invite link)

## Learning resources

- Spec (ISO/IEC 5230): https://www.openchainproject.org/license-compliance
- Self-certification: https://certification.openchainproject.org
- Curriculum: https://www.openchainproject.org/curriculum
- Read order: spec PDF → curriculum slides → telco/automotive guidance
