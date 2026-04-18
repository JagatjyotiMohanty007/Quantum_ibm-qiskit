# ============================================================
#  Code 13: Single-Qubit Gates – H, X, Y, Z, S, T
#  File: 03_single_qubit_gates.py
#  Requirements: pip install qiskit qiskit-aer matplotlib
# ============================================================
 
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
 
# ── 3A: Hadamard Gate (H) ─────────────────────────────────────────────────
qc_h = QuantumCircuit(1, 1)
qc_h.h(0)                   # |0⟩ → (|0⟩+|1⟩)/√2 : superposition
qc_h.measure(0, 0)
 
# ── 3B: Pauli-X Gate (NOT / Bit Flip) ────────────────────────────────────
qc_x = QuantumCircuit(1, 1)
qc_x.x(0)                   # |0⟩ → |1⟩
qc_x.measure(0, 0)
 
# ── 3C: Pauli-Y Gate ─────────────────────────────────────────────────────
qc_y = QuantumCircuit(1, 1)
qc_y.y(0)                   # |0⟩ → i|1⟩
qc_y.measure(0, 0)
 
# ── 3D: Pauli-Z Gate (Phase Flip) ────────────────────────────────────────
qc_z = QuantumCircuit(1, 1)
qc_z.h(0)                   # First create superposition
qc_z.z(0)                   # |+⟩ → |−⟩ (phase flip)
qc_z.h(0)                   # Back to computational basis
qc_z.measure(0, 0)
 
# ── 3E: S Gate (Phase Gate, π/2) ─────────────────────────────────────────
qc_s = QuantumCircuit(1, 1)
qc_s.h(0)                   # Superposition
qc_s.s(0)                   # Apply π/2 phase shift
qc_s.h(0)
qc_s.measure(0, 0)
 
# ── 3F: T Gate (π/8 gate, π/4 phase) ────────────────────────────────────
qc_t = QuantumCircuit(1, 1)
qc_t.h(0)                   # Superposition
qc_t.t(0)                   # Apply π/4 phase shift
qc_t.t(0)                   # Two T gates = S gate
qc_t.h(0)
qc_t.measure(0, 0)
 
# ── 3G: Full demo circuit showing all gates on separate qubits ─────────────
qc_all = QuantumCircuit(6, 6)
qc_all.h(0)                  # qubit 0: H gate
qc_all.x(1)                  # qubit 1: X gate
qc_all.y(2)                  # qubit 2: Y gate
qc_all.h(3); qc_all.z(3)     # qubit 3: H then Z gate
qc_all.h(4); qc_all.s(4)     # qubit 4: H then S gate
qc_all.h(5); qc_all.t(5)     # qubit 5: H then T gate
qc_all.measure(range(6), range(6))
 
print("=== All Single-Qubit Gates Demo ===")
print(qc_all.draw(output='text'))
 
# Simulate
sim = AerSimulator()
results = {}
for name, circ in [('H', qc_h), ('X', qc_x), ('Y', qc_y),
                   ('Z', qc_z), ('S', qc_s), ('T', qc_t)]:
    counts = sim.run(circ, shots=1024).result().get_counts()
    results[name] = counts
    print(f"Gate {name}: {counts}")