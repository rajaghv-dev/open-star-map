---
name: ONNX
url: https://github.com/onnx/onnx
license: Apache-2.0
language: Python, C++, Protobuf
difficulty: intermediate
status: active
---

## What it does

Standard format for ML model representation and interoperability. Export a model from PyTorch or TensorFlow, deploy it with OpenVINO, TensorRT, or ONNX Runtime. The glue layer between training frameworks and inference engines.

## Why contribute

- Teaches ML compiler/IR concepts: graph representation, operator specs, shape inference
- Python-first codebase with C++ core — good for mixed-language skills
- Wide ecosystem: every major ML framework and hardware vendor uses ONNX
- Clear operator spec process — writing a new operator spec is self-contained

## Dev environment setup

```bash
git clone https://github.com/onnx/onnx
cd onnx
pip install -e ".[reference]"

# Verify
python -c "import onnx; print(onnx.version.version)"

# Run tests
pytest onnx/test/
```

## Where to find good first issues

- https://github.com/onnx/onnx/labels/good%20first%20issue
- Operator documentation improvements
- Adding shape inference tests for existing operators

## Community

- Slack: https://lfaifoundation.slack.com → `#onnx`
- Working groups: https://github.com/onnx/onnx/blob/main/community/working-groups.md
- SIG meetings: listed in the community folder

## Learning resources

- Operator spec: https://onnx.ai/onnx/operators/
- ONNX IR spec: https://github.com/onnx/onnx/blob/main/docs/IR.md
- Demo chain: PyTorch → ONNX export → OpenVINO inference → OpenTelemetry latency trace
