-- Criação das tabelas normalizadas


SELECT * FROM Locacoes l  

CREATE TABLE Clientes (
    idCliente INT PRIMARY KEY,
    nomeCliente VARCHAR,
    cidadeCliente VARCHAR,
    estadoCliente VARCHAR,
    paisCliente VARCHAR
);

CREATE TABLE Carros (
    idCarro INT PRIMARY KEY,
    classiCarro VARCHAR,
    marcaCarro VARCHAR,
    modeloCarro VARCHAR,
    anoCarro INT
);

CREATE TABLE Vendedores (
    idVendedor INT PRIMARY KEY,
    nomeVendedor VARCHAR,
    sexoVendedor INT,
    estadoVendedor VARCHAR
);

CREATE TABLE Combustiveis (
    idcombustivel INT PRIMARY KEY,
    tipoCombustivel VARCHAR
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
SELECT DISTINCT idLocacao, idCliente, idCarro, kmCarro, idcombustivel, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega, idVendedor
FROM tb_locacao;
