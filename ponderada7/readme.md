# Descrição
Nesse projeto temos um publisher publicando mensagem no hive que está integrado com o Kafka e um consumer que pega as mensagens dele.

# Execução
Para executar o projeto, basta seguir os passos abaixo:

Execução do producer:

```
python3 publisher.py
``` 

Execução do consumer:

```
python3 consumer.py
``` 

Para o teste que roda os dois em subprocess:

```
python3 test.py
``` 

No vídeo temos a integração funcionando, mostrando que a mensagem enviada ao hivemq foi recebida no kafka.

# Demonstração:

Segue vídeo para ver minha solução funcionando. Basta clicar [aqui](https://youtu.be/T-TQKLrBvw0)

