# MQTT Publisher & Subscriber

Este projeto inclui um script Python que publica mensagens JSON em um tópico MQTT e um que recebe, utilizando o Mosquitto como broker. 
As mensagens contêm dados de temperatura de um freezer e uma geladeira.

## Configuração do Mosquitto
Você deve configurar o Mosquitto antes de iniciá-lo. 
Supondo que você tenha um arquivo de configuração chamado mosquitto.conf, você pode iniciar o Mosquitto com a seguinte linha de comando:
```

mosquitto -c mosquitto.conf

```

Esse comando inicia o broker Mosquitto com as configurações definidas em mosquitto.conf.

## Executando o Publisher

Para executar o script do publisher, navegue até o diretório onde o arquivo publisher.py está localizado e execute o seguinte comando no terminal:
```

python3 publisher.py

```

Isso iniciará o script que publicará mensagens JSON simuladas para o tópico MQTT no intervalo definido. O script imprimirá no terminal cada mensagem que for publicada.


## Executando o Subscriber

Para executar o script do subscriber, navegue até o diretório onde o arquivo subscriber.py está localizado e execute o seguinte comando no terminal:
```

python3 subscriber.py

```

Isso iniciará o script que receberá as mensagens JSON simuladas para o tópico MQTT no intervalo definido. O script imprimirá no terminal cada mensagem que for recebida.

Segue vídeo para ver minha solução funcionando. Basta clicar [aqui](https://youtu.be/DbDNo9gbloo)

## Teste

Foi realizado testes para verificar o recebimento de mensagens, segue imagem abaixo;
![Screenshot from 2024-03-08 10-47-47](https://github.com/VZeferino/M9/assets/99190423/05991b2c-f949-40f8-ae8f-7d129277feb7)

