# ============================================================
#  Code 1: Hello Quantum World – First Qiskit Circuit
#  File: 01_hello_quantum.py
#  Requirements: pip install qiskit qiskit-aer
# ============================================================
 
from qiskit import QuantumCircuit          # Core circuit builder
from qiskit_aer import AerSimulator        # Local quantum simulator
 
# Step 1: Create a quantum circuit with 1 qubit and 1 classical bit
qc = QuantumCircuit(2, 1)
 
# Step 2: Apply Hadamard gate to qubit 0
#   H gate transforms |0⟩ → (|0⟩ + |1⟩)/√2  (equal superposition)
qc.h(0)
qc.h(1)
# Step 3: Measure qubit 0 → store result in classical bit 0
qc.measure(0, 0)
qc.measure(1, 0)
 
# Step 4: Print the circuit diagram in ASCII art
print("=== Quantum Circuit ===")
print(qc.draw(output='text'))
 
# Step 5: Run the circuit on Aer local simulator
simulator = AerSimulator()
job = simulator.run(qc, shots=1024)       # 1024 repetitions
result = job.result()
 
# Step 6: Extract and display the measurement counts
counts = result.get_counts()
print("\n=== Measurement Results (1024 shots) ===")
print(counts)
print(counts.get('00', 0))
print(counts.get('01', 0))
print(counts.get('10', 0)) 

print(f"  '00' count: {counts.get('00', 0)}")
print(f"  '01' count: {counts.get('01', 0)}")
print(f"  '10' count: {counts.get('10', 0)}")
print(f"  '11' count: {counts.get('11', 0)}")
