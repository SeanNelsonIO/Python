
import numpy as np
import qiskit as q


def dj_oracle(case: str, num_qubits: int) -> q.QuantumCircuit:
    
    
    
    oracle_qc = q.QuantumCircuit(num_qubits + 1)

    
    if case == "balanced":
        
        
        b = np.random.randint(1, 2**num_qubits)
        
        b_str = format(b, f"0{num_qubits}b")
        
        
        
        for index, bit in enumerate(b_str):
            if bit == "1":
                oracle_qc.x(index)
        
        
        for index in range(num_qubits):
            oracle_qc.cx(index, num_qubits)
        
        for index, bit in enumerate(b_str):
            if bit == "1":
                oracle_qc.x(index)

    
    if case == "constant":
        
        
        output = np.random.randint(2)
        if output == 1:
            oracle_qc.x(num_qubits)

    oracle_gate = oracle_qc.to_gate()
    oracle_gate.name = "Oracle"  
    return oracle_gate


def dj_algorithm(oracle: q.QuantumCircuit, num_qubits: int) -> q.QuantumCircuit:
    
    dj_circuit = q.QuantumCircuit(num_qubits + 1, num_qubits)
    
    dj_circuit.x(num_qubits)
    dj_circuit.h(num_qubits)
    
    for qubit in range(num_qubits):
        dj_circuit.h(qubit)
    
    dj_circuit.append(oracle, range(num_qubits + 1))
    
    for qubit in range(num_qubits):
        dj_circuit.h(qubit)

    for i in range(num_qubits):
        dj_circuit.measure(i, i)

    return dj_circuit


def deutsch_jozsa(case: str, num_qubits: int) -> q.result.counts.Counts:
    
    
    simulator = q.Aer.get_backend("qasm_simulator")

    oracle_gate = dj_oracle(case, num_qubits)
    dj_circuit = dj_algorithm(oracle_gate, num_qubits)

    
    job = q.execute(dj_circuit, simulator, shots=1000)

    
    return job.result().get_counts(dj_circuit)


if __name__ == "__main__":
    print(f"Deutsch Jozsa - Constant Oracle: {deutsch_jozsa('constant', 3)}")
    print(f"Deutsch Jozsa - Balanced Oracle: {deutsch_jozsa('balanced', 3)}")
