# Sprint 1


## Desafio 


### Evidências

  

1. Criei um diretório chamado ecommerce e inseri o arquivo dados_de_vendas.csv nele
 ![Image](evidencias/Desafio/01.png)

2. Criei um arquivo executável denominado 'processamento_de_vendas.sh', que realizou as seguintes tarefas, usando comandos Linux (Ubuntu 22):

- 2.1. ⁠Criou um diretório denominado ⁠ vendas/ ⁠ e copiou o arquivo ⁠ dados_de_vendas.csv ⁠ para dentro dele.

- 2.2. ⁠Dentro do diretório ⁠ vendas/ ⁠, criar um subdiretório denominado ⁠ backup/ ⁠ e copiou o arquivo ⁠ dados_de_vendas.csv ⁠ para dentro dele com a data de execução como parte do nome do arquivo no padrão yyyymmdd procedido de hifen. 

- 2.3⁠. ⁠Dentro do diretório ⁠ backup/ ⁠, renomeou o arquivo copiado para ⁠ backup-dados-<yyyymmdd>.csv ⁠. 

- 2.4. ⁠Dentro do diretório ⁠ backup/ ⁠, criei um arquivo chamado ⁠ relatorio.txt ⁠com as seguintes informações:

    - Data do sistema operacional, no formato YYYY/MM/DD HH:MI.
    - ⁠Data do primeiro registro de venda contido no arquivo.
    - ⁠Data do ultimo registro de venda contido no arquivo.
    - ⁠A quantidade total de itens diferentes vendidos.
    - ⁠Dentro do diretório ⁠ backup/ ⁠, mostre as 10 primeiras linhas do arquivo ⁠ backup-dados <yyyymmdd>.csv ⁠ e as inclua no diretório ⁠ relatorio.txt ⁠.
- 2.5.⁠ ⁠Comprimiu o arquivo backup-dados-<yyyymmmdd>.csv para backup-dados-<yyyymmmdd>.zip ⁠.
</br>

- 2.6⁠. ⁠Apagou o arquivo ⁠ backup-dados-<yyyymmdd>.csv ⁠ do diretório ⁠ backup/ ⁠ e o arquivo ⁠ dados_de_vendas.csv ⁠ do diretório ⁠ vendas/ ⁠.
  </br>
  </br>
  
![Image](evidencias/02.png)

  </br>
  </br>
  
![Image](evidencias/03.png)

  </br>
  </br>
  
![Image](evidencias/04.png)

  </br>
  </br>
  
![Image](evidencias/05.png)

  </br>
  </br>
  
![Image](evidencias/06.png)

  </br>
  </br>
  
![Image](evidencias/07.png)

  </br>
  </br>
  
5. Além disso, usando o comando *crontab -e* agendei a execução de comandos Linux para executar o script processamento_de_vendas.sh ⁠ todos os dias, de segunda à quinta às 15:27. 
</br>
</br>

![Image](evidencias/08.png)
</br>
</br>

![Image](evidencias/09.png)
</br>
</br>

![Image](evidencias/10.png)
</br>
</br>
6. Por fim, criei um script chamado ⁠ consolidador_de_processamento_de_vendas.sh ⁠ que concatenou todos os relatórios gerados e gerou outro arquivo chamado ⁠ relatorio_final.txt ⁠.
![Image](evidencias/09.png)
</br>
</br>
![Image](evidencias/10.png)
</br>
</br>
![Image](evidencias/11.png)
</br>
</br>
![Image](evidencias/12.png)
</br>
</br>
![Image](evidencias/13.png)
</br>
</br>
![Image](evidencias/14.png)
</br>
</br>
![Image](evidencias/15.png)
</br>
</br>
![Image](evidencias/16.png)
</br>
</br>
![Image](evidencias/17.png)
</br>
</br>

