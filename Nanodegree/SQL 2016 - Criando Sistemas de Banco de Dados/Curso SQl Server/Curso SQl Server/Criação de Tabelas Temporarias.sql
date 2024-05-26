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

-- tabelas temporarias
-- tabelas criadas no banco de sistema tempDB

-- escopo
-- pode ser local #NomeTabela (visibilidade na conexão ativa).
-- pode ser Global ##NomeTabela (visibilidade em todas as conexão ativa).

-- Tabela temporaria local (create table)
create table #Clientes
(
codigo				int,
nomecliente	varchar(50),
cadastro			date
);

select * from #Clientes;

insert into #Clientes
values
(1, 'Alex Sousa', '2024/5/26'),
(2, 'Laura Sousa', '2024/5/26');

------------------------------
use SysConVendas;

select * from Dados;

select	*
into		#Pesquisa1
from	Dados;

select * from #pesquisa1
where Pedido = 21794
order by pedido asc;

-- filtros tabelas temporarias
select * from #Pesquisa1
where Mes = 'agosto';

-- atualizações tabelas temporarias
update #Pesquisa1
set Vendedor = 'Alex Sousa'
where Pedido = 21794;

-------------------------------------
-- Tabela com escopo Global
select	*
into		##Pesquisa2
from	Dados
where Regiao = 'sudeste';

select * from ##Pesquisa2;