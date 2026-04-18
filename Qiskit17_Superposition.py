# ============================================================
#  Code 17: Superposition & Probability Distributions
#  File: 07_superposition.py
#  Requirements: pip install qiskit qiskit-aer matplotlib
# ============================================================
 
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
 
sim = AerSimulator()
 
# ── 7A: Single-qubit superposition ───────────────────────────────────────
qc1 = QuantumCircuit(1, 1)
qc1.h(0)                           # H gate: |0⟩ → (|0⟩+|1⟩)/√2
qc1.measure(0, 0)
 
counts1 = sim.run(qc1, shots=2048).result().get_counts()
print("=== 7A: 1-Qubit Superposition (2048 shots) ===")
print(f"  |0⟩ probability ≈ {counts1.get('0',0)/2048:.3f}")
print(f"  |1⟩ probability ≈ {counts1.get('1',0)/2048:.3f}")
 
# ── 7B: 2-Qubit uniform superposition ────────────────────────────────────
qc2 = QuantumCircuit(2, 2)
qc2.h(0)                           # H on qubit 0
qc2.h(1)                           # H on qubit 1
qc2.measure([0, 1], [0, 1])
# State: (|00⟩+|01⟩+|10⟩+|11⟩)/2 — all 4 basis states equally likely
 
counts2 = sim.run(qc2, shots=4096).result().get_counts()
print("\n=== 7B: 2-Qubit Uniform Superposition (4096 shots) ===")
for state, count in sorted(counts2.items()):
    prob = count / 4096
    bar  = '█' * int(prob * 40)
    print(f"  |{state}⟩: {count:5d} shots  ({prob:.3f})  {bar}")
 
# ── 7C: N-qubit superposition — exponential state space ───────────────────
print("\n=== 7C: Superposition State Counts by Qubit Count ===")
for n in range(1, 5):
    qcN = QuantumCircuit(n, n)
    for i in range(n):
        qcN.h(i)
    qcN.measure(range(n), range(n))
    counts_n = sim.run(qcN, shots=8192).result().get_counts()
    unique_states = len(counts_n)
    expected = 2**n
    print(f"  {n} qubit(s): {unique_states} unique states observed "
          f"(expected={expected})")
 
# ── 7D: Non-uniform superposition with rotation gate Ry ───────────────────
import math
theta = math.pi / 3                # 60-degree rotation
qc4 = QuantumCircuit(1, 1)
qc4.ry(theta, 0)                   # Ry(θ): P(|0⟩)=cos²(θ/2), P(|1⟩)=sin²(θ/2)
qc4.measure(0, 0)
 
counts4 = sim.run(qc4, shots=4096).result().get_counts()
p0 = counts4.get('0', 0) / 4096
p1 = counts4.get('1', 0) / 4096
print(f"\n=== 7D: Non-Uniform Superposition Ry(π/3) ===")
print(f"  P(|0⟩) measured ≈ {p0:.3f}  (theory: {math.cos(theta/2)**2:.3f})")
print(f"  P(|1⟩) measured ≈ {p1:.3f}  (theory: {math.sin(theta/2)**2:.3f})")