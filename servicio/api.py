from flask import Flask, request, jsonify
from servicios import definirGrafo, caminoMasCorto

application = Flask(__name__)

@application.route('/', methods=['GET'])
def conectar():
    return jsonify(mensaje='Conectado a servicio')

@application.route('/grafo', methods=['POST'])
def grafo():
    content = request.get_json(silent=True)
    return definirGrafo(content['grafo'])

@application.route('/camino', methods=['POST'])
def camino():
    content = request.get_json(silent=True)
    return caminoMasCorto(content['grafo'], content['inicio'], content['final'])

if __name__ == '__main__':
    application.run(debug=True, host='localhost', port=5151)
