from qiskit import QuantumCircuit, transpile, assemble, Aer, execute
from qiskit.visualization import plot_histogram, plot_bloch_multivector
import matplotlib.pyplot as plt


def random_quantum_number(bits):
    # Create a quantum circuit with the specified number of qubits
    circuit = QuantumCircuit(bits, bits)

    # Apply Hadamard gate to create superposition of all possible states
    circuit.h(range(bits))

    # Measure the qubits to collapse the superposition and obtain a classical random number
    circuit.measure(range(bits), range(bits))

    # Use the qasm_simulator to simulate the quantum circuit
    simulator = Aer.get_backend('qasm_simulator')

    # Execute the circuit and obtain the result
    result = execute(circuit, simulator, shots=1).result()

    # Get the counts from the result
    counts = result.get_counts(circuit)

    # Convert the binary representation to decimal to get the random number
    random_number = int(list(counts.keys())[0], 2)

    return random_number, circuit


# Set the number of qubits for the random number generator
num_qubits = 4

# Generate a random quantum number and get the quantum circuit
random_number, quantum_circuit = random_quantum_number(num_qubits)

# Plot the histogram
counts = execute(quantum_circuit, Aer.get_backend(
    'qasm_simulator'), shots=1000).result().get_counts()
plot_histogram(counts)
plt.title('Probability Distribution')
plt.show()

# Plot the Bloch sphere visualization
statevector_simulator = Aer.get_backend('statevector_simulator')
statevector = execute(
    quantum_circuit, statevector_simulator).result().get_statevector()
plot_bloch_multivector(statevector)
plt.title('Bloch Sphere Visualization')
plt.show()

print(f"Random quantum number: {random_number}")
