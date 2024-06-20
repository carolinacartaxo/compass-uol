CREATE VIEW FatoLocacoes AS
SELECT
    L.idLocacao AS "ID da locação",
    L.qtdDiaria AS "Quantidade de diárias",
    L.vlrDiaria AS "Valor da diária",
    L.dataEntrega AS "Data de entrega",
    L.horaEntrega AS "Hora de entrega",
    C.idCliente AS "ID do cliente",
    Car.idCarro AS "ID do carro",
    V.idVendedor AS "ID do vendedor",
    Com.idcombustivel AS "ID do combustível"
FROM
    Locacoes L               
JOIN
    Clientes C ON L.idCliente = C.idCliente        
JOIN
    Carros Car ON L.idCarro = Car.idCarro           
JOIN
    Vendedores V ON L.idVendedor = V.idVendedor    
JOIN
    Combustiveis Com ON L.idcombustivel = Com.idcombustivel; 

   
CREATE VIEW DimensaoClientes AS
SELECT idCliente AS "ID do cliente",
       nomeCliente as "Nome do cliente",
       cidadeCliente as cidade,
       estadoCliente as estado,
       paisCliente as "país"
FROM Clientes;

CREATE VIEW DimensaoCarros AS
SELECT idCarro as "ID do carro",
       classiCarro as "Classificação do carro",
       marcaCarro as "Marca do carro",
       modeloCarro as "Modelo do carro",
       anoCarro as "Ano do carro"
FROM Carros;

CREATE VIEW DimensaoCombustiveis AS
SELECT idcombustivel as "ID do combustível",
       tipoCombustivel as "Tipo de combustível"
FROM Combustiveis;

CREATE VIEW DimensaoVendedores AS
SELECT idVendedor as "ID do vendedor",
       nomeVendedor as "Nome do vendedor",
       sexoVendedor as sexo,
       estadoVendedor as estado
FROM Vendedores;

CREATE VIEW DimensaoTempo AS
SELECT DISTINCT
       dataLocacao AS "Data da locação",
       strftime('%Y', dataLocacao) AS ano,
       strftime('%m', dataLocacao) AS mes,
       strftime('%d', dataLocacao) AS dia,
       dataEntrega AS "data de entrega",
       strftime('%Y', dataEntrega) AS ano,
       strftime('%m', dataEntrega) AS mes,
       strftime('%d', dataEntrega) AS dia
FROM Locacoes;







