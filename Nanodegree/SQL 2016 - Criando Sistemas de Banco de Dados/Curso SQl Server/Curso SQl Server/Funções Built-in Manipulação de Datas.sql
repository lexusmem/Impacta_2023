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


-- funções built-in, funçõe so proprio sgbd.
-- funções para manipular data e hora

/*
	NomeFunção([Argumentos])
	GETDATE()
	DAY(Data Referência)
	MONTH(Data Referência)
	YEAR(Data Referência)
	EMONTH(Data Referência,Quantidade de meses a adicionar)
	DATEFROMPARTS(Ano,Mês,Dia)
	DATEDIFF(Parte Data,Data Inicial,Data Final)
	DATEADD(Parte Data,valor a ser adicionado,Data Referência)
	DATENAME(Data Referência,Parte Data)
	onde Parte Data poderá ser:
		> YEAR		YYYY
		> QUARTER	Q
		> MONTH		M
		> WEEK		WW
		> DAY		D
*/

select GETDATE();

use SisDep;

select
			NomeFuncionario,
			Admissao,
			day(Admissao) as dia,
			month(admissao) as mes,
			year(Admissao) as ano
from Funcionario;

-- retornar admitidos na 1° quinzena de qualquer do 2° semestre
-- dos seguintes anos(2000, 2003,2005,2008,2010)

select
			NomeFuncionario,
			Admissao,
			day(Admissao) as dia,
			month(admissao) as mes,
			year(Admissao) as ano
from Funcionario
where day (Admissao) <= 15 and MONTH(admissao) >= 7 and YEAR(admissao) in (2000, 2003,2005,2008,2010);

select EOMONTH(getdate(),0);
select EOMONTH(getdate(),1);

select DATEFROMPARTS(2024, 1,10);

/*
		> YEAR		YYYY
		> QUARTER	Q
		> MONTH		M
		> WEEK		WW
		> DAY		D
*/
select DATEDIFF(DAY, '1987/1/19', GETDATE()) as dias;
select DATEDIFF(MONTH, '1987/1/19', GETDATE()) as mes;
select DATEDIFF(YEAR, '1987/1/19', GETDATE()) as anos;
select DATEDIFF(QUARTER, '1987/1/19', GETDATE()) as trimestres;
select DATEDIFF(week, '1987/1/19', GETDATE()) as semanas;

select DATEADD(day, 65, getdate()) as dias;
select DATEADD(MONTH, 18, getdate()) as meses;
select DATEADD(YEAR, 5, getdate()) as anos;
select DATEADD(QUARTER, 6, getdate()) as trimestres;
select DATEADD(WEEK, 5, getdate()) as semanas;

set language 'BRAZILIAN'

select 
		NomeFuncionario,
		Admissao,
		DATENAME(weekday, admissao) as [dia da semana],
		DATENAME(month, admissao) as [dia da semana]
from Funcionario;