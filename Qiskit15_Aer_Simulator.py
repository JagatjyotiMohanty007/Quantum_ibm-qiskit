# ============================================================
#  Code 15: Simulating with AerSimulator – Methods & Statevector
#  File: 05_aer_simulator.py
#  Requirements: pip install qiskit qiskit-aer
# ============================================================
 
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import numpy as np
 
# ── 5A: Default simulation (shot-based) ──────────────────────────────────
sim = AerSimulator()
 
qc = QuantumCircuit(2, 2)
qc.h(0)                           # superposition
qc.cx(0, 1)                       # CNOT: entangle qubits 0 and 1
qc.measure([0, 1], [0, 1])
 
print("=== 5A: Default Shot-Based Simulation ===")
print(qc.draw(output='text'))
 
for shots in [100, 500, 1000, 5000]:
    counts = sim.run(qc, shots=shots).result().get_counts()
    total = sum(counts.values())
    p00 = counts.get('00', 0) / total * 100
    p11 = counts.get('11', 0) / total * 100
    print(f"shots={shots:5d}  |00⟩={p00:.1f}%  |11⟩={p11:.1f}%")
 
# ── 5B: Statevector simulation (exact amplitudes) ─────────────────────────
sim_sv = AerSimulator(method='statevector')
 
qc_sv = QuantumCircuit(2)          # No classical bits needed for statevector
qc_sv.h(0)
qc_sv.cx(0, 1)
qc_sv.save_statevector()           # Save statevector to result
 
result_sv = sim_sv.run(qc_sv).result()
statevector = result_sv.get_statevector()
 
print("\n=== 5B: Exact Statevector (Bell State |Φ+⟩) ===")
print("State vector amplitudes:")
basis = ['|00⟩', '|01⟩', '|10⟩', '|11⟩']
for label, amp in zip(basis, statevector):
    prob = abs(amp)**2
    print(f"  {label}: amplitude={amp:.4f}  probability={prob:.4f}")
 
# ── 5C: Accessing result metadata ─────────────────────────────────────────
result = sim.run(qc, shots=1024).result()
print("\n=== 5C: Result Metadata ===")
print(f"  Backend name : {result.backend_name}")
print(f"  Job ID       : {result.job_id}")
print(f"  Success      : {result.success}")
print(f"  Time taken   : {result.time_taken:.4f} seconds")
