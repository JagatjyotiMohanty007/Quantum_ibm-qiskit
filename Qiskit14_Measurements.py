# ============================================================
#  Code 14: Measuring Qubits to Classical Bits
#  File: 04_measurement.py
#  Requirements: pip install qiskit qiskit-aer
# ============================================================
 
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
 
sim = AerSimulator()
 
# ── 4A: Basic single-qubit measurement ───────────────────────────────────
qc1 = QuantumCircuit(1, 1)
qc1.h(0)                          # superposition
qc1.measure(0, 0)                  # measure qubit 0 → classical bit 0
print("=== 4A: Single Qubit Measurement ===")
print(qc1.draw(output='text'))
counts1 = sim.run(qc1, shots=1000).result().get_counts()
print("Counts:", counts1)
 
# ── 4B: measure_all() – convenient shortcut ───────────────────────────────
qc2 = QuantumCircuit(3)            # 3 qubits, no classical bits yet
qc2.h(0)
qc2.x(1)                          # flip qubit 1
qc2.measure_all()                  # adds 3 classical bits and measures all
print("\n=== 4B: measure_all() ===")
print(qc2.draw(output='text'))
counts2 = sim.run(qc2, shots=500).result().get_counts()
print("Counts:", counts2)
 
# ── 4C: Selective measurement (measure only some qubits) ─────────────────
qc3 = QuantumCircuit(3, 2)         # 3 qubits but only 2 classical bits
qc3.h(0)
qc3.x(1)
qc3.h(2)
# Only measure qubits 0 and 2; qubit 1 is intentionally unmeasured
qc3.measure(0, 0)
qc3.measure(2, 1)
print("\n=== 4C: Selective Measurement (qubits 0 & 2 only) ===")
print(qc3.draw(output='text'))
counts3 = sim.run(qc3, shots=500).result().get_counts()
print("Counts:", counts3)
 
# ── 4D: get_memory() – shot-by-shot outcomes ──────────────────────────────
qc4 = QuantumCircuit(2, 2)
qc4.h(0)
qc4.h(1)
qc4.measure([0, 1], [0, 1])
# memory=True returns individual outcomes for each shot
result4 = sim.run(qc4, shots=10, memory=True).result()
memory  = result4.get_memory()
print("\n=== 4D: Individual Shot Memory (10 shots) ===")
for i, shot in enumerate(memory):
    print(f"  Shot {i+1}: {shot}")