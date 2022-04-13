
import qiskit


def quantum_entanglement(qubits: int = 2) -> qiskit.result.counts.Counts:
    
    classical_bits = qubits

    
    simulator = qiskit.Aer.get_backend("qasm_simulator")

    
    circuit = qiskit.QuantumCircuit(qubits, classical_bits)

    
    circuit.h(0)

    for i in range(1, qubits):
        
        circuit.cx(i - 1, i)

    
    circuit.measure(list(range(qubits)), list(range(classical_bits)))

    
    

    
    job = qiskit.execute(circuit, simulator, shots=1000)

    return job.result().get_counts(circuit)


if __name__ == "__main__":
    print(f"Total count for various states are: {quantum_entanglement(3)}")
