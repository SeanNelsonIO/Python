
import qiskit as q


def half_adder(bit0: int, bit1: int) -> q.result.counts.Counts:
    
    
    simulator = q.Aer.get_backend("qasm_simulator")

    qc_ha = q.QuantumCircuit(4, 2)
    
    if bit0 == 1:
        qc_ha.x(0)
    if bit1 == 1:
        qc_ha.x(1)
    qc_ha.barrier()

    
    qc_ha.cx(0, 2)
    qc_ha.cx(1, 2)

    
    qc_ha.ccx(0, 1, 3)
    qc_ha.barrier()

    
    qc_ha.measure(2, 0)  
    qc_ha.measure(3, 1)  

    
    job = q.execute(qc_ha, simulator, shots=1000)

    
    return job.result().get_counts(qc_ha)


if __name__ == "__main__":
    counts = half_adder(1, 1)
    print(f"Half Adder Output Qubit Counts: {counts}")
