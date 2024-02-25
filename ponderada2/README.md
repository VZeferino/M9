# MQTT Publisher & Subscriber

Este projeto inclui um script Python que publica mensagens JSON em um tópico MQTT e um que recebe, utilizando o Mosquitto como broker. 
As mensagens contêm dados simulados de medições, respeitando especificações técnicas como faixa de medição e alcance espectral.

## Teste

Pare executar o teste, basta rodar o comando:

obs: não se esqueça de ativar a venv antes. 
source venv/bin/activate

```

tox run-parallel

```

Como se trata de 3 ambientes diferentes;

pytest,
flake8 e
mypy.

Assim os testes serão iniciados ao mesmo tempo. 

Segue vídeo para ver minha solução funcionando. Basta clicar [aqui](https://youtu.be/7PO8NBFy_7w)
