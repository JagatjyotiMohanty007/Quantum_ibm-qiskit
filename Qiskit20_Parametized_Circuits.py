# ============================================================
#  Code 20: Parameterized Quantum Circuits
#  File: 10_parameterized_circuits.py
#  Requirements: pip install qiskit qiskit-aer matplotlib
# ============================================================
 
from qiskit import QuantumCircuit
from qiskit.circuit import Parameter, ParameterVector
from qiskit_aer import AerSimulator
import numpy as np
import matplotlib.pyplot as plt
 
sim = AerSimulator()
 
# ── 10A: Single Parameter ────────────────────────────────────────────────
theta = Parameter('θ')             # Create a symbolic parameter named θ
 
qc = QuantumCircuit(1, 1)
qc.h(0)
qc.ry(theta, 0)                    # Ry gate with angle θ (not yet assigned)
qc.measure(0, 0)
 
print("=== 10A: Parameterized Circuit (before binding) ===")
print(qc.draw(output='text'))
print(f"  Unbound parameters: {qc.parameters}")
 
# Bind θ = π/4 and run
qc_bound = qc.assign_parameters({theta: np.pi / 4})
counts = sim.run(qc_bound, shots=1024).result().get_counts()
print(f"\n  θ = π/4  →  {counts}")
 
# ── 10B: Sweep parameter over many angles ────────────────────────────────
print("\n=== 10B: Parameter Sweep — P(|1⟩) vs Ry angle ===")
angles = np.linspace(0, 2 * np.pi, 20)
p1_values = []
for angle in angles:
    bound = qc.assign_parameters({theta: float(angle)})
    counts = sim.run(bound, shots=2048).result().get_counts()
    p1 = counts.get('1', 0) / 2048
    p1_values.append(p1)
    print(f"  θ = {angle:.2f} rad  → P(|1⟩) = {p1:.3f}")
 
# ── 10C: ParameterVector for multi-qubit variational circuit ──────────────
print("\n=== 10C: ParameterVector – 2-qubit Ansatz ===")
params = ParameterVector('φ', 4)   # 4 parameters: φ[0], φ[1], φ[2], φ[3]
 
qc2 = QuantumCircuit(2, 2)
qc2.ry(params[0], 0)               # Layer 1: rotation on qubit 0
qc2.ry(params[1], 1)               # Layer 1: rotation on qubit 1
qc2.cx(0, 1)                       # Entangling layer
qc2.ry(params[2], 0)               # Layer 2: rotation on qubit 0
qc2.ry(params[3], 1)               # Layer 2: rotation on qubit 1
qc2.measure([0, 1], [0, 1])
 
print(qc2.draw(output='text'))
 
# Bind all parameters with a specific set of angles
angle_values = [np.pi/3, np.pi/6, np.pi/4, np.pi/2]
qc2_bound = qc2.assign_parameters(dict(zip(params, angle_values)))
counts2 = sim.run(qc2_bound, shots=1024).result().get_counts()
print(f"\n  Bound with {[round(a,3) for a in angle_values]}")
print(f"  Results: {counts2}")