# Explicação do Desafio da Sprint 01 

## Explicação dos passos seguidos para a normalização da tabela "concessionaria"

1. Criei as tabelas normalizadas de cada coluna que tinha id da tabela tb_locacao
2. Na criação das tabelas usei a sintaxe `create table` e criei uma coluna para cada id, especificando o tipo de dado recebido e os parâmetros até onde ele pode ser recebido, como no caso do `VARCHAR()`
3. Na tabela "Locacoes", temos a presença de 3 chaves estrangeiras que foram especificadas como `FOREIGN KEY` por serem o id de outras tabelas
4. Usei o `REFERENCES` para criar vínculo entre a tabela de fato, "Locacoes", e as respectivas tabelas de dimensão, a citar as tabelas "Clientes", "Carros", "Combustiveis" e "Vendedores"


```
CREATE TABLE Clientes (
    idCliente INT PRIMARY KEY,
    nomeCliente VARCHAR(100),
    cidadeCliente VARCHAR(40),
    estadoCliente VARCHAR(40),
    paisCliente VARCHAR(40)
);

CREATE TABLE Carros (
    idCarro INT PRIMARY KEY,
    classiCarro VARCHAR(50),
    marcaCarro VARCHAR(80),
    modeloCarro VARCHAR(80),
    anoCarro INT
);

CREATE TABLE Vendedores (
    idVendedor INT PRIMARY KEY,
    nomeVendedor VARCHAR(100),
    sexoVendedor INT,
    estadoVendedor VARCHAR(40)
);

CREATE TABLE Combustiveis (
    idcombustivel INT PRIMARY KEY,
    tipoCombustivel VARCHAR(20)
);

CREATE TABLE Locacoes (
    idLocacao INT PRIMARY KEY,
    idCliente INT,
    idCarro INT,
    kmCarro DECIMAL,
    idcombustivel INT,
    dataLocacao DATE,
    horaLocacao TIME,
    qtdDiaria INT,
    vlrDiaria DECIMAL,
    dataEntrega DATE,
    horaEntrega TIME,
    idVendedor INT,
    FOREIGN KEY (idCliente) REFERENCES Clientes(idCliente),
    FOREIGN KEY (idCarro) REFERENCES Carros(idCarro),
    FOREIGN KEY (idcombustivel) REFERENCES Combustiveis(idcombustivel),
    FOREIGN KEY (idVendedor) REFERENCES Vendedores(idVendedor)
);

```
5. Após a criação das tabelas, eu inseri os dados da tabela original `tb_locacao` nas tabelas criadas anteriormente, adicionando todos os dados com informações referentes ao nome da tabela
6. Para realizar a inserção eu usei o `INSERT INTO tabela_criada (colunas criadas)` junto com o `SELECT DISTINCT`, para evitar adição de duplicatas, `FROM` tabela original, que é a tb_locacao.

```
-- Inserção dos dados nas tabelas
INSERT INTO Clientes (idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente)
SELECT DISTINCT idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente
FROM tb_locacao;


INSERT INTO Carros (idCarro, classiCarro, marcaCarro, modeloCarro, anoCarro)
SELECT DISTINCT idCarro, classiCarro, marcaCarro, modeloCarro, anoCarro
FROM tb_locacao;


INSERT INTO Combustiveis (idcombustivel, tipoCombustivel)
SELECT DISTINCT idcombustivel, tipoCombustivel
FROM tb_locacao;


INSERT INTO Vendedores (idVendedor, nomeVendedor, sexoVendedor, estadoVendedor)
SELECT DISTINCT idVendedor, nomeVendedor, sexoVendedor, estadoVendedor
FROM tb_locacao;


INSERT INTO Locacoes (idLocacao, idCliente, idCarro, kmCarro, idcombustivel, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega, idVendedor)
SELECT idLocacao, idCliente, idCarro, kmCarro, idcombustivel, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega, idVendedor
FROM tb_locacao;
```

