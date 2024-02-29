# MQTT Publisher & Subscriber HIVEMQ

Este projeto inclui um script Python que publica mensagens JSON em um tópico MQTT e um que recebe, utilizando o HIVEMQ.

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

## Executando os Testes

Para executar o teste, execute o seguinte comando no terminal:
```

tox run-parallel

```

Aqui nós executamos o pytest, flake8, mypy.

obs: rodando os arquivos individualmente a conexão não apresenta erros.

Segue vídeo para ver minha solução funcionando. Basta clicar [aqui](https://youtu.be/F0zHeoOlvSo)
