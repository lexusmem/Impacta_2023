use IMPACTA

exec sp_help;

select * from aluno;
select * from Cliente;
select * from Prova;
select * from veiculo;
select * from venda;

exec sp_help cliente;

select distinct nome, matricula from aluno;

exec sp_databases;

use AdventureWorksLT2022;
exec sp_help;
exec sp_tables;

select * from SalesLT.Product;

select distinct color from SalesLT.Product;

select * from SalesLT.vGetAllCategories;

select * from SalesLT.Address;
select top 5 * from SalesLT.Address;
select top 5 percent * from SalesLT.Address;
select distinct city from SalesLT.Address;

select * 
from SalesLT.Address
where city = 'San Antonio';

select * 
from SalesLT.Address
where city = 'Dallas';

select * 
from SalesLT.Address
where city = 'Dallas' or city = 'San Antonio';

select distinct YEAR(ModifiedDate) as Ano from SalesLT.Address;

select *
from SalesLT.Address
where YEAR(modifieddate) = 2008;

select YEAR(modifieddate) as ano, *
from SalesLT.Address
where YEAR(modifieddate) between 2007 and 2008
order by ano desc;

-- CASE

select YEAR(modifieddate) as OrdemAno,
	case YEAR(modifieddate)
		when 2005 then 'ano 1'
		when 2006 then 'ano 2'
		else 'Ano 3 e posterior' end as TipoAno
from SalesLT.Address
order by OrdemAno asc;

select YEAR(modifieddate) as OrdemAno,
	case
		when YEAR(modifieddate) = 2005 then 'ano 1'
		when YEAR(modifieddate) = 2006 then 'ano 2'
		WHEN YEAR(modifieddate) > 2006 then 'Ano 3 e posterior' end as TipoAno
from SalesLT.Address
order by OrdemAno desc;

select YEAR(modifieddate) as OrdemAno,
	iif (YEAR(modifieddate) = 2005, 'ano 1', 'Anos posterior ao ano 1') as TipoAno
from SalesLT.Address;

select YEAR(modifieddate) as ano,
	iif (YEAR(modifieddate) = 2005, 'ano 1',
		iif(YEAR(modifieddate) = 2006, 'ano 2',
			iif(YEAR(modifieddate) = 2007, 'ano 3', 'posterior ao ano 3'))) as TipoAno
from SalesLT.Address
order by ano desc;