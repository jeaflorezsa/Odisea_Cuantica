# 01_bell_state.py
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

# Creamos un circuito con 2 qubits y 2 bits clásicos para la medida
qc = QuantumCircuit(2, 2)

# Paso 1: Ponemos el qubit 0 en una mezcla 50/50 (Superposición)
qc.h(0) 

# Paso 2: Entrelazamos el qubit 0 con el qubit 1
# Si el 0 es 1, el 1 cambia. Como el 0 es "todo a la vez", 
# el 1 se vuelve "todo a la vez" PERO conectado al 0.
qc.cx(0, 1)

# Paso 3: Medimos
qc.measure([0, 1], [0, 1])

# Ejecución
simulador = AerSimulator()
job = simulador.run(qc, shots=1000)
stats = job.result().get_counts()

print(f"Resultado del entrelazamiento: {stats}")