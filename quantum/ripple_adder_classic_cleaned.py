



from qiskit import Aer, QuantumCircuit, execute
from qiskit.providers import BaseBackend


def store_two_classics(val1: int, val2: int) -> tuple[QuantumCircuit, str, str]:
    
    x, y = bin(val1)[2:], bin(val2)[2:]  

    
    if len(x) > len(y):
        y = y.zfill(len(x))
    else:
        x = x.zfill(len(y))

    
    
    circuit = QuantumCircuit((len(x) * 3) + 1, len(x) + 1)

    
    
    for i in range(len(x)):
        if x[::-1][i] == "1":
            circuit.x(i)
    for j in range(len(y)):
        if y[::-1][j] == "1":
            circuit.x(len(x) + j)

    return circuit, x, y


def full_adder(
    circuit: QuantumCircuit,
    input1_loc: int,
    input2_loc: int,
    carry_in: int,
    carry_out: int,
):
    
    circuit.ccx(input1_loc, input2_loc, carry_out)
    circuit.cx(input1_loc, input2_loc)
    circuit.ccx(input2_loc, carry_in, carry_out)
    circuit.cx(input2_loc, carry_in)
    circuit.cx(input1_loc, input2_loc)








def ripple_adder(
    val1: int,
    val2: int,
    backend: BaseBackend = Aer.get_backend("qasm_simulator"),  
) -> int:
    

    if val1 < 0 or val2 < 0:
        raise ValueError("Both Integers must be positive!")

    
    circuit, x, y = store_two_classics(val1, val2)

    for i in range(len(x)):
        full_adder(circuit, i, len(x) + i, len(x) + len(y) + i, len(x) + len(y) + i + 1)
        circuit.barrier()  

    
    for i in range(len(x) + 1):
        circuit.measure([(len(x) * 2) + i], [i])

    res = execute(circuit, backend, shots=1).result()

    
    return int(list(res.get_counts())[0], 2)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
