from flask import Flask, request, jsonify
import sqlite3
from datetime import datetime

app = Flask(__name__)

# Rota para receber dados via POST e inserir no banco de dados
@app.route('/postdata', methods=['POST'])
def post_data():
    data = request.json  # Assume que o corpo da requisição é um JSON
    topic = data['topic']
    payload = data['payload']
    received_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Inserir os dados recebidos no banco de dados SQLite
    try:
        conn = sqlite3.connect('sensor_data.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Messages (topic, payload, received_at) VALUES (?, ?, ?)", 
                       (topic, payload, received_at))
        conn.commit()
        return jsonify({'message': 'Data inserted successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        conn.close()

if __name__ == '__main__':
    app.run(debug=True, port=5000)
