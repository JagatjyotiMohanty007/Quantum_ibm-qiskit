# ============================================
# Quantum Data Types in Qiskit
# ============================================

from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit

# Create registers
qreg = QuantumRegister(2, name="q")
creg = ClassicalRegister(2, name="c")

# Create circuit
qc = QuantumCircuit(qreg, creg)

# Apply gates
qc.h(qreg[0])
qc.cx(qreg[0], qreg[1])

# Measure
qc.measure(qreg, creg)

print(qc)