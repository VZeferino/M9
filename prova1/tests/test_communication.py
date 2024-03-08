import json
import subprocess
import pytest
import paho.mqtt.client as mqtt
import time

# Variáveis de Configuração
BROKER_ADDRESS = "localhost"
BROKER_PORT = 1891
TOPIC = "test/topic"


@pytest.fixture(scope="session", autouse=True)
def setup_mqtt_environment():
    # Inicia o Mosquitto broker
    mosquitto_process = subprocess.Popen([
        "mosquitto", "-p", str(BROKER_PORT)
    ])
    time.sleep(2)  # Broker iniciando

    # Inicia o publisher
    publisher_process = subprocess.Popen(
        ["python3", "src/publisher.py"], cwd="."
    )
    time.sleep(1)  # Publisher iniciando

    yield

    # Finaliza os processos após os testes
    publisher_process.terminate()
    mosquitto_process.terminate()


class MQTTSubscriber:

    def __init__(self, broker_address, broker_port, topic):
        self.client = mqtt.Client("TestSubscriber")
        self.broker_address = broker_address
        self.broker_port = broker_port
        self.topic = topic
        self.received_messages = []

        # Configura callbacks
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

    def on_connect(self, client, userdata, flags, rc):
        self.client.subscribe(self.topic)

    def on_message(self, client, userdata, msg):
        # Adiciona a mensagem decodificada à lista
        self.received_messages.append(json.loads(msg.payload.decode("utf-8")))

    def start(self):
        self.client.connect(self.broker_address, self.broker_port, 60)
        self.client.loop_start()

    def stop(self):
        self.client.loop_stop()
        self.client.disconnect()


@pytest.fixture(scope="module")
def subscriber():
    # Inicializa e inicia o subscriber
    sub = MQTTSubscriber(BROKER_ADDRESS, BROKER_PORT, TOPIC)
    sub.start()
    # Aguarda para acumular mensagens
    time.sleep(8)  # Ajustado devido a frequência do publisher
    yield sub.received_messages
    sub.stop()


def test_recebimento(subscriber):
    assert len(subscriber) > 0, "Deveria ter recebido pelo menos uma mensagem."


def test_confirmacao_da_taxa_de_disparo(subscriber):
    expected_min_messages = 3
    # Define um mínimo esperado baseado na taxa de disparo
    assert len(subscriber) >= expected_min_messages, \
        f"""A taxa de disparo está abaixo do esperado,
        esperava-se pelo menos {expected_min_messages} mensagens."""
