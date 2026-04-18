# ============================================
# Comments and Docstrings in Python/Qiskit
# ============================================

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

def measure_qubit():
    """
    Demonstrates measurement of a single qubit.

    Steps:
    1. Create qubit
    2. Apply Hadamard
    3. Measure result
    """

    qc = QuantumCircuit(1, 1)

    qc.h(0)  # Put qubit in superposition
    qc.measure(0, 0)

    simulator = AerSimulator()
    result = simulator.run(qc).result()

    return result.get_counts()

if __name__ == "__main__":
    print(measure_qubit())