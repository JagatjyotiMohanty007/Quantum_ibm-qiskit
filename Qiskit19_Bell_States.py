# ============================================================
#  Code 19: Entanglement – All Four Bell States
#  File: 09_bell_states.py
#  Requirements: pip install qiskit qiskit-aer matplotlib
# ============================================================
 
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
 
sim = AerSimulator()
 
def make_bell_state(phi_plus=True, psi=False, minus=False):
    """
    Create a Bell state circuit.
    Bell states:
      Phi+ : H on q0, then CX(q0,q1)
      Phi- : H on q0, Z on q0, then CX(q0,q1)
      Psi+ : H on q0, X on q1, then CX(q0,q1)
      Psi- : H on q0, X on q1, Z on q0, then CX(q0,q1)
    """
    qc = QuantumCircuit(2, 2)
    if psi:   qc.x(1)             # flip qubit 1 first for Psi states
    qc.h(0)                       # create superposition on qubit 0
    if minus: qc.z(0)             # phase flip for minus variants
    qc.cx(0, 1)                   # entangle: CNOT with q0 as control
    return qc
 
# ── All four Bell States ──────────────────────────────────────────────────
bell_circuits = {
    '|Φ+⟩ = (|00⟩+|11⟩)/√2': make_bell_state(),
    '|Φ-⟩ = (|00⟩-|11⟩)/√2': make_bell_state(minus=True),
    '|Ψ+⟩ = (|01⟩+|10⟩)/√2': make_bell_state(psi=True),
    '|Ψ-⟩ = (|01⟩-|10⟩)/√2': make_bell_state(psi=True, minus=True),
}
 
print("=== Bell State Circuits & Measurement Results ===\n")
for name, qc in bell_circuits.items():
    qc_m = qc.copy()
    qc_m.measure([0, 1], [0, 1])
    counts = sim.run(qc_m, shots=2048).result().get_counts()
    print(f"  {name}")
    print(f"    Counts: {counts}")
    print()
 
# ── Verify entanglement using statevectors ────────────────────────────────
sim_sv = AerSimulator(method='statevector')
print("=== Statevector Verification of |Φ+⟩ ===")
qc_sv = make_bell_state()
qc_sv.save_statevector()
sv = sim_sv.run(qc_sv).result().get_statevector()
basis = ['|00⟩', '|01⟩', '|10⟩', '|11⟩']
for label, amp in zip(basis, sv):
    print(f"  {label}: {amp:.4f}  (prob={abs(amp)**2:.4f})")
 
# ── Demonstrate non-classical correlations ────────────────────────────────
print("\n=== Entanglement Demonstration ===")
print("In |Φ+⟩: whenever qubit 0 = 0, qubit 1 = 0 (always correlated)")
qc_demo = make_bell_state()
qc_demo.measure([0, 1], [0, 1])
counts = sim.run(qc_demo, shots=1024).result().get_counts()
same = counts.get('00', 0) + counts.get('11', 0)
diff = counts.get('01', 0) + counts.get('10', 0)
print(f"  Correlated outcomes (00 or 11): {same}/1024 = {same/10.24:.1f}%")
print(f"  Anti-correlated    (01 or 10): {diff}/1024 = {diff/10.24:.1f}%")