# ============================================
# Qubit Lifecycle in Qiskit
# ============================================

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

qc = QuantumCircuit(2, 2)

# Creation is implicit in circuit definition

# Superposition
qc.h(0)

# Entanglement
qc.cx(0, 1)

# Measurement
qc.measure([0, 1], [0, 1])

sim = AerSimulator()
result = sim.run(qc, shots=1000).result()

print("Entangled Results:", result.get_counts())