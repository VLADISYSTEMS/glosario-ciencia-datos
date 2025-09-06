# Ejemplo práctico: Ciencia de Datos con Python
# Autor: Vladisystems
# Descripción: mini análisis de ventas diarias
# Concepto: Ciencia de Datos combina estadística + programación + análisis para transformar datos en conocimiento

import statistics

# Datos: ventas diarias en una semana
ventas = [120, 150, 90, 200, 175, 130, 160]

# Cálculos estadísticos
promedio = statistics.mean(ventas)
desviacion = statistics.stdev(ventas)
maximo = max(ventas)
minimo = min(ventas)

# Resultados
print("Ventas:", ventas)
print("Promedio de ventas:", promedio)
print("Desviación estándar:", desviacion)
print("Mayor venta:", maximo)
print("Menor venta:", minimo)
