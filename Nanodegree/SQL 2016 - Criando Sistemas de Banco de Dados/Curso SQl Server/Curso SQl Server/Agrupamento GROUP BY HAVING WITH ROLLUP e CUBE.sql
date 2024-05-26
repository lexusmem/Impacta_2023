use AdventureWorksLT2022;
use Concessionaria;
use Consorcio;
use SeguroVeiculo;
use SysConVendas;
use SisDep;
use Clientes;

-- saber quais bancos de dados possuí
exec sp_databases;

-- saber quais as tabelas de um banco de dados
exec sp_tables;

-- saber quais as colunas de uma tabela
exec sp_help;

-- retornar todos os dados da tabela Banco: AdventureWorksLT2022.SalesLT
select * from AdventureWorksLT2022.SalesLT.Product;
select * from AdventureWorksLT2022.SalesLT.ProductCategory;

-- retornar todos os dados da tabela Banco: SisDep
select * from Cargo;
select * from Dependente;
select * from Depto;
select * from Localidade;
select * from Projeto;
select * from Funcionario;

-- agrupamento de dados - GROUP BY
-- uma agregação podera consolidar ou totalizar por um deteminado
-- agrupamento de uma ou mais colinas

use SysConVendas;

select * from  Dados;

select sum(total) as faturamento from Dados;

select
					Cidade, sum(total) as 'Faturamento Total'
from			Dados
group by		Cidade;

select
					produto, Cidade, sum(total) as 'Faturamento Total',
					count(*) as [N° de Ocorrências]
from			Dados
group by		Cidade, produto;

-- filtros em agrupamento HAVING

select
					Cidade, sum(total) as 'Faturamento Total'
from			Dados
group by		Cidade
HAVING		SUM(total) > 20000
order by		2;

-- subtotais WITH ROLLUP
select
					Cidade, sum(total) as 'Faturamento Total'
from			Dados
group by		Cidade
with rollup;

select
					Cidade, Produto, sum(total) as 'Faturamento Total'
from			Dados
group by		Cidade, Produto
with rollup;

select
					Cidade, Produto, sum(total) as 'Faturamento Total'
from			Dados
group by		Cidade, Produto
WITH CUBE;

------------------------------
USE SisDep;

-- agrupamento com junções
select
		f.NomeFuncionario, COUNT(*) [N° de Dependente]
from Funcionario as f inner join Dependente as d
on f.idMatricula = d.idMatricula
group by f.NomeFuncionario;