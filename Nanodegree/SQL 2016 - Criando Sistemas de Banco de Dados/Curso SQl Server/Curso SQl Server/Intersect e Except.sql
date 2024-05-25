use AdventureWorksLT2022;
use Concessionaria;
use Consorcio;
use SeguroVeiculo;

-- saber quais bancos de dados possu�
exec sp_databases;

-- saber quais as tabelas de um banco de dados
exec sp_tables;

-- saber quais as colunas de uma tabela
exec sp_help clientes;

-- retornar todos os dados da tabela
select * from Clientes_2015;

-- cria��o de nova tabela clientes_2015 copiando dados da tabela cliente
select * into Clientes_2015 from Clientes;

-- cria��o de nova tabela clientes_2016 copiando dados da tabela cliente
select * into Clientes_2016 from Clientes;

-- INTERSECT
--Verificar existencia comum em duas tabelas
--Select mesmo numero de colunas
--As colunas comparadas dever�o ter o mesmo tipo de dados

select * from Clientes_2015
order by cadastroSegurado desc;

delete from Clientes_2015
where cadastroSegurado between '2012-06-01' and '2012-07-01';


select * from Clientes_2016;

delete from Clientes_2016
where cadastroSegurado between '2013-06-01' and '2013-07-01';

-- Clientes Mantidos - clientes que est�o nas duas bases
select nomeSegurado from Clientes_2015
intersect
select nomeSegurado from Clientes_2016;

-- clientes que est�o em 2015 e n�o est�o em 2016
select nomeSegurado from Clientes_2015
except
select nomeSegurado from Clientes_2016;

-- clientes que est�o em 2016 e n�o estav�o em 2015
select nomeSegurado from Clientes_2016
except
select nomeSegurado from Clientes_2015;