-- use master;
-- drop database Clientes;

-- para utilizar o comando union
-- todas os comando select deverão te  o mesmo numero de colunas
-- todas as colunas unidas deverão ter o mesmo tipo de dados

use clientes;

select * from clientes2015
union
select * from clientes2016;

select * from clientes2015
union
select * from clientes2016
order by Cliente asc;

select 'Cliente 2015' as Ano,* from clientes2015
union
select 'Cliente 2016',* from clientes2016
order by Cliente asc;

update clientes2015
set apolice = 30000
where codigo = 2790

update clientes2016
set apolice = 30000
where codigo = 2790

-- union
select 'Cliente 2015' as Ano,* from clientes2015
union
select 'Cliente 2016', * from clientes2016
order by Cliente asc;

-- union all
select 'Cliente 2015' as Ano,* from clientes2015
union all
select 'Cliente 2016', * from clientes2016
order by Cliente asc;

select * from clientes2015
where cidade = 'são paulo'
union
select * from clientes2016
where cidade = 'Rio de Janeiro'
order by cliente asc;