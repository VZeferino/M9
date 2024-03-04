import paho.mqtt.client as mqtt
import requests

# Callback quando uma mensagem é recebida do servidor.
def on_message(client, userdata, message):
    payload = message.payload.decode()
    print(f"Recebido: {message.payload.decode()} no tópico {message.topic}")

    api_url = "http://localhost:5000/postdata"

    data = {'topic': message.topic, 'payload': payload}

    try:
        response = requests.post(api_url, json=data)
        print("Dados enviados para a API:", response.json())
    except Exception as e:
        print("Erro ao enviar dados para a API:", e)

# Callback para quando o cliente recebe uma resposta CONNACK do servidor.
def on_connect(client, userdata, flags, rc, properties=None):
    print("Conectado com código de resultado "+str(rc))
    # Inscreva no tópico aqui, ou se perder a conexão e se reconectar, então as
    # subscrições serão renovadas.
    client.subscribe("test/topic")

# Configuração do cliente
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "python_subscriber")
client.on_connect = on_connect
client.on_message = on_message

# Conecte ao broker
client.connect("localhost", 1891, 60)

# Loop para manter o cliente executando e escutando por mensagens
client.loop_forever()