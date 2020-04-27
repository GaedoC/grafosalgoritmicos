from collections import deque, namedtuple

Arista = namedtuple('Arista', 'inicio, final, costo')

class Grafo(object):
    def __init__(self, aristas):
        self.aristas = [self.generar_arista(*arista) for arista in aristas]

    def generar_arista(self, inicio, final, costo=1):
        return Arista(inicio, final, costo)

    @property
    def vertices(self):
        return set(sum(([arista.inicio, arista.final] for arista in self.aristas), []))

    @property
    def obtener_aristas(self):
        respuesta = []
        for arista in self.aristas:
            tupla = (arista.inicio, arista.final, arista.costo)
            respuesta.append(tupla)
        return respuesta

    @property
    def vecinos(self):
        vecinos = {vertice: set() for vertice in self.vertices}
        for arista in self.aristas:
            vecinos[arista.inicio].add((arista.final, arista.costo))
        return vecinos

    def dijkstra(self, inicio, final):
        inf = float('inf')
        distancias = {vertice: inf for vertice in self.vertices}
        vertices_anteriores = {
            vertice: None for vertice in self.vertices
        }
        distancias[inicio] = 0
        vertices = self.vertices.copy()
        while vertices:
            vertice_actual = min(vertices, key=lambda vertice: distancias[vertice])
            if distancias[vertice_actual] == inf:
                break
            for vecino, costo in self.vecinos[vertice_actual]:
                otra_ruta = distancias[vertice_actual] + costo
                if otra_ruta < distancias[vecino]:
                    distancias[vecino] = otra_ruta
                    vertices_anteriores[vecino] = vertice_actual
            vertices.remove(vertice_actual)
        ruta, vertice_actual = deque(), final
        while vertices_anteriores[vertice_actual] is not None:
            ruta.appendleft(vertice_actual)
            vertice_actual = vertices_anteriores[vertice_actual]
        if ruta:
            ruta.appendleft(vertice_actual)
        return list(deque(ruta))

    def __str__(self):
        return "Vertices: "+ str(self.vertices) + "\nAristas: " + str(self.obtener_aristas)