# ============================================================
#  Code 12: Creating Quantum & Classical Registers
#  File: 02_registers.py
#  Requirements: pip install qiskit qiskit-aer
# ============================================================
 
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator
 
# ── Example A: Named registers (2 qubits, 2 classical bits) ──────────────
qr = QuantumRegister(2, name='q')          # 2 qubits, named 'q'
cr = ClassicalRegister(2, name='c')        # 2 classical bits, named 'c'
qc = QuantumCircuit(qr, cr)               # combine into one circuit
 
# Apply gates using register indices
qc.h(qr[0])                               # Hadamard on qubit q[0]
qc.x(qr[1])                               # Pauli-X (NOT gate) on qubit q[1]
 
# Measure both qubits
qc.measure(qr[0], cr[0])                  # q[0] → c[0]
qc.measure(qr[1], cr[1])                  # q[1] → c[1]
 
print("=== Circuit with Named Registers ===")
print(qc.draw(output='text'))
 
# ── Example B: Multiple named register groups ─────────────────────────────
# Useful for labelling qubit roles (e.g., data vs ancilla)
data_qr  = QuantumRegister(2, 'data')     # data qubits
anc_qr   = QuantumRegister(1, 'ancilla') # ancilla (helper) qubit
out_cr   = ClassicalRegister(2, 'out')   # classical output bits
 
qc2 = QuantumCircuit(data_qr, anc_qr, out_cr)
qc2.h(data_qr[0])
qc2.cx(data_qr[0], data_qr[1])           # CNOT: entangle data qubits
qc2.measure(data_qr[0], out_cr[0])
qc2.measure(data_qr[1], out_cr[1])
 
print("\n=== Circuit with Multiple Register Groups ===")
print(qc2.draw(output='text'))
 
# ── Simulate Example A ────────────────────────────────────────────────────
sim = AerSimulator()
result = sim.run(qc, shots=512).result()
print("\n=== Example A Results (512 shots) ===")
print(result.get_counts())