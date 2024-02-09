import paho.mqtt.client as mqtt
import time
import json
import random

# Configuração do cliente
client = mqtt.Client("python_publisher")

# Conecte ao broker
client.connect("localhost", 1891, 60)

# Função para gerar uma medição aleatória
def generate_measurement():
    measurement = {
        "medicao": f"{int(random.uniform(0, 1280))} W/m2",  # Gera um valor de medição aleatório dentro da faixa 0 a 1280 W/m2
        "espectral": f"{random.randint(300, 1100)} nm",  # Gera um valor aleatório dentro da faixa espectral 300 a 1100 nm
    }
    return measurement

# Loop para publicar mensagens continuamente
try:
    while True:
        measurement = generate_measurement()
        message = json.dumps(measurement) # Converte a medição para o formato JSON
        client.publish("test/topic", message)
        print(f"Publicado: {message}")
        time.sleep(2)
except KeyboardInterrupt:
    print("Publicação encerrada")

client.disconnect()