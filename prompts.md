# prompts.md — LLM prompts for working with this ecosystem

Session prompts for classification, contribution planning, ontology enrichment,
and project discovery. Same pattern as CFP `prompts.md`.

---

## PROMPT_01 — Classify a project into the ontology

```
You are classifying an open-source project into a knowledge graph ontology.
Given the project name, description, and GitHub metadata below, output JSON with:
- stack_layer: one of [silicon, firmware, os-net, cloud, observability, security, ai, data-gov]
- category: one of [languages, ai-ml, llm-agents, cloud-native, observability, data, security, os-firmware, web, devtools, desktop-graphics]
- difficulty: one of [beginner, intermediate, advanced]
- skills: list of 1-3 skills contributed teaches
- complements: list of project names it works well with
- implements_spec: list of specs/standards it implements (empty if none)
- is_oss: true/false (OSI-approved license)
- license_spdx: SPDX license identifier

Project:
Name: {{project_name}}
Description: {{description}}
Language: {{language}}
License: {{license}}
Stars: {{stars}}
Good first issues: {{gfi_count}}
Topics: {{topics}}
```

---

## PROMPT_02 — Find good first issue strategy for a project

```
You are helping a developer plan their first contribution to an open-source project.
Given the project name and the developer's background, suggest:
1. The specific sub-area of the codebase to start in (file path or module name)
2. Type of issue to look for (docs, tests, small bug, new feature)
3. Relevant GitHub label to filter on
4. One concrete thing to read first (file, doc page, ADR)
5. Community channel to join before submitting a PR

Project: {{project_name}}
Developer background: SuryaOS / AI systems / compliance / hardware-software acceleration
Language fluency: Python (expert), Go (intermediate), C++ (intermediate), Rust (learning), SystemVerilog (basic)
```

---

## PROMPT_03 — Verify a project is truly open source

```
Given the following project information, determine if it qualifies as "truly open source":
- License must be OSI-approved (Apache-2.0, MIT, BSD, GPL, LGPL, MPL, EPL, AGPL, ISC, PSF, etc.)
- Source code must be publicly readable
- External contributions must be accepted (has CONTRIBUTING.md or equivalent)
- Last commit within 12 months
- NOT a vendor fork with a closed contribution process

Return JSON:
{
  "is_truly_oss": true/false,
  "license_spdx": "...",
  "license_is_osi": true/false,
  "accepts_contributions": true/false,
  "last_commit_within_year": true/false,
  "disqualifier": "reason if false, else null"
}

Project:
Name: {{project_name}}
License: {{license}}
GitHub URL: {{url}}
Has CONTRIBUTING.md: {{has_contributing}}
Last commit: {{last_commit_date}}
```

---

## PROMPT_04 — Generate a project deep-dive file

```
Generate a contribution guide for an open-source project in this exact Markdown format.
Follow the template precisely. Be specific and accurate — no invented URLs.

---
name: {{project_name}}
url: {{url}}
license: {{license}}
language: {{language}}
difficulty: {{difficulty}}
status: active
---

## What it does
[One paragraph, factual]

## Why contribute
[3-4 bullet points: skills, scale, community quality, uniqueness]

## Dev environment setup
```bash
[Minimal verified steps to get a local build running]
```

## Where to find good first issues
[Specific GitHub label URLs. Specific types of issues that are beginner-friendly]

## Community
[Specific Slack/IRC/mailing list links. Meeting cadence if known]

## Learning resources
[Docs link. Architecture overview. Reading order suggestion]

Project: {{project_name}}
GitHub URL: {{url}}
License: {{license}}
Primary language: {{language}}
```

---

## PROMPT_05 — Score contribution readiness

```
Given the following information about an open-source project, score its contributor-friendliness
on a 0-100 scale. Return JSON with scores and a one-line recommendation.

Scoring rubric:
- good_first_issues (0-25): count of open good-first-issue labeled issues
- documentation (0-20): has CONTRIBUTING.md, CODE_OF_CONDUCT, architecture docs
- community (0-20): active Slack/Discord/mailing list, regular meetings
- activity (0-20): commits in last 30 days, PR response time
- onboarding (0-15): dev setup complexity, CI quality, local test suite

Return:
{
  "total_score": 0-100,
  "breakdown": {
    "good_first_issues": 0-25,
    "documentation": 0-20,
    "community": 0-20,
    "activity": 0-20,
    "onboarding": 0-15
  },
  "recommendation": "one sentence"
}

Project: {{project_name}}
GFI count: {{gfi_count}}
Has CONTRIBUTING.md: {{has_contributing}}
Has CODE_OF_CONDUCT: {{has_coc}}
Community channel: {{community}}
Commits last 30d: {{recent_commits}}
Avg PR response days: {{pr_response}}
Build setup steps: {{setup_complexity}}
```

---

## PROMPT_06 — Map relationships between projects

```
Given two open-source projects, identify their relationship. Return JSON:
{
  "relationship_type": one of [DEPENDS_ON, COMPLEMENTS, SUPERSEDES, MERGES_INTO, IMPLEMENTS_SPEC, PART_OF, NONE],
  "direction": "a→b" or "b→a" or "bidirectional",
  "note": "one sentence explaining the relationship",
  "confidence": "high/medium/low"
}

Project A: {{project_a}}
Project B: {{project_b}}
Context: {{context_if_known}}
```

---

## PROMPT_07 — Generate Cypher for a new project node

```
Generate Apache AGE Cypher statements to add a new project node and its edges
to the open_star_graph knowledge graph.

Use MERGE (not CREATE) to be idempotent. Include:
1. The Project node with all properties
2. RUNS_ON edge to the correct StackLayer
3. IN_TIER edge to the correct Tier
4. GOVERNED_BY edge if foundation is known
5. DEPENDS_ON / COMPLEMENTS / IMPLEMENTS_SPEC edges if known

Graph name: open_star_graph
Node label reference: Project, StackLayer, Tier, Foundation, Spec
Edge type reference: RUNS_ON, IN_TIER, GOVERNED_BY, DEPENDS_ON, COMPLEMENTS, IMPLEMENTS_SPEC

Project to add:
Name: {{project_name}}
URL: {{url}}
License: {{license}}
Language: {{language}}
Difficulty: {{difficulty}}
Stack layer: {{stack_layer_slug}}
Tier: {{tier}}
Foundation: {{foundation_or_null}}
Known relationships: {{relationships}}
```

---

## PROMPT_08 — Session cold-start summary

```
You are starting a new session on the open* repo.
Read the following files in order and summarize the current state in 5 bullet points,
then list the top 3 tasks from SESSION.md:

Files to read: CLAUDE.md, SESSION.md, context.md

After reading, produce:
CURRENT STATE:
• [5 bullets]

TOP 3 TASKS:
1.
2.
3.

Do not start any task until the user confirms which one to work on.
```
