# ============================================
# Create Bits and Qubits using Qiskit
# ============================================

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

# Create a quantum circuit with 1 qubit and 1 classical bit
qc = QuantumCircuit(1, 1)

# Apply Hadamard gate (superposition)
qc.h(0)

# Measure qubit
qc.measure(0, 0)

# Simulate
simulator = AerSimulator()
job = simulator.run(qc, shots=1)
result = job.result()

print("Measurement:", result.get_counts())