# Eric Rodriguez Del Valle      20310419

"""Introducción IA - Mapa de la IA

    Búsqueda en Grafos

        Planificación: Algorítmos Genéticos
        Creamos soluciones, tomamos las mejores como "padres".
        En base a esa creamos más soluciones hasta encontrar una satisfactoria.

"""

import random

# Definir los parámetros del problema
pesos = [2, 3, 4, 5, 9]             
valores = [3, 4, 5, 8, 10]          
capacidad_mochila = 20              #Maximizaremos la cantidad de objs en la mochila.
tamano_poblacion = 10
probabilidad_mutacion = 0.1
num_generaciones = 50

# Creamos las primeras soluciones para buscar a los padres
def crear_poblacion():
    poblacion = []
    for _ in range(tamano_poblacion):
        solucion = [random.randint(0, 1) for _ in range(len(pesos))]
        poblacion.append(solucion)
    return poblacion

# Analizamos en busca de las mejores para que sean los padres
def evaluar_solucion(solucion):
    peso_total = 0
    valor_total = 0
    for i in range(len(solucion)):
        if solucion[i] == 1:
            peso_total += pesos[i]
            valor_total += valores[i]
    if peso_total > capacidad_mochila:      #Si nos pasamos, descartamos y repetimos.
        valor_total = 0
    return valor_total

# Seleccionamos a los padres
def seleccionar_padres(poblacion):
    padres = []
    for _ in range(2):
        padres.append(max(poblacion, key=evaluar_solucion))     #Seleccionamos la mejor solución
    return padres

# Generamos más soluciones en base a los padres. Hijos.
def generar_hijos(padres):
    punto_cruce = random.randint(1, len(pesos) - 1)
    hijo1 = padres[0][:punto_cruce] + padres[1][punto_cruce:]
    hijo2 = padres[1][:punto_cruce] + padres[0][punto_cruce:]
    return hijo1, hijo2

# Mutamos la solución hija.
def mutar(solucion):
    for i in range(len(solucion)):
        if random.random() < probabilidad_mutacion:
            solucion[i] = 1 - solucion[i]
    return solucion

# Ejecutar el algoritmo genético
poblacion = crear_poblacion()
for _ in range(num_generaciones):
    padres = seleccionar_padres(poblacion)
    hijos = generar_hijos(padres)
    nueva_poblacion = []
    for solucion in hijos:
        if random.random() < probabilidad_mutacion:
            solucion = mutar(solucion)
        nueva_poblacion.append(solucion)
    poblacion = poblacion + nueva_poblacion
    poblacion = sorted(poblacion, key=evaluar_solucion, reverse=True)[:tamano_poblacion]

# Mostramos la mejor solución encontrada
mejor_solucion = max(poblacion, key=evaluar_solucion)
print("Mejor solución encontrada: ", mejor_solucion)
print("Valor total: ", evaluar_solucion(mejor_solucion))
