# ============================================
# Hello Quantum World - IBM Qiskit
# Install : pip install qiskit qiskit-aer
# ============================================

# pip install qiskit qiskit-aer

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

# Create a 2-qubit Bell State circuit
qc = QuantumCircuit(2, 2)
qc.h(0)            # Hadamard gate on qubit 0
qc.cx(0, 1)         # CNOT gate
qc.measure([0, 1], [0, 1])

print("Hello Quantum World from IBM Qiskit!")
print("Circuit:")
print(qc.draw())

# Run on local Aer simulator
sim = AerSimulator()
result = sim.run(qc, shots=1024).result()
counts = result.get_counts()
print(f"Measurement Results: {counts}")
