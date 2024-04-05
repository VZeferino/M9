import json
from confluent_kafka import Producer, Consumer, KafkaError
import pytest
from datetime import datetime

producer_config = {
    'bootstrap.servers': 'localhost:29092,localhost:39092',
    'client.id': 'test-producer'
}

consumer_config = {
    'bootstrap.servers': 'localhost:29092,localhost:39092',
    'group.id': 'test-consumer-group',
    'auto.offset.reset': 'earliest'
}

topic = 'qualidadeAr'

message = {
    "idSensor": "sensor",
    "timestamp": datetime.now().strftime("%d/%m/%Y %H:%M"),
    "tipoPoluente": "PM2",
    "nivel": 35
}

def send_message(producer, topic, message):
    def acked(err, msg):
        assert err is None
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")
    producer.produce(topic, json.dumps(message).encode('utf-8'), callback=acked)
    producer.flush()

@pytest.fixture(scope="module")
def kafka_producer():
    producer = Producer(**producer_config)
    yield producer
    producer.flush()

@pytest.fixture(scope="module")
def kafka_consumer():
    consumer = Consumer(**consumer_config)
    consumer.subscribe([topic])
    yield consumer
    consumer.close()

def test_integrity(kafka_producer, kafka_consumer):
    send_message(kafka_producer, topic, message)
    msg = kafka_consumer.poll(timeout=10)
    assert msg is not None
    assert not msg.error()
    received_message = json.loads(msg.value().decode("utf-8"))
    assert received_message["idSensor"] == message["idSensor"], "ID do Sensor divergente"
    assert received_message["tipoPoluente"] == message["tipoPoluente"], "Tipo de Poluente divergente"
    assert received_message["nivel"] == message["nivel"], "Nível divergente"


def test_persistence(kafka_producer, kafka_consumer):
    first = open("dados.json", "r")
    send_message(kafka_producer, topic, message)
    msg = kafka_consumer.poll(timeout=10)
    assert msg is not None
    assert not msg.error()
    message_received = json.loads(msg.value().decode("utf-8"))
    message_data = json.dumps(message_received, indent=4)
    with open("dados.json", "w") as arquivo:
        arquivo.write(message_data)
    second = open("dados.json", "r")
    assert first.read() == second.read(), "Message persistence compromised!"
