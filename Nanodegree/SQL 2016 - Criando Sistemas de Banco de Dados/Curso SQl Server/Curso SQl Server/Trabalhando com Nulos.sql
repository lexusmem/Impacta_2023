use AdventureWorksLT2022;
use Concessionaria;
use Consorcio;
use SeguroVeiculo;
use SysConVendas;

-- saber quais bancos de dados possu�
exec sp_databases;

-- saber quais as tabelas de um banco de dados
exec sp_tables;

-- saber quais as colunas de uma tabela
exec sp_help;

-- retornar todos os dados da tabela
select * from AdventureWorksLT2022.SalesLT.Product;

-- Fun��o ISNULL - campos sem informa��o
select
	ProductID, Name, isnull(Size, 'Not Inf') as Size, isnull(Weight, '0') as Weight
from AdventureWorksLT2022.SalesLT.Product;

-- Operador IS NULL / IS NOT NULL - Filtrar dados nulos e n�o nulos

-- filtrar nulo e n�o nulos
select
	ProductID, Name, Size, Weight
from AdventureWorksLT2022.SalesLT.Product
where size is null;

select
	ProductID, Name, Size, Weight
from AdventureWorksLT2022.SalesLT.Product
where Weight is null;

select
	ProductID, Name, Size, Weight
from AdventureWorksLT2022.SalesLT.Product
where size is not null;

select
	ProductID, Name, Size, Weight
from AdventureWorksLT2022.SalesLT.Product
where Weight is not null;

use SysConVendas;

-- cria��o de tabela no database sys convendas
CREATE TABLE Cotacao
(
codigo			int					identity,
produto		varchar(50)					not null,
cotacao1		money							null,
cotacao2		money							null,
cotacao3		money							null,
);

insert into Cotacao
values
('Mouse', null, 25, null),
('Impressora', 200, null, 350),
('Monitor', null, null, 500),
('HD Externo', null, null, null);

-- coalesce - retorna o primeiro valor n�o nulo

select * from Cotacao;

select
	produto,
	coalesce(cotacao1, cotacao2, cotacao3, 0) as Cota��o
from Cotacao;

select * from Cotacao
where coalesce(cotacao1, cotacao2, cotacao3, 0) = 0;
