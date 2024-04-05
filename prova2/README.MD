# Descrição
Nesse projeto usando o kafka foi criado uma simulação de sensor, um pusliher e um consumer, além de salvar a mensagem em um arquivo .json 😉 e dois testes, integridade e persistência.

# Dependências
Imagens do Zookeeper e do Kafka

# Instalação
Para instalação, basta abrir um terminal e digitar o seguinte comando:

```
docker compose up
``` 

Com isso, as imagens do zookeeper e kafka irão ser instaladas na máquina e o cluster irá iniciar.

# Execução
Para executar o projeto, basta seguir os passos abaixo:

Execução do arquivo consumer/producer:

```
python3 kafka.py
``` 

Para os testes:
```
python3 -m pytest
``` 

# Demonstração:

Segue vídeo para ver minha solução funcionando. Basta clicar [aqui](https://youtu.be/2OYumPWR7zk)
