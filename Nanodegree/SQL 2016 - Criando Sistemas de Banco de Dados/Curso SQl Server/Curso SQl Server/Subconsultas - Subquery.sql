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

-- SUBCONSULTAS - subquery
-- select dentro de select

select * from clientes_2015;
select * from clientes_2016;

-- quais clientes na base 2015 estão tambem na base 2016
select * from clientes_2015 c15
where
			EXISTS
			(
			select c15.ncontrato from clientes_2016 c16
			where c15.ncontrato = c16.ncontrato
			);

select * from clientes_2015 as c15
where c15.ncontrato in (select c16.ncontrato from clientes_2016 as c16);

-- quais clientes na base 2015 não estão na base 2016
select * from clientes_2015 as c15
where
			NOT EXISTS
			(
			select c15.ncontrato from clientes_2016 as c16
			where c15.nContrato = c16.nContrato
			);

select * from clientes_2015 as c15
where c15.ncontrato not in (select c16.ncontrato from clientes_2016 as c16);

use sisdep;
select * from funcionario;

-- nome funcionarios que possuam dependentes
select
			f.NomeFuncionario
from	funcionario as f
where	f.idMatricula in(select d.idMatricula from Dependente d);

select f.NomeFuncionario  from Funcionario f
where exists(
						select f.idMatricula  from Dependente d
						where f.idMatricula = d.idMatricula
);

-- nome funcionarios que não possuam dependentes
select
			f.NomeFuncionario
from	funcionario as f
where	f.idMatricula not in(select d.idMatricula from Dependente d);

select f.NomeFuncionario from funcionario f
where not exists(
								select f.idMatricula from Dependente d
								where f.idMatricula = d.idMatricula
);

-- subconsultas com operadores relacionais
-- retornar funcionarios acima da media salarial

select avg(salario) from Funcionario;

select
			NomeFuncionario, Admissao, Salario
from Funcionario
where Salario > (select avg(salario) from Funcionario)
order by Salario asc;