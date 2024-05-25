use AdventureWorksLT2022;
use Concessionaria;
use Consorcio;
use SeguroVeiculo;
use SysConVendas;
use SisDep;

-- saber quais bancos de dados possu�
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

-- LEFT OUTER JOIN
-- Jun��es externas
-- for�a a retornar todos os dados da tabela a esquerda do join da tabela a direita
-- somente os dados que existirem nas duas

select
				f.NomeFuncionario,
				ISNULL (d.NomeDependente,'N�o Possu� Dependente') as NomeDependente,
				ISNULL (d.NascimentoDependente,'') as NascimentoDependente
from		Funcionario as f left outer join Dependente as d
on			f.idMatricula = d.idMatricula
order by	f.NomeFuncionario;

-- RIGHT OUTER JOIN
-- Jun��es externas
-- for�a a retornar todos os dados da tabela a direita do join da tabela a esquerda
-- somente os dados que existirem nas duas

select
					isnull(f.NomeFuncionario,'N�o Possu� Funcionario') as NomeFuncion�rios,
					c.NomeCargo,
					f.Salario
from			Funcionario as f right join Cargo as c
on				f.idCargo = c.idCargo
where			f.NomeFuncionario is null;
