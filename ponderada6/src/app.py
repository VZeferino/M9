from flask import Flask, request, jsonify
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)

# Conexão com o MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['meu_banco']

# Rota para receber dados via POST e inserir no banco de dados
@app.route('/postdata', methods=['POST'])
def post_data():
    data = request.json  # Assume que o corpo da requisição é um JSON
    topic = data['topic']
    payload = data['payload']
    received_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    document = {
        "topic": topic,
        "payload": payload,
        "received_at": received_at
    }

    # Inserir os dados recebidos no banco de dados SQLite
    try:
        colecao = db['minha_colecao']
        colecao.insert_one(document)
        return jsonify({'message': 'Data inserted successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
