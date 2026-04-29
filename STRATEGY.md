# STRATEGY.md — Best 70 personal control plane

> *Your stack should not be "one open-source project." It should be an open-source control plane: Linux + containers + observability + policy + AI frameworks + agent orchestration + hardware/firmware validation.*

The 70 projects to learn deeply and contribute to first, organised by the layer they operate at. Pulled out of `README.md` so the README can stay focused on map + navigation.

---

## Systems foundation
| Project | Role | License | Difficulty |
|---------|------|---------|------------|
| Linux kernel | OS foundation | GPL-2.0 | Advanced |
| GCC | Compiler | GPL-3.0 | Advanced |
| LLVM | Compiler infra | Apache-2.0 | Advanced |
| QEMU | Emulator/VM | GPL-2.0 | Advanced |
| KVM | Virtualization | GPL-2.0 | Advanced |

## Languages
| Project | Role | License | Difficulty |
|---------|------|---------|------------|
| Python / CPython | Language | PSF-2.0 | Intermediate |
| R | Statistical language | GPL-2.0 | Intermediate |
| Rust | Language | Apache-2.0 / MIT | Intermediate |
| Go | Language | BSD-3 | Intermediate |
| Java / OpenJDK | Language/runtime | GPL-2.0 | Advanced |
| Node.js | JS runtime | MIT | Intermediate |

## AI/ML core
| Project | Role | License | Difficulty |
|---------|------|---------|------------|
| PyTorch | Deep learning | BSD | Intermediate |
| TensorFlow | Deep learning | Apache-2.0 | Intermediate |
| JAX | ML/autodiff | Apache-2.0 | Advanced |
| ONNX | Model format | Apache-2.0 | Intermediate |
| OpenVINO | Inference optimization | Apache-2.0 | Intermediate |
| Apache TVM | ML compiler | Apache-2.0 | Advanced |
| MLIR | Compiler infra | Apache-2.0 | Advanced |
| NumPy | Numerical computing | BSD | Beginner |
| pandas | Dataframes | BSD | Beginner |
| scikit-learn | Classical ML | BSD | Beginner |
| Ray | Distributed compute | Apache-2.0 | Intermediate |

## LLM, agents, RAG, evaluation
| Project | Role | License | Difficulty |
|---------|------|---------|------------|
| Hugging Face Transformers | LLM/NLP framework | Apache-2.0 | Beginner |
| LangChain | LLM app framework | MIT | Beginner |
| LangGraph | Agent orchestration | MIT | Beginner |
| LlamaIndex | RAG/data framework | MIT | Beginner |
| Haystack | RAG/search framework | Apache-2.0 | Beginner |
| DSPy | LLM programming | MIT | Intermediate |
| vLLM | LLM serving | Apache-2.0 | Intermediate |
| llama.cpp | Local LLM inference | MIT | Intermediate |
| Ollama | Local LLM runtime | MIT | Beginner |
| RAGAS | RAG evaluation | Apache-2.0 | Beginner |
| OpenCompass | LLM evaluation | Apache-2.0 | Beginner |

## Cloud, containers, orchestration
| Project | Role | License | Difficulty |
|---------|------|---------|------------|
| Kubernetes | Container orchestration | Apache-2.0 | Advanced |
| containerd | Container runtime | Apache-2.0 | Intermediate |
| Podman | Containers (rootless) | Apache-2.0 | Intermediate |
| Helm | Kubernetes packaging | Apache-2.0 | Beginner |
| Argo CD | GitOps deployment | Apache-2.0 | Intermediate |
| Cilium | eBPF networking/security | Apache-2.0 | Advanced |
| Envoy | Proxy/service mesh | Apache-2.0 | Advanced |
| MLflow | ML lifecycle | Apache-2.0 | Beginner |
| Kubeflow | ML on Kubernetes | Apache-2.0 | Intermediate |

## Observability
| Project | Role | License | Difficulty |
|---------|------|---------|------------|
| OpenTelemetry | Observability standard | Apache-2.0 | Beginner |
| Prometheus | Metrics | Apache-2.0 | Intermediate |
| Grafana | Visualization | AGPL-3.0 | Beginner |
| Loki | Logs | AGPL-3.0 | Intermediate |
| OpenSearch | Search/log analytics | Apache-2.0 | Intermediate |
| bpftrace | eBPF tracing | Apache-2.0 | Advanced |

## Security, policy, compliance, identity
| Project | Role | License | Difficulty |
|---------|------|---------|------------|
| OpenSSL | Crypto/TLS | Apache-2.0 | Advanced |
| OpenSSH | Secure shell | BSD | Advanced |
| OpenSCAP | Compliance scanning | LGPL-2.1 | Intermediate |
| Open Policy Agent | Policy-as-code | Apache-2.0 | Intermediate |
| Keycloak | Identity/IAM | Apache-2.0 | Intermediate |
| OpenFGA | Fine-grained authz | Apache-2.0 | Intermediate |
| OpenBao | Secrets management | MPL-2.0 | Intermediate |

## Hardware, firmware, EDA
| Project | Role | License | Difficulty |
|---------|------|---------|------------|
| OpenBMC | BMC firmware | Apache-2.0 | Advanced |
| OpenSBI | RISC-V firmware | BSD-2 | Advanced |
| Yosys | Synthesis | ISC | Advanced |
| Verilator | HDL simulator | LGPL | Advanced |
| cocotb | HDL testing | BSD | Intermediate |
| OpenROAD | RTL-to-GDS EDA | BSD-3 | Advanced |
| KiCad | PCB/EDA | GPL-3.0 | Intermediate |

## Desktop, media, graphics
| Project | Role | License | Difficulty |
|---------|------|---------|------------|
| KDE Plasma | Desktop | GPL / LGPL | Beginner |
| Wayland | Display protocol | MIT | Advanced |
| FFmpeg | Media processing | LGPL / GPL | Advanced |
| OpenCV | Computer vision | Apache-2.0 | Intermediate |

---

## The open systems control plane — demo chain

```
Silicon RoT     Firmware      Cloud          Containers     Observability
 OpenTitan  →  OpenBMC    →  OpenStack  →   OCI/Kata    →  OpenTelemetry
                                                             OpenSearch
Hardware sim   Inference     Policy         Compliance     Data lineage
 QEMU/KVM   →  ONNX/OpenVINO → OPA       →  OpenSCAP   →  OpenLineage
                                  ↓
              AI workload: PyTorch → ONNX → vLLM/Ollama → LangGraph agent
                                  ↓
              Evaluation:  RAGAS → OpenCompass → MLflow tracking
```
