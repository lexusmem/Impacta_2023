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

-- INNER JOIN
-- Junção de dados de 2 ou mais tabelas
-- Junções internas não precisam obrigatoriamente de FK e PK

select
			NomeFuncionario, Admissao, Salario, Uf, Cidade
from	Funcionario inner join Localidade
on		Funcionario.idLocalidade = Localidade.idLocalidade;

select * from Funcionario;
select * from Localidade;

select
					NomeFuncionario, NomeDepartamento, Admissao, Salario, Uf, Cidade
from			Funcionario inner join Localidade
on				Funcionario.idLocalidade = Localidade.idLocalidade
inner join	Depto
on				Depto.idDepartamento = Funcionario.idDepartamento;

-- nomes qualificados
select
			Funcionario.NomeFuncionario,
			Dependente.NomeDependente,
			Dependente.NascimentoDependente
from	Funcionario inner join Dependente
on		Funcionario.idMatricula = Dependente.idMatricula;


-- rotulos ou alias
select
			f.NomeFuncionario,
			d.NomeDependente,
			d.NascimentoDependente
from	Funcionario as f inner join Dependente as d
on		f.idMatricula = d.idMatricula;


-- teste com varios join's
select
					f.NomeFuncionario,f.idLocalidade,
					l.Uf, l.Cidade,
					f.idDepartamento,
					d.NomeDepartamento,
					c.NomeCargo,
					t.NomeDependente
from			Funcionario as f left outer join Localidade as l
on				f.idLocalidade = l.idLocalidade
left outer join	Depto d
on				f.idDepartamento = d.idDepartamento
left outer join	Cargo c
on				f.idCargo = c.idCargo
left outer join	Dependente t
on				f.idMatricula = t.idMatricula;

