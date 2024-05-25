use AdventureWorksLT2022;
use Concessionaria;
use Consorcio;
use SeguroVeiculo;
use SysConVendas;
use SisDep;

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

-- FULL JOIN
-- junções totais dos dados da direita e esquerda de join

select
					f.NomeFuncionario,
					f.Admissao,
					d.NomeDependente,
					d.NascimentoDependente
from			Funcionario as f full join Dependente as d
on				f.idMatricula = d.idMatricula
order by		f.NomeFuncionario;

-- CROSS JOIN
-- operador de junção de produto cartesiano

select * from Depto;
select * from Projeto;

select
			d.NomeDepartamento,
			p.NomeProjeto,
			p.DataInicio,
			p.DataTermino
from	Depto  d cross join Projeto  p;
