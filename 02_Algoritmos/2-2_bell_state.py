# 📂 Archivo: 2-2_bell_state.py
# 📅 Día: 2/2
# 🔗 Índice Global: ../README.md
# 🔗 Bitácora Diaria: ../log_de_vuelo-Bitacora_diaria.md
# 🔗 Teoría Detallada: ../01_Fundamentos/Dia2_Bell.md

"""
PROYECTO: Mi primer Estado de Bell
DESCRIPCIÓN: Este script crea dos qubits entrelazados.

RESUMEN TEÓRICO:
El entrelazamiento cuántico permite que dos qubits estén correlacionados 
de tal forma que el estado de uno dependa instantáneamente del otro. 
Usamos una puerta H (Hadamard) y una CNOT.

OBJETIVO: 
Demostrar que en el resultado final NO existen los estados '01' o '10'.

paso a paso:
1. Creamos un circuito con 2 qubits y 2 bits clásicos para la medida
2. Ponemos el qubit 0 en una mezcla 50/50 (Superposición)
3. Entrelazamos el qubit 0 con el qubit 1
4. Medimos
5. Ejecutamos
6. Mostramos el resultado

"""

# 2-2_bell_state.py
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

# %% [markdown]
# ### Visualización (Para Obsidian/Notebooks)
# Si corres esto en Cursor como una celda, puedes exportar el histograma aquí.
# NOTA PARA EL LOG: El resultado {'00': 493, '11': 507} confirma la correlación.
# Siguiente paso: Probar esto en un procesador real (Willow/Sycamore).