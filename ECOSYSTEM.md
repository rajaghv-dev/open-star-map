# Ecosystem reference — 500 truly open-source projects

All projects verified: OSI-approved license, public source, active community.
Organized by domain. License abbreviations use SPDX identifiers.

Jump to: [A](#a-languages-runtimes-compilers) · [B](#b-aiml-deep-learning) · [C](#c-llms-agents-rag-evaluation) · [D](#d-cloud-native-containers-orchestration) · [E](#e-observability-logging-tracing-performance) · [F](#f-data-engineering-databases-analytics) · [G](#g-security-identity-compliance-supply-chain) · [H](#h-os-embedded-firmware-hardware-eda) · [I](#i-web-backend-frontend) · [J](#j-developer-tools-cicd-editors) · [K](#k-desktop-graphics-media-robotics-scientific) · [L](#l-additions-2026-04-29) · [Open*](#open-project-map)

---

## A. Languages, runtimes, compilers

| # | Project | Role | License | Link |
|---|---------|------|---------|------|
| 1 | Linux kernel | OS foundation | GPL-2.0 | [kernel.org](https://kernel.org) |
| 2 | GNU C Library (glibc) | C runtime | LGPL-2.1 | [gnu.org](https://www.gnu.org/software/libc/) |
| 3 | musl libc | C runtime (embedded) | MIT | [musl.libc.org](https://musl.libc.org) |
| 4 | GCC | Compiler collection | GPL-3.0 | [gcc.gnu.org](https://gcc.gnu.org) |
| 5 | LLVM | Compiler infrastructure | Apache-2.0 | [llvm.org](https://llvm.org) |
| 6 | Clang | C/C++ compiler | Apache-2.0 | [clang.llvm.org](https://clang.llvm.org) |
| 7 | lld | LLVM linker | Apache-2.0 | [lld.llvm.org](https://lld.llvm.org) |
| 8 | LLDB | LLVM debugger | Apache-2.0 | [lldb.llvm.org](https://lldb.llvm.org) |
| 9 | GDB | GNU debugger | GPL-3.0 | [gnu.org/software/gdb](https://www.gnu.org/software/gdb/) |
| 10 | Python / CPython | Language | PSF-2.0 | [python.org](https://python.org) |
| 11 | PyPy | Python JIT runtime | MIT | [pypy.org](https://pypy.org) |
| 12 | MicroPython | Embedded Python | MIT | [micropython.org](https://micropython.org) |
| 13 | Rust | Language | Apache-2.0 / MIT | [rust-lang.org](https://rust-lang.org) |
| 14 | Cargo | Rust package/build | Apache-2.0 / MIT | [doc.rust-lang.org/cargo](https://doc.rust-lang.org/cargo/) |
| 15 | Go | Language | BSD-3 | [go.dev](https://go.dev) |
| 16 | TinyGo | Embedded Go | BSD-3 | [tinygo.org](https://tinygo.org) |
| 17 | Java / OpenJDK | Language/runtime | GPL-2.0 | [openjdk.org](https://openjdk.org) |
| 18 | Eclipse OpenJ9 | JVM | EPL-2.0 | [github.com/eclipse-openj9](https://github.com/eclipse-openj9/openj9) |
| 19 | Kotlin | Language | Apache-2.0 | [kotlinlang.org](https://kotlinlang.org) |
| 20 | Scala | Language | Apache-2.0 | [scala-lang.org](https://scala-lang.org) |
| 21 | Clojure | Language | EPL-1.0 | [clojure.org](https://clojure.org) |
| 22 | Groovy | Language | Apache-2.0 | [groovy-lang.org](https://groovy-lang.org) |
| 23 | JavaScript / Node.js | Runtime | MIT | [nodejs.org](https://nodejs.org) |
| 24 | TypeScript | Language | Apache-2.0 | [typescriptlang.org](https://typescriptlang.org) |
| 25 | Deno | JS/TS runtime | MIT | [deno.land](https://deno.land) |
| 26 | Bun | JS runtime/toolchain | MIT | [bun.sh](https://bun.sh) |
| 27 | PHP | Language | PHP-3.0 | [php.net](https://php.net) |
| 28 | Ruby | Language | BSD-2 | [ruby-lang.org](https://ruby-lang.org) |
| 29 | Perl | Language | GPL / Artistic | [perl.org](https://perl.org) |
| 30 | Lua | Language | MIT | [lua.org](https://lua.org) |
| 31 | LuaJIT | JIT runtime | MIT | [luajit.org](https://luajit.org) |
| 32 | R | Statistical language | GPL-2.0 | [r-project.org](https://r-project.org) |
| 33 | Julia | Scientific language | MIT | [julialang.org](https://julialang.org) |
| 34 | Erlang/OTP | Runtime/language | Apache-2.0 | [erlang.org](https://erlang.org) |
| 35 | Elixir | Language | Apache-2.0 | [elixir-lang.org](https://elixir-lang.org) |
| 36 | Haskell / GHC | Language/compiler | BSD-3 | [haskell.org](https://haskell.org) |
| 37 | OCaml | Language | LGPL-2.1 | [ocaml.org](https://ocaml.org) |
| 38 | Zig | Language | MIT | [ziglang.org](https://ziglang.org) |
| 39 | Nim | Language | MIT | [nim-lang.org](https://nim-lang.org) |
| 40 | Crystal | Language | Apache-2.0 | [crystal-lang.org](https://crystal-lang.org) |
| 41 | SWI-Prolog | Logic programming | BSD | [swi-prolog.org](https://swi-prolog.org) |
| 42 | Guile | Scheme runtime | LGPL-3.0 | [gnu.org/software/guile](https://www.gnu.org/software/guile/) |
| 43 | Racket | Language | Apache-2.0 | [racket-lang.org](https://racket-lang.org) |
| 44 | Bash | Shell | GPL-3.0 | [gnu.org/software/bash](https://www.gnu.org/software/bash/) |
| 45 | Zsh | Shell | MIT-like | [zsh.org](https://zsh.org) |
| 46 | Fish shell | Shell | GPL-2.0 | [fishshell.com](https://fishshell.com) |
| 47 | PowerShell | Shell | MIT | [github.com/PowerShell](https://github.com/PowerShell/PowerShell) |
| 48 | WebAssembly / WABT | Bytecode tooling | Apache-2.0 | [github.com/WebAssembly/wabt](https://github.com/WebAssembly/wabt) |
| 49 | Wasmtime | WASM runtime | Apache-2.0 | [wasmtime.dev](https://wasmtime.dev) |
| 50 | WasmEdge | WASM runtime | Apache-2.0 | [wasmedge.org](https://wasmedge.org) |

---

## B. AI/ML deep learning

| # | Project | Role | License | Link |
|---|---------|------|---------|------|
| 51 | PyTorch | Deep learning | BSD | [pytorch.org](https://pytorch.org) |
| 52 | TorchVision | Vision | BSD | [github.com/pytorch/vision](https://github.com/pytorch/vision) |
| 53 | TorchAudio | Audio | BSD | [github.com/pytorch/audio](https://github.com/pytorch/audio) |
| 54 | TorchText | NLP | BSD | [github.com/pytorch/text](https://github.com/pytorch/text) |
| 55 | PyTorch Lightning | Training framework | Apache-2.0 | [lightning.ai](https://lightning.ai) |
| 56 | TensorFlow | Deep learning | Apache-2.0 | [tensorflow.org](https://tensorflow.org) |
| 57 | Keras | Deep learning API | Apache-2.0 | [keras.io](https://keras.io) |
| 58 | JAX | ML/autodiff | Apache-2.0 | [github.com/google/jax](https://github.com/google/jax) |
| 59 | Flax | JAX neural nets | Apache-2.0 | [github.com/google/flax](https://github.com/google/flax) |
| 60 | Haiku | JAX neural nets | Apache-2.0 | [github.com/google-deepmind/dm-haiku](https://github.com/google-deepmind/dm-haiku) |
| 61 | MXNet | Deep learning | Apache-2.0 | [mxnet.apache.org](https://mxnet.apache.org) |
| 62 | ONNX | Model format standard | Apache-2.0 | [github.com/onnx/onnx](https://github.com/onnx/onnx) |
| 63 | ONNX Runtime | Inference runtime | MIT | [github.com/microsoft/onnxruntime](https://github.com/microsoft/onnxruntime) |
| 64 | OpenVINO | Inference optimization | Apache-2.0 | [github.com/openvinotoolkit/openvino](https://github.com/openvinotoolkit/openvino) |
| 65 | Apache TVM | ML compiler | Apache-2.0 | [tvm.apache.org](https://tvm.apache.org) |
| 66 | IREE | ML compiler/runtime | Apache-2.0 | [github.com/iree-org/iree](https://github.com/iree-org/iree) |
| 67 | XLA | ML compiler | Apache-2.0 | [github.com/openxla/xla](https://github.com/openxla/xla) |
| 68 | OpenXLA | ML compiler ecosystem | Apache-2.0 | [github.com/openxla](https://github.com/openxla) |
| 69 | MLIR | Compiler infrastructure | Apache-2.0 | [mlir.llvm.org](https://mlir.llvm.org) |
| 70 | NumPy | Numerical computing | BSD | [numpy.org](https://numpy.org) |
| 71 | SciPy | Scientific computing | BSD | [scipy.org](https://scipy.org) |
| 72 | scikit-learn | Classical ML | BSD | [scikit-learn.org](https://scikit-learn.org) |
| 73 | pandas | Dataframes | BSD | [pandas.pydata.org](https://pandas.pydata.org) |
| 74 | Polars | Fast dataframes | MIT | [pola.rs](https://pola.rs) |
| 75 | Dask | Parallel Python | BSD | [dask.org](https://dask.org) |
| 76 | Ray | Distributed compute | Apache-2.0 | [ray.io](https://ray.io) |
| 77 | XGBoost | Gradient boosting | Apache-2.0 | [xgboost.ai](https://xgboost.ai) |
| 78 | LightGBM | Gradient boosting | MIT | [github.com/microsoft/LightGBM](https://github.com/microsoft/LightGBM) |
| 79 | CatBoost | Gradient boosting | Apache-2.0 | [catboost.ai](https://catboost.ai) |
| 80 | Statsmodels | Statistics | BSD | [statsmodels.org](https://statsmodels.org) |
| 81 | Numba | JIT compilation | BSD | [numba.pydata.org](https://numba.pydata.org) |
| 82 | CuPy | GPU NumPy | MIT | [cupy.dev](https://cupy.dev) |
| 83 | RAPIDS cuDF | GPU dataframe | Apache-2.0 | [rapids.ai](https://rapids.ai) |
| 84 | RAPIDS cuML | GPU ML | Apache-2.0 | [rapids.ai](https://rapids.ai) |
| 85 | Horovod | Distributed training | Apache-2.0 | [github.com/horovod/horovod](https://github.com/horovod/horovod) |
| 86 | DeepSpeed | Distributed training | Apache-2.0 | [github.com/microsoft/DeepSpeed](https://github.com/microsoft/DeepSpeed) |
| 87 | Megatron-LM | Large-model training | BSD | [github.com/NVIDIA/Megatron-LM](https://github.com/NVIDIA/Megatron-LM) |
| 88 | Colossal-AI | Distributed training | Apache-2.0 | [github.com/hpcaitech/ColossalAI](https://github.com/hpcaitech/ColossalAI) |
| 89 | FairScale | Distributed training | BSD | [github.com/facebookresearch/fairscale](https://github.com/facebookresearch/fairscale) |
| 90 | Optuna | Hyperparameter tuning | MIT | [optuna.org](https://optuna.org) |
| 91 | Hyperopt | Hyperparameter tuning | BSD | [github.com/hyperopt/hyperopt](https://github.com/hyperopt/hyperopt) |
| 92 | MLflow | ML lifecycle | Apache-2.0 | [mlflow.org](https://mlflow.org) |
| 93 | Kubeflow | ML on Kubernetes | Apache-2.0 | [kubeflow.org](https://kubeflow.org) |
| 94 | Metaflow | ML workflow | Apache-2.0 | [metaflow.org](https://metaflow.org) |
| 95 | Kedro | ML/data pipeline | Apache-2.0 | [kedro.org](https://kedro.org) |
| 96 | Feast | Feature store | Apache-2.0 | [feast.dev](https://feast.dev) |
| 97 | Evidently AI | ML monitoring | Apache-2.0 | [evidentlyai.com](https://evidentlyai.com) |
| 98 | Alibi | Explainability | Apache-2.0 | [github.com/SeldonIO/alibi](https://github.com/SeldonIO/alibi) |
| 99 | Captum | PyTorch explainability | BSD | [captum.ai](https://captum.ai) |
| 100 | Opacus | Differential privacy | Apache-2.0 | [opacus.ai](https://opacus.ai) |

---

## C. LLMs, agents, RAG, evaluation

| # | Project | Role | License | Link |
|---|---------|------|---------|------|
| 101 | Hugging Face Transformers | LLM/NLP framework | Apache-2.0 | [github.com/huggingface/transformers](https://github.com/huggingface/transformers) |
| 102 | Hugging Face Datasets | Dataset library | Apache-2.0 | [github.com/huggingface/datasets](https://github.com/huggingface/datasets) |
| 103 | Hugging Face Tokenizers | Tokenizers | Apache-2.0 | [github.com/huggingface/tokenizers](https://github.com/huggingface/tokenizers) |
| 104 | Hugging Face Accelerate | Training/inference | Apache-2.0 | [github.com/huggingface/accelerate](https://github.com/huggingface/accelerate) |
| 105 | PEFT | Parameter-efficient fine-tuning | Apache-2.0 | [github.com/huggingface/peft](https://github.com/huggingface/peft) |
| 106 | TRL | RLHF/SFT tooling | Apache-2.0 | [github.com/huggingface/trl](https://github.com/huggingface/trl) |
| 107 | Sentence Transformers | Embeddings | Apache-2.0 | [sbert.net](https://sbert.net) |
| 108 | spaCy | NLP | MIT | [spacy.io](https://spacy.io) |
| 109 | NLTK | NLP | Apache-2.0 | [nltk.org](https://nltk.org) |
| 110 | Gensim | NLP/topic modeling | LGPL-2.1 | [radimrehurek.com/gensim](https://radimrehurek.com/gensim/) |
| 111 | LangChain | LLM app framework | MIT | [github.com/langchain-ai/langchain](https://github.com/langchain-ai/langchain) |
| 112 | LangGraph | Agent orchestration | MIT | [github.com/langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) |
| 113 | LlamaIndex | RAG/data framework | MIT | [llamaindex.ai](https://llamaindex.ai) |
| 114 | Haystack | RAG/search framework | Apache-2.0 | [haystack.deepset.ai](https://haystack.deepset.ai) |
| 115 | Semantic Kernel | Agent framework | MIT | [github.com/microsoft/semantic-kernel](https://github.com/microsoft/semantic-kernel) |
| 116 | AutoGen | Multi-agent framework | MIT | [github.com/microsoft/autogen](https://github.com/microsoft/autogen) |
| 117 | CrewAI | Multi-agent framework | MIT | [github.com/crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) |
| 118 | DSPy | LLM programming/optimization | MIT | [github.com/stanfordnlp/dspy](https://github.com/stanfordnlp/dspy) |
| 119 | Guidance | LLM control | MIT | [github.com/guidance-ai/guidance](https://github.com/guidance-ai/guidance) |
| 120 | Outlines | Structured generation | Apache-2.0 | [github.com/outlines-dev/outlines](https://github.com/outlines-dev/outlines) |
| 121 | Instructor | Structured LLM outputs | MIT | [github.com/jxnl/instructor](https://github.com/jxnl/instructor) |
| 122 | Guardrails AI | LLM validation | Apache-2.0 | [guardrailsai.com](https://guardrailsai.com) |
| 123 | LiteLLM | LLM API gateway | MIT | [github.com/BerriAI/litellm](https://github.com/BerriAI/litellm) |
| 124 | vLLM | LLM serving | Apache-2.0 | [github.com/vllm-project/vllm](https://github.com/vllm-project/vllm) |
| 125 | llama.cpp | Local LLM inference | MIT | [github.com/ggerganov/llama.cpp](https://github.com/ggerganov/llama.cpp) |
| 126 | Ollama | Local LLM runtime | MIT | [github.com/ollama/ollama](https://github.com/ollama/ollama) |
| 127 | OpenWebUI | Local LLM UI | MIT | [github.com/open-webui/open-webui](https://github.com/open-webui/open-webui) |
| 128 | text-generation-inference | LLM serving | Apache-2.0 | [github.com/huggingface/text-generation-inference](https://github.com/huggingface/text-generation-inference) |
| 129 | SGLang | LLM serving/runtime | Apache-2.0 | [github.com/sgl-project/sglang](https://github.com/sgl-project/sglang) |
| 130 | LMDeploy | LLM deployment | Apache-2.0 | [github.com/InternLM/lmdeploy](https://github.com/InternLM/lmdeploy) |
| 131 | GPT4All | Local LLM ecosystem | MIT | [github.com/nomic-ai/gpt4all](https://github.com/nomic-ai/gpt4all) |
| 132 | OpenLLM | LLM serving | Apache-2.0 | [github.com/bentoml/OpenLLM](https://github.com/bentoml/OpenLLM) |
| 133 | RAGAS | RAG evaluation | Apache-2.0 | [github.com/explodinggradients/ragas](https://github.com/explodinggradients/ragas) |
| 134 | DeepEval | LLM evaluation | Apache-2.0 | [github.com/confident-ai/deepeval](https://github.com/confident-ai/deepeval) |
| 135 | lm-evaluation-harness | LLM benchmarks | MIT | [github.com/EleutherAI/lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) |
| 136 | OpenCompass | LLM evaluation | Apache-2.0 | [github.com/open-compass/opencompass](https://github.com/open-compass/opencompass) |
| 137 | EleutherAI GPT-NeoX | LLM training | Apache-2.0 | [github.com/EleutherAI/gpt-neox](https://github.com/EleutherAI/gpt-neox) |
| 138 | OpenRLHF | RLHF framework | Apache-2.0 | [github.com/OpenRLHF/OpenRLHF](https://github.com/OpenRLHF/OpenRLHF) |
| 139 | Axolotl | LLM fine-tuning | Apache-2.0 | [github.com/axolotl-ai-cloud/axolotl](https://github.com/axolotl-ai-cloud/axolotl) |
| 140 | Unsloth | Fine-tuning optimization | Apache-2.0 | [github.com/unslothai/unsloth](https://github.com/unslothai/unsloth) |
| 141 | FastChat | Chatbot serving/eval | Apache-2.0 | [github.com/lm-sys/FastChat](https://github.com/lm-sys/FastChat) |
| 142 | Chroma | Vector database | Apache-2.0 | [trychroma.com](https://trychroma.com) |
| 143 | Qdrant | Vector database | Apache-2.0 | [qdrant.tech](https://qdrant.tech) |
| 144 | Milvus | Vector database | Apache-2.0 | [milvus.io](https://milvus.io) |
| 145 | Weaviate | Vector database | BSD-3 | [weaviate.io](https://weaviate.io) |
| 146 | FAISS | Vector search | MIT | [github.com/facebookresearch/faiss](https://github.com/facebookresearch/faiss) |
| 147 | Annoy | Approx nearest neighbor | Apache-2.0 | [github.com/spotify/annoy](https://github.com/spotify/annoy) |
| 148 | hnswlib | Approx nearest neighbor | Apache-2.0 | [github.com/nmslib/hnswlib](https://github.com/nmslib/hnswlib) |
| 149 | txtai | Embeddings/RAG | Apache-2.0 | [github.com/neuml/txtai](https://github.com/neuml/txtai) |
| 150 | OpenCLIP | CLIP training/models | MIT | [github.com/mlfoundations/open_clip](https://github.com/mlfoundations/open_clip) |

---

## D. Cloud native, containers, orchestration

| # | Project | Role | License | Link |
|---|---------|------|---------|------|
| 151 | Kubernetes | Container orchestration | Apache-2.0 | [kubernetes.io](https://kubernetes.io) |
| 152 | containerd | Container runtime | Apache-2.0 | [containerd.io](https://containerd.io) |
| 153 | CRI-O | Container runtime | Apache-2.0 | [cri-o.io](https://cri-o.io) |
| 154 | runc | OCI runtime | Apache-2.0 | [github.com/opencontainers/runc](https://github.com/opencontainers/runc) |
| 155 | BuildKit | Container build | Apache-2.0 | [github.com/moby/buildkit](https://github.com/moby/buildkit) |
| 156 | Docker Engine / Moby | Containers | Apache-2.0 | [mobyproject.org](https://mobyproject.org) |
| 157 | Podman | Containers (rootless) | Apache-2.0 | [podman.io](https://podman.io) |
| 158 | Buildah | Container build | Apache-2.0 | [buildah.io](https://buildah.io) |
| 159 | Skopeo | Image operations | Apache-2.0 | [github.com/containers/skopeo](https://github.com/containers/skopeo) |
| 160 | Helm | Kubernetes packaging | Apache-2.0 | [helm.sh](https://helm.sh) |
| 161 | Kustomize | Kubernetes config | Apache-2.0 | [kustomize.io](https://kustomize.io) |
| 162 | Argo CD | GitOps deployment | Apache-2.0 | [argo-cd.readthedocs.io](https://argo-cd.readthedocs.io) |
| 163 | Argo Workflows | Workflow engine | Apache-2.0 | [argoproj.github.io](https://argoproj.github.io/workflows/) |
| 164 | Flux CD | GitOps | Apache-2.0 | [fluxcd.io](https://fluxcd.io) |
| 165 | Crossplane | Control planes | Apache-2.0 | [crossplane.io](https://crossplane.io) |
| 166 | KubeVirt | VM on Kubernetes | Apache-2.0 | [kubevirt.io](https://kubevirt.io) |
| 167 | Knative | Serverless | Apache-2.0 | [knative.dev](https://knative.dev) |
| 168 | OpenFaaS | Serverless | MIT | [openfaas.com](https://openfaas.com) |
| 169 | Apache OpenWhisk | Serverless | Apache-2.0 | [openwhisk.apache.org](https://openwhisk.apache.org) |
| 170 | Dapr | Distributed app runtime | Apache-2.0 | [dapr.io](https://dapr.io) |
| 171 | Istio | Service mesh | Apache-2.0 | [istio.io](https://istio.io) |
| 172 | Linkerd | Service mesh | Apache-2.0 | [linkerd.io](https://linkerd.io) |
| 173 | Envoy | Proxy | Apache-2.0 | [envoyproxy.io](https://envoyproxy.io) |
| 174 | Cilium | eBPF networking/security | Apache-2.0 | [cilium.io](https://cilium.io) |
| 175 | Calico | Kubernetes networking | Apache-2.0 | [tigera.io/project-calico](https://www.tigera.io/project-calico/) |
| 176 | Flannel | Kubernetes networking | Apache-2.0 | [github.com/flannel-io/flannel](https://github.com/flannel-io/flannel) |
| 177 | CoreDNS | DNS | Apache-2.0 | [coredns.io](https://coredns.io) |
| 178 | etcd | Distributed KV | Apache-2.0 | [etcd.io](https://etcd.io) |
| 179 | Harbor | Container registry | Apache-2.0 | [goharbor.io](https://goharbor.io) |
| 180 | Rook | Storage orchestration | Apache-2.0 | [rook.io](https://rook.io) |
| 181 | Ceph | Distributed storage | LGPL-2.1 | [ceph.io](https://ceph.io) |
| 182 | Longhorn | Kubernetes storage | Apache-2.0 | [longhorn.io](https://longhorn.io) |
| 183 | OpenEBS | Kubernetes storage | Apache-2.0 | [openebs.io](https://openebs.io) |
| 184 | Velero | Backup/restore | Apache-2.0 | [velero.io](https://velero.io) |
| 185 | KEDA | Event-driven autoscaling | Apache-2.0 | [keda.sh](https://keda.sh) |
| 186 | Cluster API | Kubernetes lifecycle | Apache-2.0 | [cluster-api.sigs.k8s.io](https://cluster-api.sigs.k8s.io) |
| 187 | K3s | Lightweight Kubernetes | Apache-2.0 | [k3s.io](https://k3s.io) |
| 188 | Nomad | Workload scheduler | MPL-2.0 | [nomadproject.io](https://nomadproject.io) |
| 189 | Consul | Service discovery | MPL-2.0 | [consul.io](https://consul.io) |
| 190 | OpenTofu | Infrastructure as code | MPL-2.0 | [opentofu.org](https://opentofu.org) |
| 191 | Ansible | Automation | GPL-3.0 | [ansible.com](https://ansible.com) |
| 192 | Salt | Automation | Apache-2.0 | [saltproject.io](https://saltproject.io) |
| 193 | Puppet | Configuration management | Apache-2.0 | [puppet.com/community](https://puppet.com/community/) |
| 194 | Packer | Image build | MPL-2.0 | [packer.io](https://packer.io) |
| 195 | Nix | Package/build system | MIT | [nixos.org/nix](https://nixos.org/nix/) |
| 196 | Guix | Package/build system | GPL-3.0 | [guix.gnu.org](https://guix.gnu.org) |
| 197 | MLflow | ML lifecycle | Apache-2.0 | [mlflow.org](https://mlflow.org) |
| 198 | Kubeflow | ML on Kubernetes | Apache-2.0 | [kubeflow.org](https://kubeflow.org) |
| 199 | Open Cluster Management | Multicluster Kubernetes | Apache-2.0 | [open-cluster-management.io](https://open-cluster-management.io) |
| 200 | OpenYurt | Edge Kubernetes | Apache-2.0 | [openyurt.io](https://openyurt.io) |

---

## E. Observability, logging, tracing, performance

| # | Project | Role | License | Link |
|---|---------|------|---------|------|
| 201 | OpenTelemetry | Observability standard | Apache-2.0 | [opentelemetry.io](https://opentelemetry.io) |
| 202 | Prometheus | Metrics | Apache-2.0 | [prometheus.io](https://prometheus.io) |
| 203 | Grafana | Visualization | AGPL-3.0 | [grafana.com/oss](https://grafana.com/oss/grafana/) |
| 204 | Loki | Logs | AGPL-3.0 | [grafana.com/oss/loki](https://grafana.com/oss/loki/) |
| 205 | Tempo | Traces | AGPL-3.0 | [grafana.com/oss/tempo](https://grafana.com/oss/tempo/) |
| 206 | Mimir | Metrics backend | AGPL-3.0 | [grafana.com/oss/mimir](https://grafana.com/oss/mimir/) |
| 207 | Jaeger | Distributed tracing | Apache-2.0 | [jaegertracing.io](https://jaegertracing.io) |
| 208 | Zipkin | Distributed tracing | Apache-2.0 | [zipkin.io](https://zipkin.io) |
| 209 | Fluentd | Log collection | Apache-2.0 | [fluentd.org](https://fluentd.org) |
| 210 | Fluent Bit | Log collection | Apache-2.0 | [fluentbit.io](https://fluentbit.io) |
| 211 | Vector | Telemetry pipeline | MPL-2.0 | [vector.dev](https://vector.dev) |
| 212 | OpenSearch | Search/log analytics | Apache-2.0 | [opensearch.org](https://opensearch.org) |
| 213 | OpenSearch Dashboards | Visualization | Apache-2.0 | [opensearch.org](https://opensearch.org) |
| 214 | Netdata | System monitoring | GPL-3.0 | [netdata.cloud](https://netdata.cloud) |
| 215 | VictoriaMetrics | Metrics database | Apache-2.0 | [victoriametrics.com](https://victoriametrics.com) |
| 216 | InfluxDB OSS | Time-series DB | MIT | [influxdata.com/influxdb](https://influxdata.com/influxdb/) |
| 217 | Telegraf | Metrics agent | MIT | [influxdata.com/telegraf](https://influxdata.com/telegraf/) |
| 218 | Grafana Alloy | Telemetry collector | Apache-2.0 | [grafana.com/oss/alloy](https://grafana.com/oss/alloy/) |
| 219 | bpftrace | eBPF tracing | Apache-2.0 | [bpftrace.io](https://bpftrace.io) |
| 220 | BCC | eBPF tools | Apache-2.0 | [github.com/iovisor/bcc](https://github.com/iovisor/bcc) |
| 221 | Parca | Continuous profiling | Apache-2.0 | [parca.dev](https://parca.dev) |
| 222 | Pixie | Kubernetes observability | Apache-2.0 | [px.dev](https://px.dev) |
| 223 | Kepler | Energy observability | Apache-2.0 | [github.com/sustainable-computing-io/kepler](https://github.com/sustainable-computing-io/kepler) |
| 224 | Kube-state-metrics | Kubernetes metrics | Apache-2.0 | [github.com/kubernetes/kube-state-metrics](https://github.com/kubernetes/kube-state-metrics) |
| 225 | Node Exporter | Linux metrics | Apache-2.0 | [github.com/prometheus/node_exporter](https://github.com/prometheus/node_exporter) |
| 226 | Alertmanager | Alert routing | Apache-2.0 | [github.com/prometheus/alertmanager](https://github.com/prometheus/alertmanager) |
| 227 | OpenMetrics | Metrics format | Apache-2.0 | [github.com/OpenObservability/OpenMetrics](https://github.com/OpenObservability/OpenMetrics) |
| 228 | OpenLIT | LLM observability | Apache-2.0 | [github.com/openlit/openlit](https://github.com/openlit/openlit) |

---

## F. Data engineering, databases, analytics

| # | Project | Role | License | Link |
|---|---------|------|---------|------|
| 229 | PostgreSQL | RDBMS | PostgreSQL | [postgresql.org](https://postgresql.org) |
| 230 | SQLite | Embedded DB | Public domain | [sqlite.org](https://sqlite.org) |
| 231 | MariaDB | RDBMS | GPL-2.0 | [mariadb.org](https://mariadb.org) |
| 232 | Apache Cassandra | NoSQL | Apache-2.0 | [cassandra.apache.org](https://cassandra.apache.org) |
| 233 | Apache HBase | NoSQL | Apache-2.0 | [hbase.apache.org](https://hbase.apache.org) |
| 234 | ClickHouse | OLAP DB | Apache-2.0 | [clickhouse.com](https://clickhouse.com) |
| 235 | DuckDB | Analytical DB | MIT | [duckdb.org](https://duckdb.org) |
| 236 | Valkey | Redis-compatible KV | BSD-3 | [valkey.io](https://valkey.io) |
| 237 | FoundationDB | Distributed DB | Apache-2.0 | [foundationdb.org](https://foundationdb.org) |
| 238 | TiDB | Distributed SQL | Apache-2.0 | [pingcap.com/tidb](https://pingcap.com/tidb/) |
| 239 | YugabyteDB | Distributed SQL | Apache-2.0 | [yugabyte.com](https://yugabyte.com) |
| 240 | Apache Kafka | Event streaming | Apache-2.0 | [kafka.apache.org](https://kafka.apache.org) |
| 241 | Apache Pulsar | Event streaming | Apache-2.0 | [pulsar.apache.org](https://pulsar.apache.org) |
| 242 | NATS | Messaging | Apache-2.0 | [nats.io](https://nats.io) |
| 243 | Apache Spark | Big data | Apache-2.0 | [spark.apache.org](https://spark.apache.org) |
| 244 | Apache Flink | Stream processing | Apache-2.0 | [flink.apache.org](https://flink.apache.org) |
| 245 | Apache Beam | Data processing model | Apache-2.0 | [beam.apache.org](https://beam.apache.org) |
| 246 | Apache Iceberg | Table format | Apache-2.0 | [iceberg.apache.org](https://iceberg.apache.org) |
| 247 | Delta Lake | Table format | Apache-2.0 | [delta.io](https://delta.io) |
| 248 | Apache Airflow | Workflow scheduler | Apache-2.0 | [airflow.apache.org](https://airflow.apache.org) |
| 249 | Dagster | Data orchestration | Apache-2.0 | [dagster.io](https://dagster.io) |
| 250 | dbt Core | Analytics engineering | Apache-2.0 | [getdbt.com](https://getdbt.com) |
| 251 | Apache Superset | BI/dashboard | Apache-2.0 | [superset.apache.org](https://superset.apache.org) |
| 252 | Metabase | BI/dashboard | AGPL-3.0 | [metabase.com](https://metabase.com) |
| 253 | Apache Druid | Real-time analytics | Apache-2.0 | [druid.apache.org](https://druid.apache.org) |
| 254 | OpenLineage | Data lineage | Apache-2.0 | [openlineage.io](https://openlineage.io) |
| 255 | OpenMetadata | Data catalog | Apache-2.0 | [open-metadata.org](https://open-metadata.org) |
| 256 | Great Expectations | Data quality | Apache-2.0 | [greatexpectations.io](https://greatexpectations.io) |
| 257 | Apache OpenDAL | Unified data access | Apache-2.0 | [github.com/apache/opendal](https://github.com/apache/opendal) |
| 258 | Apache OpenNLP | NLP toolkit | Apache-2.0 | [opennlp.apache.org](https://opennlp.apache.org) |
| 259 | OpenTSDB | Time-series database | LGPL-2.1 | [opentsdb.net](http://opentsdb.net) |

---

## G. Security, identity, compliance, supply chain

| # | Project | Role | License | Link |
|---|---------|------|---------|------|
| 260 | OpenSSL | Crypto/TLS | Apache-2.0 | [openssl.org](https://openssl.org) |
| 261 | LibreSSL | Crypto/TLS | OpenSSL/ISC | [libressl.org](https://libressl.org) |
| 262 | OpenSSH | Secure shell | BSD | [openssh.com](https://openssh.com) |
| 263 | GnuPG | Encryption/signing | GPL-3.0 | [gnupg.org](https://gnupg.org) |
| 264 | WireGuard | VPN | GPL-2.0 | [wireguard.com](https://wireguard.com) |
| 265 | OpenVPN | VPN | GPL-2.0 | [openvpn.net](https://openvpn.net) |
| 266 | Suricata | IDS/IPS | GPL-2.0 | [suricata.io](https://suricata.io) |
| 267 | Zeek | Network monitoring | BSD | [zeek.org](https://zeek.org) |
| 268 | Wazuh | SIEM/XDR | GPL-2.0 | [wazuh.com](https://wazuh.com) |
| 269 | Falco | Runtime security | Apache-2.0 | [falco.org](https://falco.org) |
| 270 | Tetragon | eBPF security | Apache-2.0 | [github.com/cilium/tetragon](https://github.com/cilium/tetragon) |
| 271 | Trivy | Vulnerability scanner | Apache-2.0 | [trivy.dev](https://trivy.dev) |
| 272 | Grype | Vulnerability scanner | Apache-2.0 | [github.com/anchore/grype](https://github.com/anchore/grype) |
| 273 | Syft | SBOM generation | Apache-2.0 | [github.com/anchore/syft](https://github.com/anchore/syft) |
| 274 | CycloneDX | SBOM standard | Apache-2.0 | [cyclonedx.org](https://cyclonedx.org) |
| 275 | cosign | Signing | Apache-2.0 | [github.com/sigstore/cosign](https://github.com/sigstore/cosign) |
| 276 | Sigstore | Software signing | Apache-2.0 | [sigstore.dev](https://sigstore.dev) |
| 277 | in-toto | Supply-chain provenance | Apache-2.0 | [in-toto.io](https://in-toto.io) |
| 278 | OpenSSF Scorecard | OSS security score | Apache-2.0 | [github.com/ossf/scorecard](https://github.com/ossf/scorecard) |
| 279 | OpenSCAP | Compliance scanning | LGPL-2.1 | [openscap.org](https://openscap.org) |
| 280 | Lynis | Security audit | GPL-3.0 | [cisofy.com/lynis](https://cisofy.com/lynis/) |
| 281 | OpenVAS / Greenbone CE | Vulnerability scanning | AGPL-3.0 | [greenbone.net](https://greenbone.net) |
| 282 | Keycloak | Identity/IAM | Apache-2.0 | [keycloak.org](https://keycloak.org) |
| 283 | Dex | OIDC identity | Apache-2.0 | [dexidp.io](https://dexidp.io) |
| 284 | Authelia | Authentication/SSO | Apache-2.0 | [authelia.com](https://authelia.com) |
| 285 | Zitadel | Identity | Apache-2.0 | [zitadel.com](https://zitadel.com) |
| 286 | Authentik | Identity | MIT | [goauthentik.io](https://goauthentik.io) |
| 287 | OpenLDAP | Directory | OpenLDAP | [openldap.org](https://openldap.org) |
| 288 | FreeIPA | Identity/domain | GPL-3.0 | [freeipa.org](https://freeipa.org) |
| 289 | Open Policy Agent | Policy-as-code | Apache-2.0 | [openpolicyagent.org](https://openpolicyagent.org) |
| 290 | Kyverno | Kubernetes policy | Apache-2.0 | [kyverno.io](https://kyverno.io) |
| 291 | Gatekeeper | Kubernetes policy (OPA) | Apache-2.0 | [github.com/open-policy-agent/gatekeeper](https://github.com/open-policy-agent/gatekeeper) |
| 292 | OpenFGA | Fine-grained authz | Apache-2.0 | [openfga.dev](https://openfga.dev) |
| 293 | Casbin | Authorization | Apache-2.0 | [casbin.org](https://casbin.org) |
| 294 | OpenBao | Secrets management | MPL-2.0 | [openbao.org](https://openbao.org) |
| 295 | OpenCTI | Cyber-threat intelligence | Apache-2.0 | [github.com/OpenCTI-Platform/opencti](https://github.com/OpenCTI-Platform/opencti) |
| 296 | OpenZiti | Zero-trust networking | Apache-2.0 | [openziti.io](https://openziti.io) |

---

## H. OS, embedded, firmware, hardware, EDA

| # | Project | Role | License | Link |
|---|---------|------|---------|------|
| 297 | Debian | Linux distro | DFSG | [debian.org](https://debian.org) |
| 298 | Fedora | Linux distro | Various | [fedoraproject.org](https://fedoraproject.org) |
| 299 | Arch Linux | Linux distro | Various | [archlinux.org](https://archlinux.org) |
| 300 | openSUSE | Linux distro | Various | [opensuse.org](https://opensuse.org) |
| 301 | Alpine Linux | Linux distro | MIT/GPL | [alpinelinux.org](https://alpinelinux.org) |
| 302 | NixOS | Linux distro | MIT | [nixos.org](https://nixos.org) |
| 303 | FreeBSD | OS | BSD-2/3 | [freebsd.org](https://freebsd.org) |
| 304 | OpenBSD | OS (security) | ISC/BSD | [openbsd.org](https://openbsd.org) |
| 305 | NetBSD | OS | BSD-2/3 | [netbsd.org](https://netbsd.org) |
| 306 | Zephyr RTOS | RTOS | Apache-2.0 | [zephyrproject.org](https://zephyrproject.org) |
| 307 | FreeRTOS | RTOS | MIT | [freertos.org](https://freertos.org) |
| 308 | RTEMS | RTOS | BSD | [rtems.org](https://rtems.org) |
| 309 | seL4 | Microkernel | GPL-2.0 | [sel4.systems](https://sel4.systems) |
| 310 | Yocto Project | Embedded Linux | MIT/GPL | [yoctoproject.org](https://yoctoproject.org) |
| 311 | OpenEmbedded | Embedded Linux build | MIT | [openembedded.org](https://openembedded.org) |
| 312 | Buildroot | Embedded Linux build | GPL-2.0 | [buildroot.org](https://buildroot.org) |
| 313 | OpenWrt | Router/edge OS | GPL-2.0 | [openwrt.org](https://openwrt.org) |
| 314 | U-Boot | Bootloader | GPL-2.0 | [denx.de/wiki/U-Boot](https://denx.de/wiki/U-Boot/) |
| 315 | coreboot | Firmware | GPL-2.0 | [coreboot.org](https://coreboot.org) |
| 316 | Tianocore EDK II | UEFI firmware | BSD-2 | [tianocore.org](https://tianocore.org) |
| 317 | OpenBMC | BMC firmware | Apache-2.0 | [github.com/openbmc/openbmc](https://github.com/openbmc/openbmc) |
| 318 | OpenSBI | RISC-V firmware | BSD-2 | [github.com/riscv-software-src/opensbi](https://github.com/riscv-software-src/opensbi) |
| 319 | OpenOCD | Debug (JTAG/SWD) | GPL-2.0 | [openocd.org](http://openocd.org) |
| 320 | QEMU | Emulator | GPL-2.0 | [qemu.org](https://qemu.org) |
| 321 | KVM | Virtualization | GPL-2.0 | [linux-kvm.org](https://linux-kvm.org) |
| 322 | Xen | Hypervisor | GPL-2.0 | [xenproject.org](https://xenproject.org) |
| 323 | Firecracker | MicroVM | Apache-2.0 | [firecracker-microvm.github.io](https://firecracker-microvm.github.io) |
| 324 | gem5 | Architecture simulator | BSD | [gem5.org](https://gem5.org) |
| 325 | Verilator | HDL simulator | LGPL | [veripool.org/verilator](https://veripool.org/verilator/) |
| 326 | Icarus Verilog | Verilog simulator | GPL-2.0 | [iverilog.icarus.com](http://iverilog.icarus.com) |
| 327 | Yosys | Synthesis | ISC | [yosyshq.net/yosys](https://yosyshq.net/yosys/) |
| 328 | nextpnr | FPGA place-route | ISC | [github.com/YosysHQ/nextpnr](https://github.com/YosysHQ/nextpnr) |
| 329 | SymbiYosys | Formal verification | ISC | [github.com/YosysHQ/sby](https://github.com/YosysHQ/sby) |
| 330 | cocotb | HDL testing | BSD | [cocotb.org](https://cocotb.org) |
| 331 | OpenROAD | RTL-to-GDS | BSD-3 | [theopenroadproject.org](https://theopenroadproject.org) |
| 332 | OpenLane | ASIC flow | Apache-2.0 | [github.com/efabless/openlane](https://github.com/efabless/openlane) |
| 333 | KLayout | Layout viewer/editor | GPL-2.0 | [klayout.de](https://klayout.de) |
| 334 | OpenSTA | Static timing analysis | GPL-3.0 | [github.com/The-OpenROAD-Project/OpenSTA](https://github.com/The-OpenROAD-Project/OpenSTA) |
| 335 | OpenRAM | SRAM compiler | BSD-3 | [github.com/VLSIDA/OpenRAM](https://github.com/VLSIDA/OpenRAM) |
| 336 | OpenTitan | Root-of-trust silicon | Apache-2.0 | [opentitan.org](https://opentitan.org) |
| 337 | RISC-V toolchain | ISA/toolchain | GPL-2.0 | [github.com/riscv-collab/riscv-gnu-toolchain](https://github.com/riscv-collab/riscv-gnu-toolchain) |
| 338 | LiteX | SoC builder | BSD | [github.com/enjoy-digital/litex](https://github.com/enjoy-digital/litex) |
| 339 | OpenAMP | Asymmetric multiprocessing | BSD | [openampproject.org](https://openampproject.org) |
| 340 | OpenThread | Thread networking stack | BSD-3 | [openthread.io](https://openthread.io) |
| 341 | Zephyr RTOS | RTOS | Apache-2.0 | [zephyrproject.org](https://zephyrproject.org) |
| 342 | open62541 | OPC UA implementation | MPL-2.0 | [open62541.org](https://open62541.org) |

---

## I. Web, backend, frontend, app frameworks

| # | Project | Role | License | Link |
|---|---------|------|---------|------|
| 343 | Apache HTTP Server | Web server | Apache-2.0 | [httpd.apache.org](https://httpd.apache.org) |
| 344 | NGINX OSS | Web server | BSD-2 | [nginx.org](https://nginx.org) |
| 345 | Caddy | Web server | Apache-2.0 | [caddyserver.com](https://caddyserver.com) |
| 346 | HAProxy | Load balancer | GPL-2.0 | [haproxy.org](https://haproxy.org) |
| 347 | Traefik Proxy | Reverse proxy | MIT | [traefik.io](https://traefik.io) |
| 348 | Django | Python web | BSD | [djangoproject.com](https://djangoproject.com) |
| 349 | Flask | Python web | BSD | [flask.palletsprojects.com](https://flask.palletsprojects.com) |
| 350 | FastAPI | Python web | MIT | [fastapi.tiangolo.com](https://fastapi.tiangolo.com) |
| 351 | Starlette | Python web | BSD | [starlette.io](https://starlette.io) |
| 352 | Celery | Task queue | BSD | [celeryq.dev](https://celeryq.dev) |
| 353 | Express.js | Node web | MIT | [expressjs.com](https://expressjs.com) |
| 354 | Fastify | Node web | MIT | [fastify.io](https://fastify.io) |
| 355 | NestJS | Node framework | MIT | [nestjs.com](https://nestjs.com) |
| 356 | React | UI framework | MIT | [react.dev](https://react.dev) |
| 357 | Vue.js | UI framework | MIT | [vuejs.org](https://vuejs.org) |
| 358 | Angular | UI framework | MIT | [angular.dev](https://angular.dev) |
| 359 | Svelte | UI framework | MIT | [svelte.dev](https://svelte.dev) |
| 360 | Next.js | Web framework | MIT | [nextjs.org](https://nextjs.org) |
| 361 | Nuxt | Web framework | MIT | [nuxt.com](https://nuxt.com) |
| 362 | Astro | Web framework | MIT | [astro.build](https://astro.build) |
| 363 | Vite | Build tool | MIT | [vitejs.dev](https://vitejs.dev) |
| 364 | esbuild | Build tool | MIT | [esbuild.github.io](https://esbuild.github.io) |
| 365 | Tailwind CSS | CSS framework | MIT | [tailwindcss.com](https://tailwindcss.com) |
| 366 | Rails | Ruby web | MIT | [rubyonrails.org](https://rubyonrails.org) |
| 367 | Phoenix | Elixir web | MIT | [phoenixframework.org](https://phoenixframework.org) |

---

## J. Developer tools, CI/CD, editors, testing

| # | Project | Role | License | Link |
|---|---------|------|---------|------|
| 368 | Git | Version control | GPL-2.0 | [git-scm.com](https://git-scm.com) |
| 369 | GitLab CE | Dev platform | MIT | [gitlab.com/gitlab-org/gitlab-foss](https://gitlab.com/gitlab-org/gitlab-foss) |
| 370 | Gitea | Git hosting | MIT | [gitea.io](https://gitea.io) |
| 371 | Forgejo | Git hosting | MIT | [forgejo.org](https://forgejo.org) |
| 372 | Jenkins | CI/CD | MIT | [jenkins.io](https://jenkins.io) |
| 373 | Tekton | CI/CD (Kubernetes-native) | Apache-2.0 | [tekton.dev](https://tekton.dev) |
| 374 | Drone CI | CI/CD | Apache-2.0 | [drone.io](https://drone.io) |
| 375 | Zuul CI | Gated CI/CD | Apache-2.0 | [zuul-ci.org](https://zuul-ci.org) |
| 376 | SonarQube Community | Code quality | LGPL-3.0 | [sonarsource.com/community](https://www.sonarsource.com/community/) |
| 377 | Semgrep CE | Static analysis | LGPL-2.1 | [semgrep.dev](https://semgrep.dev) |
| 378 | ESLint | JS linting | MIT | [eslint.org](https://eslint.org) |
| 379 | Ruff | Python lint/format | MIT | [astral.sh/ruff](https://astral.sh/ruff/) |
| 380 | Black | Python formatting | MIT | [black.readthedocs.io](https://black.readthedocs.io) |
| 381 | mypy | Python typing | MIT | [mypy-lang.org](https://mypy-lang.org) |
| 382 | pytest | Python testing | MIT | [pytest.org](https://pytest.org) |
| 383 | JUnit | Java testing | EPL-2.0 | [junit.org](https://junit.org) |
| 384 | Jest | JS testing | MIT | [jestjs.io](https://jestjs.io) |
| 385 | Playwright | Browser automation | Apache-2.0 | [playwright.dev](https://playwright.dev) |
| 386 | Selenium | Browser automation | Apache-2.0 | [selenium.dev](https://selenium.dev) |
| 387 | Bruno | API testing | MIT | [usebruno.com](https://usebruno.com) |
| 388 | Code-OSS / VSCodium | Editor | MIT | [vscodium.com](https://vscodium.com) |
| 389 | Eclipse IDE | IDE | EPL-2.0 | [eclipse.org/ide](https://eclipse.org/ide/) |
| 390 | Eclipse Theia | Cloud/desktop IDE | EPL-2.0 | [theia-ide.org](https://theia-ide.org) |
| 391 | Neovim | Editor | Apache-2.0 | [neovim.io](https://neovim.io) |
| 392 | Vim | Editor | Vim | [vim.org](https://vim.org) |
| 393 | Emacs | Editor | GPL-3.0 | [gnu.org/software/emacs](https://www.gnu.org/software/emacs/) |
| 394 | tmux | Terminal multiplexer | ISC | [github.com/tmux/tmux](https://github.com/tmux/tmux) |
| 395 | Open VSX | Extension registry | EPL-2.0 | [open-vsx.org](https://open-vsx.org) |
| 396 | OpenRewrite | Automated refactoring | Apache-2.0 | [docs.openrewrite.org](https://docs.openrewrite.org) |
| 397 | OpenAPI Generator | Client/server generation | Apache-2.0 | [openapi-generator.tech](https://openapi-generator.tech) |

---

## K. Desktop, graphics, media, robotics, scientific

| # | Project | Role | License | Link |
|---|---------|------|---------|------|
| 398 | KDE Plasma | Desktop | GPL / LGPL | [kde.org](https://kde.org) |
| 399 | GNOME | Desktop | GPL / LGPL | [gnome.org](https://gnome.org) |
| 400 | XFCE | Desktop | GPL / LGPL | [xfce.org](https://xfce.org) |
| 401 | Wayland | Display protocol | MIT | [wayland.freedesktop.org](https://wayland.freedesktop.org) |
| 402 | Weston | Wayland compositor | MIT | [gitlab.freedesktop.org/wayland/weston](https://gitlab.freedesktop.org/wayland/weston) |
| 403 | Mesa | Graphics stack | MIT | [mesa3d.org](https://mesa3d.org) |
| 404 | GStreamer | Media framework | LGPL-2.0 | [gstreamer.freedesktop.org](https://gstreamer.freedesktop.org) |
| 405 | FFmpeg | Media processing | LGPL / GPL | [ffmpeg.org](https://ffmpeg.org) |
| 406 | VLC | Media player | GPL-2.0 | [videolan.org](https://videolan.org) |
| 407 | OBS Studio | Streaming/recording | GPL-2.0 | [obsproject.com](https://obsproject.com) |
| 408 | Blender | 3D creation | GPL-3.0 | [blender.org](https://blender.org) |
| 409 | FreeCAD | CAD | LGPL-2.0 | [freecad.org](https://freecad.org) |
| 410 | KiCad | EDA/PCB | GPL-3.0 | [kicad.org](https://kicad.org) |
| 411 | Inkscape | Vector graphics | GPL-3.0 | [inkscape.org](https://inkscape.org) |
| 412 | GIMP | Image editing | GPL-3.0 | [gimp.org](https://gimp.org) |
| 413 | LibreOffice | Office suite | MPL-2.0 | [libreoffice.org](https://libreoffice.org) |
| 414 | JupyterLab | Notebooks | BSD | [jupyter.org](https://jupyter.org) |
| 415 | ROS 2 | Robotics OS | Apache-2.0 | [ros.org](https://ros.org) |
| 416 | Gazebo | Robotics simulation | Apache-2.0 | [gazebosim.org](https://gazebosim.org) |
| 417 | OpenCV | Computer vision | Apache-2.0 | [opencv.org](https://opencv.org) |
| 418 | scikit-image | Image processing | BSD | [scikit-image.org](https://scikit-image.org) |
| 419 | VTK | Visualization toolkit | BSD | [vtk.org](https://vtk.org) |
| 420 | ParaView | Scientific visualization | BSD | [paraview.org](https://paraview.org) |
| 421 | OpenFOAM | CFD simulation | GPL-3.0 | [openfoam.org](https://openfoam.org) |
| 422 | OpenModelica | Modeling/simulation | GPL-3.0 | [openmodelica.org](https://openmodelica.org) |
| 423 | Octave | Numerical computing | GPL-3.0 | [octave.org](https://octave.org) |
| 424 | SageMath | Mathematics | GPL-3.0 | [sagemath.org](https://sagemath.org) |
| 425 | QGIS | GIS | GPL-2.0 | [qgis.org](https://qgis.org) |
| 426 | GDAL | Geospatial | MIT | [gdal.org](https://gdal.org) |
| 427 | PostGIS | Spatial database | GPL-2.0 | [postgis.net](https://postgis.net) |
| 428 | OpenDroneMap | Drone photogrammetry | AGPL-3.0 | [opendronemap.org](https://opendronemap.org) |
| 429 | Godot | Game engine | MIT | [godotengine.org](https://godotengine.org) |
| 430 | Bevy | Game engine (Rust) | MIT / Apache-2.0 | [bevyengine.org](https://bevyengine.org) |

---

## L. Additions (2026-04-29)

Networking, telco/RAN, AI agents, film/VFX pipeline, hardware standards.

| # | Project | Role | License | Link |
|---|---------|------|---------|------|
| 431 | OpenFPGA | Open-source FPGA IP / fabric | MIT | [github.com/lnis-uofu/OpenFPGA](https://github.com/lnis-uofu/OpenFPGA) |
| 432 | OpenAirInterface | Open 5G RAN + Core | Apache-2.0 | [openairinterface.org](https://openairinterface.org) |
| 433 | OKD | Kubernetes distro (OpenShift upstream) | Apache-2.0 | [okd.io](https://okd.io) |
| 434 | Open vSwitch (OVS) | Production virtual switch | Apache-2.0 | [openvswitch.org](https://openvswitch.org) |
| 435 | OVN | Virtual networking on OVS | Apache-2.0 | [github.com/ovn-org/ovn](https://github.com/ovn-org/ovn) |
| 436 | OpenConfig | Vendor-neutral network config models | Apache-2.0 | [openconfig.net](https://openconfig.net) |
| 437 | OpenHands | Autonomous coding agent (formerly OpenDevin) | MIT | [github.com/All-Hands-AI/OpenHands](https://github.com/All-Hands-AI/OpenHands) |
| 438 | Open Interpreter | Natural-language code interpreter | AGPL-3.0 | [github.com/OpenInterpreter/open-interpreter](https://github.com/OpenInterpreter/open-interpreter) |
| 439 | OpenUSD | Universal Scene Description (Pixar/ASWF) | TOST (Apache-2.0 derived) | [openusd.org](https://openusd.org) |
| 440 | OpenEXR | HDR image format (ASWF) | BSD-3 | [openexr.com](https://openexr.com) |
| 441 | OpenColorIO | Color management pipeline (ASWF) | BSD-3 | [opencolorio.org](https://opencolorio.org) |
| 442 | OpenZFS | Filesystem / volume manager | CDDL-1.0 | [openzfs.org](https://openzfs.org) |
| 443 | OpenNebula | Open IaaS / hybrid cloud | Apache-2.0 | [opennebula.io](https://opennebula.io) |
| 444 | OpenStreetMap | Open geographic data project | ODbL | [openstreetmap.org](https://openstreetmap.org) |
| 445 | OpenAlex | Open scholarly metadata graph | CC0 | [openalex.org](https://openalex.org) |

---

## Open* project map

The original 100 curated open\* projects, organized by tier and stack layer.

### Strategic tier (track deeply)

| Project | Stack layer | Difficulty | Repo |
|---------|-------------|------------|------|
| OpenTelemetry | Observability (5) | Beginner | [→](https://github.com/open-telemetry) |
| OpenSearch | Observability (5) | Intermediate | [→](https://github.com/opensearch-project/OpenSearch) |
| Open Policy Agent | Security (6) | Intermediate | [→](https://github.com/open-policy-agent/opa) |
| OpenSSF Scorecard | Security (6) | Beginner | [→](https://github.com/ossf/scorecard) |
| OpenSCAP | Security (6) | Intermediate | [→](https://github.com/OpenSCAP/openscap) |
| OpenBMC | Firmware (2) | Advanced | [→](https://github.com/openbmc/openbmc) |
| OpenTitan | Silicon (1) | Advanced | [→](https://github.com/lowRISC/opentitan) |
| OpenROAD | Silicon (1) | Advanced | [→](https://github.com/The-OpenROAD-Project/OpenROAD) |
| OpenStack | Cloud (4) | Intermediate | [→](https://opendev.org/openstack) |
| Kata Containers | Cloud (4) | Advanced | [→](https://github.com/kata-containers/kata-containers) |
| OpenEmbedded | Firmware (2) | Intermediate | [→](https://github.com/openembedded/openembedded-core) |
| ONNX | AI (7) | Intermediate | [→](https://github.com/onnx/onnx) |
| OpenVINO | AI (7) | Intermediate | [→](https://github.com/openvinotoolkit/openvino) |
| OpenCV | AI (7) | Intermediate | [→](https://github.com/opencv/opencv) |
| OpenAPI | Standards | Beginner | [→](https://github.com/OAI/OpenAPI-Specification) |
| OCI / runc | Cloud (4) | Intermediate | [→](https://github.com/opencontainers/runc) |
| OpenChain | Compliance | Beginner | [→](https://openchainproject.org) |
| OpenInfra | Foundation | — | [→](https://openinfra.dev) |
| StarlingX | Edge (4) | Advanced | [→](https://opendev.org/starlingx) |

### Practical tier (build demos now)

| Project | Pairs with | Link |
|---------|-----------|------|
| OpenTelemetry | → OpenSearch | [→](https://github.com/open-telemetry) |
| OpenSearch | → OPA | [→](https://github.com/opensearch-project/OpenSearch) |
| OPA | → OpenSCAP | [→](https://github.com/open-policy-agent/opa) |
| OpenSCAP | → OpenSSF Scorecard | [→](https://github.com/OpenSCAP/openscap) |
| ONNX | → OpenVINO | [→](https://github.com/onnx/onnx) |
| OpenVINO | → OpenCV | [→](https://github.com/openvinotoolkit/openvino) |
| OpenBMC | → OpenTitan | [→](https://github.com/openbmc/openbmc) |
| OpenFeature | standalone | [→](https://github.com/open-feature) |
| OpenAPI | → OpenAPIGenerator | [→](https://github.com/OAI/OpenAPI-Specification) |

### Watchlist tier

OpenTofu · OpenBao · OpenFGA · OpenLineage · OpenMetadata · OpenDataHub · OpenLane · OpenSBI · OpenHW Group · OCP ·
OKD · OpenAirInterface · OpenFPGA · Open vSwitch · OpenConfig · OpenHands · OpenUSD · OpenEXR

### Not truly open (listed for awareness)

| Project | Reason |
|---------|--------|
| OpenAI | Proprietary — not OSI licensed |
| OpenRouter | Commercial API proxy |
| OpenTracing | Archived — merged into OpenTelemetry |
| OpenCensus | Archived — merged into OpenTelemetry |
