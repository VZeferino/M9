import paho.mqtt.client as mqtt
import time
import json
import random
from datetime import datetime
from uuid import uuid4

# Configuração do cliente
client = mqtt.Client("python_publisher")

# Conecte ao broker
client.connect("localhost", 1891, 60)

# Função para gerar ID
def generate_unique_id():
    id = str(uuid4())
    loja = "loja"+random.choice(["A", "B", "C", "D"])
    return f"{loja}-{id[:2]}"

# Função para escolher o tipo de equipamento e definir a faixa de temperatura
def choose_equipment_and_temperature():
    equipment_type = random.choice(["freezer", "geladeira"])
    if equipment_type == "freezer":
        temperature = random.randint(-30, -10)
    else:
        temperature = random.randint(-3, 20)
    return equipment_type, temperature

# Função para gerar informações
def generate_payload():
    equipment_type, temperature = choose_equipment_and_temperature()
    payload = {
        "id": generate_unique_id(),  # Gera um id único para nossa mensagem
        "tipo": equipment_type,  # Informa se é do Freezer ou da Geladeira
        "temperatura": temperature,  # Gera nossa temperatura
        "timestamp": datetime.now().strftime("%d/%m/%Y %H:%M"),  # Quando a mensagem foi enviada
    }
    return payload

# Loop para publicar mensagens continuamente
try:
    while True:
        payload = generate_payload()
        message = json.dumps(payload) # Converte para o formato JSON
        client.publish("test/topic", message)
        print(f"Publicado: {message}")
        time.sleep(2)
except KeyboardInterrupt:
    print("Publicação encerrada")

client.disconnect()

