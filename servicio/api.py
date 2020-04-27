from flask import Flask, request, jsonify
from servicios import definirGrafo, caminoMasCorto

api = Flask(__name__)

@api.route('/', methods=['GET'])
def conectar():
    return {"mensaje": 'Conectado a servicio'}

@api.route('/grafo', methods=['POST'])
def grafo():
    content = request.get_json(silent=True)
    return definirGrafo(content['grafo'])

@api.route('/camino', methods=['POST'])
def camino():
    content = request.get_json(silent=True)
    return caminoMasCorto(content['grafo'], content['inicio'], content['final'])

if __name__ == '__main__':
    api.run(debug=True, host='localhost', port=5151)