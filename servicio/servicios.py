from flask import jsonify
from grafo import Grafo

def parsear_grafo(grafo):
    aristas_parseadas = []
    for arista in grafo['aristas']:
        tupla = (arista['inicio'], arista['final'], arista['peso'])
        aristas_parseadas.append(tupla)
    return Grafo(aristas_parseadas, grafo['vertices'])

def matriz(json):
    grafo = parsear_grafo(json['grafo'])
    return jsonify(vertices=grafo.vertices, largo=json['largo'], matriz=grafo.matriz_caminos_largo_n(json['largo']), esConexo=grafo.es_conexo)

def camino_mas_corto(json):
    grafo = parsear_grafo(json['grafo'])
    dijkstra = grafo.dijkstra(json['inicio'], json['final'])
    return jsonify(ruta=dijkstra[0], pesoTotal=dijkstra[1])

def camino(json):
    resultado = []
    grafo = parsear_grafo(json['grafo'])
    resultado.append({'hamiltoniano': grafo.hamilton})
    if (grafo.hamilton):
        resultado.append({'caminoHamiltoniano': grafo.camino_hamiltoniano})
    resultado.append({'euleriano': grafo.euler})
    if (grafo.euler):
        resultado.append({'caminoEuleriano': grafo.camino_euleriano})
    return jsonify(resultado)

def flujo(json):
    # Lógica para indicar flujo máximo
    return jsonify(flujo=True)

def arbol(json):
    grafo = parsear_grafo(json['grafo'])
    return jsonify(arbol=grafo.kruskal)