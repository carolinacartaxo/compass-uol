# Pasta com os exercícios realizados na sprint.
As imagens da execução com o passo a passo completo de cada exercício, encontram-se em suas respectivas pastas.

## Exercício 1 - Lab AWS S3 
Após configurar a hospedagem de site estático para o meu bucket, realizei o teste e consegui hospedar o site no Amazon S3.  
![Image](/sprint_06/Exercicios/exercicio1/0114.png)

![Image](/sprint_06/Exercicios/exercicio1/0115.png)

## Exercício 2 - Lab AWS Athena 
Criei uma consulta que lista os 3 nomes mais usados em cada década desde o 1950 até hoje.
Para isso, precisei usar Common Table Expressions, que são tabelas temporárias que otimizam o tempo de consulta, visto que da forma tradicional usando `DISTINCT` a consulta SQL não carregava por conta do volume de dados. 

```
WITH ranked_names AS (
    SELECT
        nome,
        sexo,
        total,
        ano,
        (ano - (ano % 10)) AS decada,
        ROW_NUMBER() OVER (PARTITION BY (ano - (ano % 10)), nome ORDER BY total DESC) AS rank
    FROM
        meubanco.tabela1
    WHERE
        ano >= 1950
),
distinct_names AS (
    SELECT
        decada,
        nome,
        total,
        ROW_NUMBER() OVER (PARTITION BY decada ORDER BY total DESC) AS rank
    FROM
        ranked_names
    WHERE
        rank = 1
)
SELECT
    decada,
    nome,
    total
FROM
    distinct_names
WHERE
    rank <= 3
ORDER BY
    decada,
    rank;
```
Usei a função `ROW_NUMBER()` para dar uma classificação (rank) a cada nome dentro de cada década, ordenado pelo total de registros do nome em ordem decrescente. A classificação se reinicia para cada década para evitar a repetição. 

![Image](/sprint_06/Exercicios/exercicio2/0211.png)

## Exercício 3 - Lab AWS Lambda
Neste exercício, apesar de realizar todo o passo a passo, o guia está desatualizado e o Lambda não possui mais a versão do Python 3.7, então o arquivo docker não funcionou pois não era compatível com as versões corretas. 

Após consultar alguns colegas sobre a atividade, rodei outro script docker tentando baixar a layer necessária para a versão 3.9 do Python, porém, apesar de ter conseguido baixar a versão correta, o Lambda ainda asim deu

![Image](/sprint_06/Exercicios/exercicio3/0319.png)
![Image](/sprint_06/Exercicios/exercicio3/0310.png)
![Image](/sprint_06/Exercicios/exercicio3/0311.png)
![Image](/sprint_06/Exercicios/exercicio3/0312.png)
![Image](/sprint_06/Exercicios/exercicio3/0313.png)
![Image](/sprint_06/Exercicios/exercicio3/0314.png)
![Image](/sprint_06/Exercicios/exercicio3/0316.png)
