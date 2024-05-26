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

-- funções de agregações
-- consolidar ou totaliza uma determinada informação

-- agrgação de dominio geral (tabela ou consulta) uma colunainteira
-- seletc sun(coluna) from tabela

use SisDep;

-- retornar o total geral de salários pagos
select sum(salario) 'Total de Salário' from Funcionario;

-- retornar a média de salários
select avg(salario) [Média de Salários] from Funcionario;

-- mais de uma agregação no mesmo comando select
select
max(salario) as 'Maior Salário',
min(salario) as 'Maior Salário',
COUNT(salario) as [N° de Funcionários],
count(idDepartamento) as [Nº de Departamentos]
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