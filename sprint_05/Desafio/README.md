# Explicação do Desafio
 

## Explicação dos passos seguidos para a realização da consulta SQL em arquivos diretamente no S3 

1. Baixei uma base de dados do Governo em formato CSV e criei um bucket no S3 da Amazon
![Image](/sprint_05/Evidencias/02.png)
< /br>
2. Após isso, analisei minha base de dados para iniciar a consulta SQL
   ![Image](/sprint_05/Evidencias/04.png)

3. Fazendo uso do Boto3, desenvolvi um código Python para pegar o meu bucket e realizar a consulta SQL com base nele
4. Realizei um código Python que:
   - importasse o boto3;
   - configurasse as minhas credenciais na AWS CLI;
   - definisse o nome do bucket (bucket_name) e a chave do objeto (object_key);
   - realizasse a leitura do arquivo `query.sql`;
   - executasse a consulta S3 select e processasse os dados

```
import boto3

# Configurar o cliente S3 utilizando as credenciais configuradas na AWS CLI
s3_client = boto3.client('s3')

# Nome do bucket e chave do objeto
bucket_name = 'prounibolsas'
object_key = 'prouni_relatorio_bolsas_2020.csv'

# Ler a consulta SQL do arquivo .sql
with open('query.sql', 'r') as file:
    expression = file.read()


# Executar a consulta S3 Select
response = s3_client.select_object_content(
    Bucket=bucket_name,
    Key=object_key,
    ExpressionType='SQL',
    Expression=expression,
    InputSerialization={'CSV': {'FileHeaderInfo': 'USE'}},  # Certificar que a primeira linha é tratada como cabeçalho
    OutputSerialization={'CSV': {}}
)

# Inicializar uma string para armazenar os dados CSV
result_data = ""
for event in response['Payload']:
    if 'Records' in event:
        result_data += event['Records']['Payload'].decode('utf-8')
    elif 'Stats' in event:
        print("Processed: ", event['Stats']['Details']['BytesProcessed'], " bytes")

if result_data:
    print("Results:\n", result_data)
else:
    print("No results found or there was an error in the query.")

```
5. Meu código Python puxou minha consulta sql que teve como objetivo: calcular a média de idade dos beneficiários pardos ou pretos que não são deficientes físicos, que são da região Nordeste e que estão em cursos presenciais.
6. Passando para a query SQL, realizei a seguinte query
```
SELECT COALESCE(
    SUM(
        CASE 
            WHEN REGIAO_BENEFICIARIO = 'NORDESTE'
                 AND BENEFICIARIO_DEFICIENTE_FISICO = 'N' 
                 AND RACA_BENEFICIARIO = 'Parda' OR RACA_BENEFICIARIO = 'Preta' 
            THEN DATE_DIFF('year', TO_TIMESTAMP(DATA_NASCIMENTO, 'dd/MM/yyyy'), UTCNOW()) 
            ELSE 0 
        END
    ) 
    / NULLIF(
        SUM(
            CASE 
                WHEN REGIAO_BENEFICIARIO = 'NORDESTE' 
                     AND BENEFICIARIO_DEFICIENTE_FISICO = 'N' 
                     AND RACA_BENEFICIARIO = 'Parda' OR RACA_BENEFICIARIO = 'Preta'
                THEN 1 
                ELSE 0 
            END
        ), 
        0
    ), 
    0
) AS MEDIA_IDADE 
FROM S3Object s 
WHERE REGIAO_BENEFICIARIO = 'NORDESTE' 
  AND BENEFICIARIO_DEFICIENTE_FISICO = 'N' 
  AND UPPER(MODALIDADE_ENSINO_BOLSA) = 'PRESENCIAL'
  AND RACA_BENEFICIARIO = 'Parda' OR RACA_BENEFICIARIO = 'Preta'
   ```
8. Para isso utilizei:
   - **Dois operadores lógicos:** A cláusula `WHERE` usa múltiplos operadores `AND`.
   - **Duas funções de agregação:** A query usa `SUM` duas vezes.
   - **Uma função condicional:** A query usa `CASE`.
   - **Uma função de conversão:** A query usa `TO_TIMESTAMP`.
   - **Uma função de data:** A query usa `DATE_DIFF` e `UTCNOW`.
   - **Uma função de string:** A query usa `UPPER`.
9. Visto a impossibilidade de usar `GROUP BY`, esse foi o maior número de funções que consegui utilizar em uma única consulta

A query:
- Filtra os beneficiários que são pardos, não deficientes físicos, da região Nordeste e que estão em cursos presenciais.
-  Calcula a diferença de anos entre a data de nascimento e a data atual para esses beneficiários.
- Soma essas diferenças para obter a soma total das idades.
- Conta o número de beneficiários que atendem aos critérios.
- Calcula a média das idades dividindo a soma total das idades pelo número de beneficiários.
- Usa `COALESCE` para garantir que, se não houver beneficiários que atendam aos critérios, a média de idade seja retornada como 0.

10. Imagens da execução do código Python
![Image](/sprint_05/Evidencias/05.png)
![Image](/sprint_05/Evidencias/07.png)

11. A média de idade dos beneficiários pardos ou pretos que não são deficientes físicos, que são da região Nordeste e que estão em cursos presenciais é 26 anos 
