from collections import deque, namedtuple,OrderedDict
import numpy as np

def buscar_id(L,a):
    b=0
    for i in L:   
        if(i==a):
            return b
        b+=1

def sort(L):
    A=L
    n = len(A)
    for i in range(1, n):
        for j in range(n-i):
            if A[j][2] > A[j+1][2]:
                A[j], A[j+1] = A[j+1], A[j]
    return A

parent = dict()
rank = dict()

def make_set(vertice):
    parent[vertice] = vertice
    rank[vertice] = 0
def find(vertice):
    if parent[vertice] != vertice:
        parent[vertice] = find(parent[vertice])
    return parent[vertice]
def union(vertice1, vertice2):
    root1 = find(vertice1)
    root2 = find(vertice2)
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
        if rank[root1] == rank[root2]:
            rank[root2] += 1

Arista = namedtuple('Arista', 'inicio, final, peso')

class Grafo(object):
    def __init__(self, aristas):
        self.aristas = [self.generar_arista(*arista) for arista in aristas]

    def generar_arista(self, inicio, final, peso=1):
        return Arista(inicio, final, peso)

    def peso_arista(self, inicio, final):
        for arista in self.aristas:
            if arista.inicio == inicio and arista.final == final:
                return arista.peso
        return 0

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

    @property
    def caminoH(self):
        if(self.hamilton):
            V = []
            Ar = self.obtener_aristas
            a=0
            V.append(Ar[a][0])
            b=0
            D=Ar[a][1]
            a=1
            while(a<len(Ar)):
                if(Ar[a][0]==D):
                    V.append(Ar[a][0])
                    D=Ar[a][1]
                a+=1
            if(a>=len(Ar)):
                a=0
                while(a<len(Ar) and b<1):
                    if(Ar[a][1]==D):
                        V.append(Ar[a][1])
                        D=Ar[a][0]
                        b+=1
                    a+=1
            V.append(Ar[0][0])
            return V
        return "No hay camino hamiltoniano"

    @property
    def euler(self):
        a=0
        if(self.conexa):
            while a <len(self.grados):
                if(self.grados[a]%2!=0):
                    b=a+1
                    while b <len(self.grados):
                        if(self.grados[b]%2!=0):
                            c=b+1
                            while c <len(self.grados):
                                if(self.grados[c]%2!=0):
                                        return False
                                c = c+1
                            return True
                        b = b+1
                    return False
                a = a+1
                return True
        return False

    @property
    def caminoE(self):
         a=0
         b=0
         c=0
         d=0
         e=0
         if(self.euler):
             aristas=[]
             v_actual=self.vertices[0]
             v_camino=[]
             a_recorridas=[]
             while a <len(self.obtener_aristas):
                 aristas.append((self.obtener_aristas[a][0],self.obtener_aristas[a][1]))
                 a=a+1
             while b < len(aristas):
                if v_actual == aristas[b][0] :
                        v_camino.append(v_actual)
                        v_actual=aristas[b][1]
                        a_recorridas.append(aristas[b])
                b=b+1
             if len(a_recorridas) != len(aristas):
                     while c <len(aristas):
                        if v_actual == aristas[c][1] :
                                v_camino.append(v_actual)
                                v_actual=aristas[c][0]
                                a_recorridas.append(aristas[c])
                        c=c+1
             if len(a_recorridas) != len(aristas):
                     while d <len(aristas):
                        if v_actual == aristas[d][0] and aristas[d] not in a_recorridas:
                                v_camino.append(v_actual)
                                v_actual=aristas[d][1]
                                a_recorridas.append(aristas[d])
                        d=d+1
             if len(a_recorridas) != len(aristas):
                     while e <len(aristas):
                        if v_actual == aristas[e][1] and aristas[e] not in a_recorridas:
                                v_camino.append(v_actual)
                                v_actual=aristas[e][0]
                                a_recorridas.append(aristas[e])
                        e=e+1
             v_camino.append(v_actual)
             return v_camino
         return "No hay camino euleriano"

    def kruskal(self):
        for vertice in self.vertices:
            make_set(vertice)
            ar_min=set()
            Ar=sort(self.obtener_aristas)
        for arista in Ar:
            V1,V2,peso=arista
            if(find(V1)!=find(V2)):
                union(V1,V2)
                ar_min.add(arista)
        return sorted(ar_min)
        
    def __str__(self):
        return "Vertices: "+ str(self.vertices) + "\nAristas: " + str(self.obtener_aristas)