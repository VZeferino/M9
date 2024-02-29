import os
import pytest
from dotenv import load_dotenv
import paho.mqtt.client as paho
import time
import subprocess


load_dotenv()

# Variáveis de Configuração
BROKER_ADDRESS = os.getenv("BROKER_ADDR")
BROKER_PORT = 8883  # Ajuste para a porta correta do seu broker MQTT
TOPIC = "my/test/topic"
username = os.getenv("HIVE_USER")
password = os.getenv("HIVE_PSWD")

if BROKER_ADDRESS is None:
    raise ValueError("A variável de ambiente 'BROKER_ADDR' não está definida.")
print(f"BROKER_ADDRESS: {BROKER_ADDRESS}")  # Para depuração


class MQTTSubscriber:

    def __init__(self, BROKER_ADDRESS, broker_port, topic, username, password):
        self.client = paho.Client(
            paho.CallbackAPIVersion.VERSION2, "TestSubscriber"
        )
        self.BROKER_ADDRESS = BROKER_ADDRESS
        self.broker_port = broker_port
        self.topic = topic
        self.received_messages = []

        if username and password:
            self.client.username_pw_set(
                username, password
            )  # Configura as credenciais

        # Configura callbacks
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

    def on_connect(self, client, userdata, flags, rc):
        print(f"Connected with result code {rc}")
        self.client.subscribe(self.topic)

    def on_message(self, client, userdata, msg):
        # Adiciona a mensagem decodificada à lista
        self.received_messages.append(msg.payload.decode("utf-8"))

    def start(self):
        self.client.connect(self.BROKER_ADDRESS, self.broker_port, 60)
        self.client.loop_start()

    def stop(self):
        self.client.loop_stop()
        self.client.disconnect()


@pytest.fixture(scope="module")
def subscriber():
    sub = MQTTSubscriber(
        BROKER_ADDRESS, BROKER_PORT, TOPIC, username, password
    )
    sub.start()
    time.sleep(1)  # Dê um tempo

    publisher_process = subprocess.Popen(
        ["python3", "src/publisher.py"], cwd="."
    )

    time.sleep(4)

    received_messages = sub.received_messages.copy()

    sub.stop()
    publisher_process.terminate()

    yield received_messages  # Use a cópia das mensagens


def test_recebimento(subscriber):
    assert len(subscriber) > 0, "Deveria ter recebido pelo menos uma mensagem."


def test_validacao_mensagem_hello(subscriber):
    # Verifica mensagem
    assert "hello" in subscriber, "Erro"
