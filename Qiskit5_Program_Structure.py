# ============================================
# Full Qiskit Program Structure
# ============================================

from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

def create_circuit():
    qc = QuantumCircuit(1, 1)
    qc.h(0)
    qc.measure(0, 0)
    return qc

def run_circuit(qc):
    simulator = AerSimulator()

    # Transpile for backend
    compiled = transpile(qc, simulator)

    job = simulator.run(compiled, shots=100)
    result = job.result()

    return result.get_counts()

if __name__ == "__main__":
    circuit = create_circuit()
    counts = run_circuit(circuit)

    print("Result:", counts)