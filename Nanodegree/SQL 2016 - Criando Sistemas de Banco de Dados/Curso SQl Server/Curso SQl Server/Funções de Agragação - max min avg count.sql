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

-- fun��es de agrega��es
-- consolidar ou totaliza uma determinada informa��o

-- agrga��o de dominio geral (tabela ou consulta) uma colunainteira
-- seletc sun(coluna) from tabela

use SisDep;

-- retornar o total geral de sal�rios pagos
select sum(salario) 'Total de Sal�rio' from Funcionario;

-- retornar a m�dia de sal�rios
select avg(salario) [M�dia de Sal�rios] from Funcionario;

-- mais de uma agrega��o no mesmo comando select
select
max(salario) as 'Maior Sal�rio',
min(salario) as 'Maior Sal�rio',
COUNT(salario) as [N� de Funcion�rios],
count(idDepartamento) as [N� de Departamentos]
from Funcionario;

select * from funcionario;

use SysConVendas;

select * from Dados
where pedido = 22769;

update Dados
set Vendedor = NULL
where Pedido = 22769;

update Dados
set Vendedor = NULL
where Pedido = 22769;

-- count ignora a linha com valor NULL
select count(vendedor) as Contagem_Coluna from dados;
select count(pedido) as Contagem_Coluna from dados;
-- count * conta a linha independente se constar valor null
select count(*) as Contagem_Linha from Dados;