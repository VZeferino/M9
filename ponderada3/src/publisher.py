import os
from dotenv import load_dotenv
import paho.mqtt.client as paho
from paho import mqtt

load_dotenv() # Le variáveis de ambiente do arquivo .env

# Configurações do broker
broker_address = os.getenv("BROKER_ADDR")
port = 8883
topic = "my/test/topic"
username = os.getenv("HIVE_USER")
password = os.getenv("HIVE_PSWD")

def on_connect(client, userdata, flags, reason_code, properties):
    print(f"CONNACK received with code {reason_code}")

def on_publish(client, userdata, mid, reason_code, properties):
    print(f"Mid: {mid}")

# print message, useful for checking if it was successful
def on_message(client, userdata, msg):
    print(f"{msg.topic} (QoS: {msg.qos}) - {msg.payload.decode('utf-8')}")

# Instanciação do cliente
client = paho.Client(paho.CallbackAPIVersion.VERSION2, "Publisher",
                     protocol=paho.MQTTv5)
client.on_connect = on_connect

# Configurações de TLS
client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
client.username_pw_set(username, password)  # Configuração da autenticação

client.on_message = on_message
client.on_publish = on_publish

# Conexão ao broker
client.connect(broker_address, port=port)

client.publish(topic, payload="Hello", qos=1)

# Loop de espera por mensagens
client.loop_forever()