from flask import Flask, request, jsonify
from servicios import matriz, caminoMasCorto, camino, flujo, arbol

application = Flask(__name__)

@application.route('/', methods=['GET'])
def conectar():
    return jsonify(mensaje='Conectado a servicio')

# a. Mostrar matriz de caminos e indicar si el grafo es o no conexo
@application.route('/matriz', methods=['POST'])
def matrizConexo():
    content = request.get_json(silent=True)
    return matriz(content)

# b. Mostrar el camino más corto mostrando la duración y ruta de dicho camino
@application.route('/dijkstra', methods=['POST'])
def dijkstra():
    content = request.get_json(silent=True)
    return caminoMasCorto(content, content['inicio'], content['final'])

# c. Indicar si es hamiltoniano y/o euleriano, y su camino respectivo
@application.route('/camino', methods=['POST'])
def caminoHE():
    content = request.get_json(silent=True)
    return camino(content)

# d. Flujo máximo para un nodo de origen/entrada y otro de destino/salida
@application.route('/flujo', methods=['POST'])
def flujoMax():
    content = request.get_json(silent=True)
    return flujo(content)

# c. Árbol generador mínimo mediante prim o kruskal
@application.route('/arbol', methods=['POST'])
def arbolGen():
    content = request.get_json(silent=True)
    return arbol(content)

if __name__ == '__main__':
    application.run(debug=True, host='localhost', port=5151)