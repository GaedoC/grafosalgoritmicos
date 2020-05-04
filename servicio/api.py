from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from servicios import matriz, camino_mas_corto, camino, flujo, arbol

application = Flask(__name__)
cors = CORS(application, resources={r"/foo": {"origins": "*"}})
application.config['CORS_HEADERS'] = 'Content-Type'

@application.route('/', methods=['GET'])
def conectar():
    return jsonify(mensaje='Conectado a servicio')

# a. Mostrar matriz de caminos e indicar si el grafo es o no conexo
@application.route('/matriz', methods=['POST'])
@cross_origin(origin='*')
def matriz_conexo():
    content = request.get_json(silent=True)
    return matriz(content)

# b. Mostrar el camino más corto mostrando la duración y ruta de dicho camino
@application.route('/dijkstra', methods=['POST'])
@cross_origin(origin='*')
def dijkstra():
    content = request.get_json(silent=True)
    return camino_mas_corto(content)

# c. Indicar si es hamiltoniano y/o euleriano, y su camino respectivo
@application.route('/camino', methods=['POST'])
@cross_origin(origin='*')
def camino_hamilton_euler():
    content = request.get_json(silent=True)
    return camino(content)

# d. Flujo máximo para un nodo de origen/entrada y otro de destino/salida
@application.route('/flujo', methods=['POST'])
@cross_origin(origin='*')
def flujo_maximo():
    content = request.get_json(silent=True)
    return flujo(content)

# c. Árbol generador mínimo mediante Prim o Kruskal
@application.route('/arbol', methods=['POST'])
@cross_origin(origin='*')
def arbol_generador():
    content = request.get_json(silent=True)
    return arbol(content)

if __name__ == '__main__':
    application.run(debug=True, host='localhost', port=5151)