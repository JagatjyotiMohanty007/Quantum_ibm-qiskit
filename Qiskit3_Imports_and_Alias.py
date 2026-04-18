# ============================================
# Imports and Aliases in Qiskit
# ============================================

import qiskit as qk
from qiskit import QuantumCircuit as QC
from qiskit_aer import AerSimulator as Simulator

# Create circuit using alias
qc = QC(1, 1)

qc.h(0)
qc.measure(0, 0)

sim = Simulator()
result = sim.run(qc, shots=10).result()

print("Counts:", result.get_counts())