import paho.mqtt.client as mqtt
import json

# Callback quando uma mensagem é recebida do servidor.
def on_message(client, userdata, message):
    msg = json.loads(message.payload.decode())
    print(f"Recebido: {msg}")

    # Verifica o tipo e a temperatura
    tipo = msg.get("tipo")
    temperatura = msg.get("temperatura")
    
    # Condições baseadas no tipo e verifica se a temperatura está fora da faixa
    if tipo == "freezer" and not (-25 <= temperatura <= -15):
        print(f"[ALERTA: Temperatura fora da faixa ({temperatura}°C)]")
        print("..................")
    elif tipo == "geladeira" and not (2 <= temperatura <= 10):
        print(f"[ALERTA: Temperatura fora da faixa ({temperatura}°C)]")
        print("..................")

# Callback para quando o cliente recebe uma resposta CONNACK do servidor.
def on_connect(client, userdata, flags, rc, properties=None):
    print("Conectado com código de resultado "+str(rc))
    # Inscrito no tópico
    client.subscribe("test/topic")

# Configuração do cliente
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "python_subscriber")
client.on_connect = on_connect
client.on_message = on_message

# Conecte ao broker
client.connect("localhost", 1891, 60)

# Loop para manter o cliente executando e escutando por mensagens
client.loop_forever()

def on_message(client, userdata, message):
    # Decodifica a mensagem JSON recebida
    msg = json.loads(message.payload.decode())
    print(f"Recebido: {msg}")