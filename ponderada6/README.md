# MQTT Metabase e Integração com Banco de Dados via API

Este projeto inclui um script Python que publica mensagens JSON em um tópico MQTT e um que recebe, utilizando o Mosquitto como broker. 
As mensagens contêm dados simulados de medições, respeitando especificações técnicas como faixa de medição e alcance espectral. Além disso, o projeto integra essas mensagens a um banco de dados SQL através de uma API, e os dados são visualizados usando o Metabase.

## API e Banco de Dados

O subscriber envia as mensagens recebidas para uma API Flask, que então insere esses dados em um banco de dados SQL.

Para executar a API Flask, navegue até o diretório onde o arquivo app.py está localizado e execute:
```

python3 app.py

```

Isso iniciará o servidor Flask, pronto para receber e processar as mensagens enviadas pelo subscriber.

Os dados inseridos no banco são visualizados utilizando o Metabase, uma ferramenta de visualização de dados. Configure o Metabase para se conectar ao banco de dados SQL utilizado pelo projeto para explorar e visualizar os dados recebidos em tempo real.

Segue comando abaixo para colocar o metabase no ar:

```

sudo docker run -d -p 12345:3000 \
  --name metabase \
  -v [caminho para seu banco local]:/db \
  metabase/metabase

```

Segue vídeo para ver minha solução funcionando. Basta clicar [aqui](https://youtu.be/Gyk1jiX4-rI)
