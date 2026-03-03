
# Matthews Resonance Framework

Deterministic nonlinear phase-ratio stabilization system with triune harmonic feedback.

## Included Scripts

- matthews_framework.py — Core ODE system and utilities
- boundary_sweep_pair.py — Pair capture boundary test
- plug_pull_test.py — Remove ε and κ to verify causality
- noise_test.py — Stochastic noise robustness test

## Setup

python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt

## Run

python boundary_sweep_pair.py
python plug_pull_test.py
python noise_test.py

Outputs are written to ./out/

Patent Pending.
