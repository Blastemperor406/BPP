# BPP — Branch Prediction with Perceptrons

Exploring ML-based dynamic branch prediction for RISC-V, using TinyML-inspired techniques small enough to be plausible in hardware.

## Why

Branch mispredictions are one of the main things stalling a deep pipeline. Classic dynamic predictors (2-bit saturating counters, gshare) track short local/global history well but plateau on branches with long-range correlation. Perceptron-based predictors ([Jiménez & Lin, HPCA 2001](https://www.cs.utexas.edu/~lin/papers/hpca01.pdf)) showed a linear model can exploit much longer histories at a hardware budget comparable to table-based schemes — which is exactly the TinyML regime: tiny models, integer arithmetic, hard resource ceilings.

## What's here

| File | Predictor | Idea |
|---|---|---|
| [`Imperical-dynamic.py`](Imperical-dynamic.py) | 2-bit history baseline | Classic finite-state prediction from the last two outcomes |
| [`Intelligent-dynamic.py`](Intelligent-dynamic.py) | Perceptron predictor | Learns a weighted vote over branch history via perceptron updates |

Both are proof-of-concept models running on small hand-made sequences — the goal at this stage is to contrast the two prediction philosophies, not to benchmark them.

## Roadmap

- **Real branch traces** — drive both predictors from actual RISC-V branch streams (e.g. instrumented Spike/QEMU runs or CBP-style trace files) instead of hardcoded sequences.
- **Faithful Jiménez–Lin implementation** — table of perceptrons indexed by PC, global history register, threshold-based training, integer weights.
- **Baselines & metrics** — static, 1-bit, 2-bit, gshare vs. perceptron, compared on accuracy and MPKI (mispredictions per kilo-instruction) under equal storage budgets.
- **TinyML angle** — quantized weights and a hardware-budget accounting (KB of state per predictor) to keep every design implementable.
