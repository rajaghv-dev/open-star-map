---
name: OpenAPI
url: https://github.com/OAI/OpenAPI-Specification
license: Apache-2.0
language: YAML/JSON (spec), multi-language tooling
difficulty: beginner
status: active
---

## What it does

The industry standard for describing REST APIs — schemas, endpoints, auth, parameters, responses — in a machine-readable YAML/JSON document. Everything downstream (client SDKs, server stubs, docs, mocking, validation, testing) generates from it. Governed by the OpenAPI Initiative under the Linux Foundation.

## Why contribute

- Teaches API design: versioning, schema composition, content negotiation, security schemes
- Spec contributions are documentation/prose — no complex build setup
- Tooling ecosystem (OpenAPI Generator, Spectral, etc.) has many beginner-friendly issues
- Used everywhere: every major cloud vendor, Kubernetes, AWS, GitHub APIs are described in OpenAPI

## Dev environment setup

```bash
# Spec repo — text editing + JSON Schema validation
git clone https://github.com/OAI/OpenAPI-Specification
cd OpenAPI-Specification

# Validate a spec file:
npm install -g @apidevtools/swagger-cli
swagger-cli validate examples/v3.0/petstore.yaml

# OpenAPI Generator (Java, generates clients/servers):
git clone https://github.com/OpenAPITools/openapi-generator
cd openapi-generator
mvn package -DskipTests

# Spectral (TypeScript, linting rules):
git clone https://github.com/stoplightio/spectral
cd spectral
npm install && npm test
```

## Where to find good first issues

- Spec: https://github.com/OAI/OpenAPI-Specification/issues?q=label%3A%22good+first+issue%22
- OpenAPI Generator: https://github.com/OpenAPITools/openapi-generator/labels/good%20first%20issue
- Improving generated code for a specific language template

## Community

- Slack: https://communityinviter.com/apps/open-api/openapi-initiative
- TDC (Technical Developer Community): https://www.openapis.org/participate/how-to-contribute
- GitHub Discussions: https://github.com/OAI/OpenAPI-Specification/discussions

## Learning resources

- Spec: https://spec.openapis.org/oas/latest.html
- Learn OpenAPI: https://learn.openapis.org/
- Demo chain: OpenAPI spec → OpenAPI Generator → client SDK → OpenTelemetry instrumented calls
