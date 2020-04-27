from flask import jsonify
from grafo import Grafo

def parsearGrafo(grafo):
    grafoParseado = []
    for nodo in grafo:
        tupla = (nodo["0"], nodo["1"], nodo["2"])
        grafoParseado.append(tupla)
    return Grafo(grafoParseado)

def definirGrafo(grafo):
    grafo = parsearGrafo(grafo)
    print('-- Grafo --')
    print(grafo)
    jsonify(vertices=len(grafo.vertices), aristas=len(grafo.obtener_aristas))

def caminoMasCorto(grafo, inicio, final):
    grafo = parsearGrafo(grafo)
    print('-- Grafo --')
    print(grafo)
    return jsonify(caminoMasCorto=grafo.dijkstra(inicio, final))