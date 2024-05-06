#!/bin/bash

# Define o diretório onde estão os relatórios
reports_dir="vendas/backup"
output_file="relatorio_final.txt"

# Concatena todos os relatórios em um único arquivo
cat "$reports_dir"/relatorio*.txt > "$output_file"

echo "Consolidação concluída. Arquivo $output_file gerado."
