from collections import deque, namedtuple,OrderedDict
import numpy as np

def buscar_id(L,a):
        b=0
        for i in L:   
            if(i==a):
                return b
            b+=1

Arista = namedtuple('Arista', 'inicio, final, costo')

class Grafo(object):
    def __init__(self, aristas):
        self.aristas = [self.generar_arista(*arista) for arista in aristas]

    def generar_arista(self, inicio, final, costo=1):
        return Arista(inicio, final, costo)

    @property
    def vertices(self):
        V=[]
        for letra in ("".join(OrderedDict.fromkeys(sum(([arista.inicio, arista.final] for arista in self.aristas), [])))):
            V.append(letra)
        return V

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

    @property
    def matriz(self):
        mat= []
        for i in range(len(self.vertices)):
            mat.append([0]*len(self.vertices))
        i=0
        a=0
        while(i<len(mat)):
            j=0
            while(j<len(mat) and a<len(self.aristas)):
                if(i==buscar_id(self.vertices,self.aristas[a][0]) and j==buscar_id(self.vertices,self.aristas[a][1])):
                    mat[i][j] = self.aristas[a][2]
                    mat[j][i] = self.aristas[a][2]
                    a+=1
                j+=1
            i+=1
        return mat

    @property
    def conexa(self):
        a=0
        mat= np.linalg.matrix_power(self.matriz, a)
        a+=1
        while(a<len(self.vertices)):
            mat+=np.linalg.matrix_power(self.matriz, a)
            a+=1
        p=0
        while(p<len(mat)):
            q=0
            while(q<len(mat)):
                if(mat[p][q]==0):
                    return False
                q+=1
            p+=1
                        
        return True
        

    def __str__(self):
        return "Vertices: "+ str(self.vertices) + "\nAristas: " + str(self.obtener_aristas)