class Grafo(object):
    def __init__(self, grafo_dict=None):
        if grafo_dict == None:
            grafo_dict = {}
        self.__grafo_dict = grafo_dict

    def vertices(self):
        return list(self.__grafo_dict.keys())

    def aristas(self):
        return self.__generar_aristas()

    def agregar_vertice(self, vertice):
        if vertice not in self.__grafo_dict:
            self.__grafo_dict[vertice] = []

    def agregar_arista(self, arista):
        arista = set(arista)
        (vertice1, vertice2) = tuple(arista)
        if vertice1 in self.__grafo_dict:
            self.__grafo_dict[vertice1].append(vertice2)
        else:
            self.__grafo_dict[vertice1] = [vertice2]

    def __generar_aristas(self):
        aristas = []
        for vertice1 in self.__grafo_dict:
            for vertice2 in self.__grafo_dict[vertice1]:
                if {vertice1, vertice2} not in aristas:
                    aristas.append({vertice1, vertice2})
        return aristas

    def camino(self, inicio, final, ruta=[]):
        ruta = ruta + [inicio]
        if inicio == final:
            return ruta
        caminoMasCorto = None
        for nodo in self.__grafo_dict[inicio]:
            if nodo not in ruta:
                nuevaRuta = self.camino(nodo, final, ruta)
                if nuevaRuta:
                    if not caminoMasCorto or len(nuevaRuta) < len(caminoMasCorto):
                        caminoMasCorto = nuevaRuta
        return caminoMasCorto

    def __str__(self):
        respuesta = "vertices: "
        for k in self.__grafo_dict:
            respuesta += str(k) + " "
        respuesta += "\naristas: "
        for arista in self.__generar_aristas():
            respuesta += str(arista) + " "
        return respuesta