import os
import pytest
from dotenv import load_dotenv
import subprocess
import time

# Carrega as variáveis de ambiente
load_dotenv()

# Variáveis de Configuração
BROKER_ADDRESS = os.getenv("BROKER_ADDR")
BROKER_PORT = 8883  # Porta padrão TLS para HiveMQ
TOPIC = "my/test/topic"
username = os.getenv("HIVE_USER")
password = os.getenv("HIVE_PSWD")


@pytest.fixture(scope="module")
def mqtt_processes():
    # Caminho para os scripts do publisher e subscriber
    publisher_script = "src/publisher.py"
    subscriber_script = "src/subscriber.py"

    # Inicia o subscriber como um subprocesso e captura a saída
    subscriber_process = subprocess.Popen(
        ["python", subscriber_script],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True  # Garante que a saída seja tratada como texto
    )

    # Dá um tempo para o subscriber se conectar
    time.sleep(2)

    # Inicia o publisher como um subprocesso
    publisher_process = subprocess.Popen(
        ["python", publisher_script],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True
    )

    # Aguarda o publisher terminar
    publisher_process.wait()

    # Dá um tempo para mensagens serem recebidas
    time.sleep(5)

    # Encerra o subscriber e captura a saída
    subscriber_output, _ = subscriber_process.communicate(timeout=10)
    subscriber_process.terminate()

    yield subscriber_output


def test_recebimento(mqtt_processes):
    expected_messages = ["Hello", "Hello1", "Hello2", "Hello3"]
    subscriber_output = mqtt_processes

    # Verifica se cada mensagem esperada foi recebida
    for expected_message in expected_messages:
        assert expected_message in subscriber_output, "Error."
