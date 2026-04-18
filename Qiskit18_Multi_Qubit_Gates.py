# ============================================================
#  Code 18: Multi-Qubit Gates – CX, CCX (Toffoli), SWAP, CZ
#  File: 08_multi_qubit_gates.py
#  Requirements: pip install qiskit qiskit-aer
# ============================================================
 
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
 
sim = AerSimulator()
 
# ── 8A: CNOT / CX Gate truth table ───────────────────────────────────────
print("=== 8A: CNOT Gate Truth Table ===")
print("Control | Target | Output")
print("--------+--------+-------")
for ctrl, tgt in [(0,0),(0,1),(1,0),(1,1)]:
    qc = QuantumCircuit(2, 2)
    if ctrl: qc.x(0)              # set control qubit to |1⟩ if needed
    if tgt:  qc.x(1)              # set target qubit  to |1⟩ if needed
    qc.cx(0, 1)                   # CNOT: flip qubit 1 if qubit 0 is |1⟩
    qc.measure([0, 1], [0, 1])
    counts = sim.run(qc, shots=1).result().get_counts()
    result_str = list(counts.keys())[0]
    print(f"  {ctrl}       |   {tgt}    |  {result_str}  (c={result_str[1]}, t={result_str[0]})")
 
# ── 8B: Toffoli (CCX) Gate – quantum AND ──────────────────────────────────
print("\n=== 8B: Toffoli (CCX) Gate ===")
print("Control0 | Control1 | Target | Output")
for c0, c1, tgt in [(0,0,0),(0,1,0),(1,0,0),(1,1,0)]:
    qc = QuantumCircuit(3, 3)
    if c0:  qc.x(0)
    if c1:  qc.x(1)
    if tgt: qc.x(2)
    qc.ccx(0, 1, 2)               # Toffoli: flip qubit 2 only if qubits 0 AND 1 are |1⟩
    qc.measure([0, 1, 2], [0, 1, 2])
    counts = sim.run(qc, shots=1).result().get_counts()
    r = list(counts.keys())[0]    # e.g. '011' → qubit 2 is r[0]
    print(f"  {c0}        |    {c1}     |   {tgt}    |  {r}")
 
# ── 8C: SWAP Gate ─────────────────────────────────────────────────────────
print("\n=== 8C: SWAP Gate ===")
qc_swap = QuantumCircuit(2, 2)
qc_swap.x(0)                      # set qubit 0 = |1⟩, qubit 1 = |0⟩
qc_swap.swap(0, 1)                 # SWAP: exchange qubit 0 and qubit 1
qc_swap.measure([0, 1], [0, 1])
counts_swap = sim.run(qc_swap, shots=100).result().get_counts()
print(f"  Before SWAP: q0=|1⟩, q1=|0⟩")
print(f"  After SWAP:  counts={counts_swap}")   # Expect '01': q1 is now |1⟩
 
# ── 8D: CZ Gate – phase-sensitive entanglement ────────────────────────────
print("\n=== 8D: CZ Gate (Controlled-Z) ===")
qc_cz = QuantumCircuit(2, 2)
qc_cz.h(0)                        # superposition on qubit 0
qc_cz.h(1)                        # superposition on qubit 1
qc_cz.cz(0, 1)                    # CZ: flips phase of |11⟩ component
qc_cz.h(0)                        # map back to computational basis
qc_cz.h(1)
qc_cz.measure([0, 1], [0, 1])
counts_cz = sim.run(qc_cz, shots=1024).result().get_counts()
print(f"  H-CZ-H result (should collapse to |11⟩): {counts_cz}")