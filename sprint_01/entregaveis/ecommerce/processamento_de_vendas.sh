#!/bin/bash

# 1. Criar diretório vendas/ e copiar dados_de_vendas.csv para dentro dele
mkdir -p vendas && cp dados_de_vendas.csv vendas/

# 2. Criar subdiretório backup/ e copiar dados_de_vendas.csv com a data de execução no nome
current_date=$(date "+%Y%m%d")
mkdir -p vendas/backup && cp dados_de_vendas.csv vendas/backup/dados-"$current_date".csv

# 3. Renomear o arquivo copiado para backup-dados-<yyyymmdd>.csv
mv vendas/backup/dados-"$current_date".csv vendas/backup/backup-dados-"$current_date".csv

# 4. Criar relatorio.txt com as informações necessárias
{
echo "Data do sistema operacional: $(date "+%Y/%m/%d %H:%M")"
echo "Data do primeiro registro de venda:"
awk -F',' 'NR==2{print $5}' vendas/dados_de_vendas.csv
echo "Data do último registro de venda:"
awk -F',' 'END{print $5}' vendas/dados_de_vendas.csv
echo "Quantidade total de itens diferentes vendidos (excluindo cabeçalho):"
awk -F',' 'NR>1{print $2}' vendas/dados_de_vendas.csv | sort | uniq | wc -l
echo "As 10 primeiras linhas do arquivo backup-dados-$current_date.csv:"
tail -n +2 vendas/backup/backup-dados-"$current_date".csv | head -10
} > vendas/backup/relatorio.txt

# 5. Comprimir o arquivo backup-dados-<yyyymmmdd>.zip
zip -r vendas/backup/backup-dados-"$current_date".zip vendas/backup/backup-dados-"$current_date".csv

# 6. Apagar o arquivo backup-dados-<yyyymmdd>.csv do diretório backup/ e o arquivo dados_de_vendas.csv do diretório vendas/
rm vendas/backup/backup-dados-"$current_date".csv vendas/dados_de_vendas.csv

