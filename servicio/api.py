from flask import Flask, request, jsonify
from grafo import Grafo

api = Flask(__name__)

@api.route('/', methods=['GET'])
def conectar():
    return {"mensaje": 'Conectado a servicio'}

@api.route('/grafo', methods=['POST'])
def grafo():
    content = request.get_json(silent=True)
    return jsonify(vertices=len(grafo.vertices()), aristas=len(grafo.aristas()))

@api.route('/camino', methods=['POST'])
def camino():
    content = request.get_json(silent=True)
    grafo = Grafo(content['grafo'])
    return jsonify(caminoMasCorto=grafo.camino(content['inicio'], content['final']))

if __name__ == '__main__':
    api.run(debug=True, host='localhost', port=5151)
