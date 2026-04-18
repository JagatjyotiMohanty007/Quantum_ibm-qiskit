# ============================================================
#  Code 16: Visualizing Circuits & Results
#  File: 06_visualization.py
#  Requirements: pip install qiskit qiskit-aer matplotlib pylatexenc
# ============================================================
 
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram, plot_bloch_multivector
import matplotlib.pyplot as plt
 
# Build a sample Bell State circuit
qc = QuantumCircuit(2, 2)
qc.h(0)
qc.cx(0, 1)
qc.measure([0, 1], [0, 1])
 
# ── 6A: Text diagram (always works, no dependencies) ─────────────────────
print("=== 6A: Text Diagram ===")
print(qc.draw(output='text'))
 
# ── 6B: Matplotlib diagram – save to file ────────────────────────────────
fig = qc.draw(output='mpl', style={'name': 'bw'})  # black & white style
fig.savefig('circuit_diagram.png', dpi=150, bbox_inches='tight')
print("\n=== 6B: Circuit saved to 'circuit_diagram.png' ===")
 
# ── 6C: Matplotlib with color style ──────────────────────────────────────
fig2 = qc.draw(output='mpl', style={'name': 'clifford'})   # colorful
fig2.savefig('circuit_color.png', dpi=150, bbox_inches='tight')
print("=== 6C: Color circuit saved to 'circuit_color.png' ===")
 
# ── 6D: Histogram of measurement counts ──────────────────────────────────
sim = AerSimulator()
counts = sim.run(qc, shots=2048).result().get_counts()
fig3 = plot_histogram(counts, title="Bell State Measurement Distribution")
fig3.savefig('histogram.png', dpi=150, bbox_inches='tight')
print("=== 6D: Histogram saved to 'histogram.png' ===")
print("Counts:", counts)
 
# ── 6E: Bloch sphere visualization (statevector) ─────────────────────────
# For single qubit: create |+⟩ state and visualize on Bloch sphere
qc_sv = QuantumCircuit(1)
qc_sv.h(0)                              # |0⟩ → |+⟩
qc_sv.save_statevector()
 
sim_sv = AerSimulator(method='statevector')
sv = sim_sv.run(qc_sv).result().get_statevector()
 
fig4 = plot_bloch_multivector(sv)
fig4.savefig('bloch_sphere.png', dpi=150, bbox_inches='tight')
print("=== 6E: Bloch sphere saved to 'bloch_sphere.png' ===")
 
print("\nAll visualizations complete. Open .png files in VS Code to view.")