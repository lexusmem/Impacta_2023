use AdventureWorksLT2022;
use Concessionaria;
use Consorcio;
use SeguroVeiculo;
use SysConVendas;
use SisDep;
use Clientes;

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


-- fun��es built-in, fun��e so proprio sgbd.
-- fun��es para convers�o e formato

/*
	NomeFun��o([Argumentos])
	CAST(Valor Refer�ncia AS Tipo de Dado)
	CONVERT(Tipo de Dado,Valor Refer�ncia,Estilo)
	Onde Estilo ser� aplicado para datas e possui c�digos de 1 a 14 (Ano Sem S�culo)
	e 101 1 114 (Ano Com S�culo)
	FORMAT(Valor Refer�ncia,Formato,Cultura/Pa�s)
	EX:
	Format(Campo Monet�rio,'C','en-us')
	Format(Campo Monet�rio,'C','pt-br')
	Format(Campo Data,'d','pt-br')
	Format(Campo Data,'D','pt-br')
	Format(Campo Data,'dd - mm - yyyy','pt-br')
*/

use SisDep;
exec sp_help funcionario;

select
			NomeFuncionario,
			Admissao
from Funcionario;

select
			NomeFuncionario,
			Admissao,
			cast(admissao as date) as data
from Funcionario;

select 'media final: '+ cast(6.5 as varchar );

select
			NomeFuncionario,
			Admissao,
			convert(varchar, admissao, 1) as Codigo1,
			convert(varchar, admissao, 2) as Codigo3,
			convert(varchar, admissao, 3) as Codigo3,
			convert(varchar, admissao, 101) as Codigo101,
			convert(varchar, admissao, 102) as Codigo102,
			convert(varchar, admissao, 103) as Codigo103
from Funcionario;

select
		NomeFuncionario,
		FORMAT(Salario, 'C', 'en-us') as [Formato Dolar],
		FORMAT(Salario, 'C', 'pt-br') as [Formato Dolar],
		FORMAT(Admissao, 'd','pt-br') as 'Formato data 1',
		FORMAT(Admissao, 'D','pt-br') as 'Formato data 2',
		FORMAT(Admissao, 'dd-mm-yyyy','pt-br') as 'Formato data 3'
from Funcionario;
