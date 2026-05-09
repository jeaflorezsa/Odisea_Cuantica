# 📂 Archivo: 3-4_puerta_toffoli-if_cuantico.py
# 📅 Día: 3/4
# 🔗 Índice Global: ../README.md
# 🔗 Bitácora Diaria: ../log_de_vuelo-Bitacora_diaria.md
# 🔗 Teoría Detallada: ../01_Fundamentos/Dia3_Toffoli.md

"""
PROYECTO: Puerta Toffoli (El "IF" Cuántico)
DESCRIPCIÓN: Este script demuestra la lógica condicional cuántica usando tres qubits.

RESUMEN TEÓRICO:
La puerta Toffoli (CCNOT) es una puerta de tres qubits que funciona como un "AND" lógico. 
Invierte el estado del tercer qubit (objetivo) SI Y SOLO SI los dos primeros 
qubits (controles) están en el estado |1>. Es fundamental para construir 
computación reversible y algoritmos de optimización.

OBJETIVO: 
Observar cómo la superposición en los controles genera múltiples ramas de 
decisión lógica ejecutadas en simultáneo.

paso a paso:
1. Creamos un circuito con 3 qubits y 3 bits clásicos.
2. Ponemos el qubit 0 en superposición (50% de probabilidad de ser 1).
3. Ponemos el qubit 1 en estado sólido 1 (activado).
4. Aplicamos la puerta Toffoli (CCX) usando q0 y q1 como controles de q2.
5. Medimos los tres qubits para colapsar el estado.
6. Dibujamos el circuito y ejecutamos la simulación.
"""

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

# 1. Creamos un circuito con 3 qubits y 3 bits clásicos
# q0 y q1 serán nuestros "controles", q2 será el "objetivo"
qc = QuantumCircuit(3, 3)

# 2. Preparación de estados
# q0 es una "moneda en el aire" (Superposición)
qc.h(0) 
# q1 está "encendido" (Estado 1)
qc.x(1) 

# 3. Aplicación de la Puerta Toffoli (CCNOT)
# Sintaxis: ccx(control1, control2, objetivo)
qc.ccx(0, 1, 2)

# 4. Medición
qc.measure([0, 1, 2], [0, 1, 2])

# 5. Dibujo del circuito
print("--- Estructura del Circuito Toffoli ---")
print(qc.draw(output='text'))

# 6. Ejecución en simulador (Qiskit 1.0+: usar backend.run() en lugar de execute())
simulador = AerSimulator()
job = simulador.run(qc, shots=1000)
resultado = job.result()
counts = resultado.get_counts()

print("\n--- Resultados de la simulación ---")
print(f"Combinaciones detectadas (q2q1q0): {counts}")

"""
ANÁLISIS DE RESULTADOS:
Deberías ver aproximadamente un 50% de resultados '010' (q0 fue 0, no se activó el IF)
y un 50% de resultados '111' (q0 fue 1, se cumplió el IF y q2 cambió a 1).
"""






# 3. Aplicamos la Puerta Toffoli (CCNOT)
# Solo si q0 Y q1 son 1, entonces q2 cambiará de 0 a 1
qc.ccx(0, 1, 2)

# 4. Medimos los resultados
qc.measure([0, 1, 2], [0, 1, 2])

# 5. Dibujamos el circuito (como pediste)
print("--- Diagrama del Circuito Toffoli ---")
print(qc.draw(output='text'))

# 6. Ejecutamos para ver el resultado (reutilizando el mismo circuito; ya ejecutado arriba)
# Si se desea una segunda ejecución: resultado2 = simulador.run(qc, shots=1000).result()
counts = counts  # ya obtenido en el bloque anterior

print("\nResultado de la ejecución:")
print(counts)