from collections import deque, namedtuple,OrderedDict
import numpy as np

def buscar_id(L,a):
        b=0
        for i in L:   
            if(i==a):
                return b
            b+=1

Arista = namedtuple('Arista', 'inicio, final, peso')

class Grafo(object):
    def __init__(self, aristas):
        self.aristas = [self.generar_arista(*arista) for arista in aristas]

    def generar_arista(self, inicio, final, peso=1):
        return Arista(inicio, final, peso)

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
            tupla = (arista.inicio, arista.final, arista.peso)
            respuesta.append(tupla)
        return respuesta

    def peso_arista(self, inicio, final):
        for arista in self.aristas:
            if arista.inicio == inicio and arista.final == final:
                return arista.peso
        return 0

    @property
    def vecinos(self):
        vecinos = {vertice: set() for vertice in self.vertices}
        for arista in self.aristas:
            vecinos[arista.inicio].add((arista.final, arista.peso))
        return vecinos

    def dijkstra(self, inicio, final):
        inf = float('inf')
        distancias = {vertice: inf for vertice in self.vertices}
        vertices_anteriores = {
            vertice: None for vertice in self.vertices
        }
        peso_total = 0
        distancias[inicio] = 0
        vertices = self.vertices.copy()
        while vertices:
            vertice_actual = min(vertices, key=lambda vertice: distancias[vertice])
            if distancias[vertice_actual] == inf:
                break
            for vecino, peso in self.vecinos[vertice_actual]:
                otra_ruta = distancias[vertice_actual] + peso
                if otra_ruta < distancias[vecino]:
                    distancias[vecino] = otra_ruta
                    vertices_anteriores[vecino] = vertice_actual
            vertices.remove(vertice_actual)
        ruta, vertice_actual = deque(), final
        while vertices_anteriores[vertice_actual] is not None:
            if len(ruta)>0:
                peso_total = peso_total + self.peso_arista(str(vertice_actual), str(ruta[0]))
            ruta.appendleft(vertice_actual)
            vertice_actual = vertices_anteriores[vertice_actual]
        if ruta:
            peso_total = peso_total + self.peso_arista(str(vertice_actual), str(ruta[0]))
            ruta.appendleft(vertice_actual)
        return (list(deque(ruta)), peso_total)

    @property
    def matriz(self):
        mat= []
        for i in range(len(self.vertices)):
            mat.append([0]*len(self.vertices))
        a=0
        while(a<len(self.aristas)):
            i=buscar_id(self.vertices,self.aristas[a][0])
            j=buscar_id(self.vertices,self.aristas[a][1])
            mat[i][j] = self.aristas[a][2]
            mat[j][i] = self.aristas[a][2]
            a+=1
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
    
    @property
    def grados(self):
        L=[]
        for i in range(len(self.vertices)):
            L.append(0)
        a=0
        while(a<len(self.aristas)):
            i=buscar_id(self.vertices,self.aristas[a][0])
            j=buscar_id(self.vertices,self.aristas[a][1])
            L[i]+=1
            L[j]+=1
            a+=1
        return L

    @property
    def hamilton(self):
        if(self.conexa and len(self.vertices)>=3):
            p=len(self.vertices)/2
            for i in self.grados:
                if(i < p):
                    return False
            return True  
        return False




    def __str__(self):
        return "Vertices: "+ str(self.vertices) + "\nAristas: " + str(self.obtener_aristas)