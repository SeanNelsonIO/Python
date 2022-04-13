

import qiskit as q


def single_qubit_measure(qubits: int, classical_bits: int) -> q.result.counts.Counts:
    
    
    simulator = q.Aer.get_backend("qasm_simulator")

    
    circuit = q.QuantumCircuit(qubits, classical_bits)

    
    circuit.x(0)
    circuit.x(1)

    
    circuit.measure([0, 1], [0, 1])

    
    job = q.execute(circuit, simulator, shots=1000)

    
    return job.result().get_counts(circuit)


if __name__ == "__main__":
    counts = single_qubit_measure(2, 2)
    print(f"Total count for various states are: {counts}")
