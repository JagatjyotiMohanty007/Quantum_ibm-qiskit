# ============================================
# Circuit Flow: Create → Apply → Measure
# ============================================

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

qc = QuantumCircuit(1, 1)

# Superposition
qc.h(0)

# Measurement
qc.measure(0, 0)

sim = AerSimulator()
result = sim.run(qc, shots=100).result()

print("Counts:", result.get_counts())