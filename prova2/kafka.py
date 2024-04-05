from confluent_kafka import Producer, Consumer, KafkaError
import json
from datetime import datetime
from rich.console import Console
from rich.table import Table

# Configurações do produtor
producer_config = {
    'bootstrap.servers': 'localhost:29092,localhost:39092',
    'client.id': 'python-producer'
}

# Configurações do consumidor
consumer_config = {
    'bootstrap.servers': 'localhost:29092,localhost:39092',
    'group.id': 'python-consumer-group',
    'auto.offset.reset': 'earliest'
}

# Criar produtor
producer = Producer(**producer_config)

# Função de callback para confirmação de entrega
def delivery_callback(err, msg):
    if err:
        print(f'Message delivery failed: {err}')
    else:
        print(f'Message delivered to {msg.topic()} [{msg.partition()}]')

# Enviar mensagem
topic = 'qualidadeAr'
message = {
    "idSensor": "sensor",
    "timestamp": datetime.now().strftime("%d/%m/%Y %H:%M"),
    "tipoPoluente": "PM2",
    "nivel": 35
}

producer.produce(topic, json.dumps(message).encode('utf-8'), callback=delivery_callback)

# Aguardar a entrega de todas as mensagens
producer.flush()

# Criar consumidor
consumer = Consumer(**consumer_config)
console = Console()

# Assinar tópico
consumer.subscribe([topic])

def format_and_display_message(message):
    table = Table(show_header=True, header_style="bold blue")
    table.add_column("ID do Sensor", justify="center")
    table.add_column("Timestamp", justify="center")
    table.add_column("Tipo de Poluente", justify="center")
    table.add_column("Nível", justify="center")

    table.add_row(
        message["idSensor"],
        message["timestamp"],
        message["tipoPoluente"],
        str(message["nivel"])
    )

    console.print(table)

# Consumir mensagens
try:
    while True:
        msg = consumer.poll(timeout=1.0)
        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                continue
            else:
                print(msg.error())
                break
        message_received = json.loads(msg.value().decode("utf-8"))
        message_data = json.dumps(message_received, indent=4)
        # Gravando a string JSON em um arquivo
        with open("dados.json", "w") as arquivo:
            arquivo.write(message_data)
        # Formata e mostra a mensagem
        format_and_display_message(message_received)
except KeyboardInterrupt:
    pass
finally:
    # Fechar consumidor
    consumer.close()