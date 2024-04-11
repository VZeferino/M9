# 1BRC

Desafio de processamento de um bilhão de linhas.

## Solução

Eu estudei a solução pública em python deste repositório: https://github.com/ifnesi/1brc/tree/main

## Execução

Para rodar, deve-se baixar os arquivos do requirements.txt.

```
pip install -r requirements.txt
```


E depois rodar o arquivo createMeasurements.py para criação do arquivo com 1B. 

```
python3 createMeasurements.py
```

Enfim, basta rodar nosso arquivo de solution.py.

```
python3 solution.py
```

## Explicação

<b>Ler a Lista:</b> Primeiro, lemos essa grande lista, que está em um arquivo de texto, indicando como os dados estão organizados (neste caso, separados por ponto e vírgula) e dizendo que queremos olhar para duas coisas: o nome da estação e a medição feita, utilizando a biblioteca polars.

<b>Organizar os Dados:</b> Depois, agrupamos todas as medições pelo nome da estação.

<b>Calcular:</b> Para cada estação calculamos a menor medição, a média de todas as medições e a maior medição. Isso nos dá uma boa ideia de como estão as condições do ar em cada estação.

<b>Mostrar os Resultados:</b> Por fim, mostramos esses números indicando qual estação cada conjunto de números pertence.

## Resposta

A resposta recebida foi salva no arquivo "response.txt", levou o tempo de aproximadamente 3 minutos para concluir.
