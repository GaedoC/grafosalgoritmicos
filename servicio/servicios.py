from flask import jsonify
from grafo import Grafo


def parsearGrafo(grafo):
    aristasParseadas = []
    for arista in grafo['aristas']:
        tupla = (arista["inicio"], arista["final"], arista["peso"])
        aristasParseadas.append(tupla)
    return Grafo(aristasParseadas, grafo['vertices'])


def matriz(json):
    grafo = parsearGrafo(json)
    return jsonify(matriz=grafo.matriz, conexo=grafo.conexa)


def caminoMasCorto(grafo, inicio, final):
    grafo = parsearGrafo(grafo)
    dijkstra = grafo.dijkstra(inicio, final)
    return jsonify(ruta=dijkstra[0], duración=dijkstra[1])


def camino(grafo):
    resultado = []
    grafo = parsearGrafo(grafo)
    resultado.append({"hamiltoniano": grafo.hamilton})
    if (grafo.hamilton):
        resultado.append({"caminoHamiltoniano": grafo.caminoH})
    resultado.append({"euleriano": grafo.euler})
    if (grafo.euler):
        resultado.append({"caminoEuleriano": grafo.caminoE})
    return jsonify(resultado)


def flujo(grafo):
    # Lógica para indicar flujo máximo
    return jsonify(flujo=True)


def arbol(grafo):
    # Lógica para definir árbol generador mínimo
    return jsonify(arbol=True)
