# MQTT Publisher

Este projeto inclui um script Python que publica mensagens JSON em um tópico MQTT, utilizando o Mosquitto como broker. 
As mensagens contêm dados simulados de medições, respeitando especificações técnicas como faixa de medição e alcance espectral.

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

Segue vídeo para ver minha solução funcionando. Basta clicar [aqui](https://youtu.be/RBNywO2PM0E)
