# Eric Rodriguez Del Valle      20310419

"""Introducción IA - Mapa de la IA

    Búsqueda en Grafos

        Planificación: Búsqueda no informada
"""


def dfs(graph, start, goal):        #Le damos el grafo, el nodo inicio y el obj.
    visited = set()                 #Nodos visitados
    stack = [start]
    
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)           #Añadimos nodo a lista de visitados.
            if node == goal:
                return True             #Al encontrar el nodo obj.
            stack.extend(set(graph[node]) - visited)
            
    return False


