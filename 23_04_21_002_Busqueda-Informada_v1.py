# Eric Rodriguez Del Valle      20310419

"""Introducción IA - Mapa de la IA

    Búsqueda en Grafos

        Planificación: Búsqueda informadad. Heurística.
        Estimamos costos, analizamos una solución en base a las estimaciones.
        Si no llegamos al obj, nos vamos a los vecinos del nodo actual.

"""


from queue import PriorityQueue

def astar(graph, start, goal, heuristic):       #Heuristic toma nodo actual y obj para regresar un costo estimado.
    frontier = PriorityQueue()          #Nodos a explorar
    frontier.put(start, 0)
    came_from = {}              #Nodos visitados y predecesor
    cost_so_far = {}        #Registro del costo acumulado de llegar a cada nodo.
    came_from[start] = None
    cost_so_far[start] = 0
    
    while not frontier.empty():
        current = frontier.get()            #Nodo más barato estimado
        if current == goal:         #If llegamos al obj
            break
        
        for next in graph[current]:         #Si no, buscamos en los vecinos del nodo actual.
            new_cost = cost_so_far[current] + graph[current][next]
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost        #Actualizamos el menor costo
                priority = new_cost + heuristic(goal, next)
                frontier.put(next, priority)
                came_from[next] = current       #Actualizamos nodo actual
    
    return came_from, cost_so_far
