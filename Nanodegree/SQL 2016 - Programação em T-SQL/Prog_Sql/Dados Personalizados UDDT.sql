exec sp_databases;

use RecursosAdicionais;

exec sp_tables;

exec sp_help base1;

-- tipo de dados de usuarios - UDDT
-- tipo de dados personalizados
-- user defines data type

-- tabela de sistemas - tipos de dados de sistema
select * from systypes;

-- view de sistemas
select * from sys.types;

-- criando banco uddt
create database uddt;
go
use uddt;

-- criando tipos de dados personalizados (uddt)
create type nomepessoa
from varchar(50) not null;

create type valormonetario
from decimal (10,2) not null;

create type opcaoSN
from char(1) not null;

create type dataregra
from date null;

-- visualizando somente os tipos personalizados
select * from systypes
where uid = 1;

-- criando regras de validação
go
create rule r_valormonetario as @valor >= 0;
go
create rule r_opcaosn as @sn in('s','n');
go
create rule r_dataregra as @data between '2014-1-1' and getdate();
go

-- visualizando regras criadas
select * from sysobjects where xtype = 'r';

-- associando as regras aos tipos criados

exec sp_bindrule 'r_valormonetario', 'valormonetario';
exec sp_bindrule 'r_opcaosn', 'opcaosn';
exec sp_bindrule 'r_dataregra', 'dataregra';

-- criando defaults
go
create default def_sn as 's';
go
create default def_data as getdate();
go

-- visualizando defaults
select * from sysobjects where xtype = 'd';

-- associando os defaults aos tipos criados
exec sp_bindefault 'def_sn', 'opcaosn';
exec sp_bindefault 'def_data', 'dataregra';

-- criando sequencial (identity personalizado)
create sequence seq_registro
	start with 1000
	increment by 10
	minvalue 10
	maxvalue 10000000
	cycle;

-- visualizando sequencias criadas
select * from sys.sequences;

-- utilizando uddt e sequencias criadas
create table clientes
(
id							int			primary key,
nomecliente		nomepessoa,
statusativo			opcaosn,
cadastrocliente	dataregra
);

create table fornecedores
(
id										int		primary key,
nomefornecedor			nomepessoa,
statusfornecedor			opcaosn,
cadastrofornecedor		dataregra					
);
-- inserindo dados
insert into clientes
(id, nomecliente,statusativo,cadastrocliente)
values
(next value for dbo.seq_registro, 'Alex Sousa', 's', GETDATE());

-- testando default
insert into clientes
(id, nomecliente)
values
(next value for dbo.seq_registro, 'Laura Sousa');

select * from clientes;

-- testando regras
insert into clientes
(id, nomecliente,statusativo,cadastrocliente)
values
(next value for dbo.seq_registro, 'Alex Sousa', 's', getdate()+30);

-- criando sinonimos
create synonym cli for dbo.clientes;

-- visualizando sinonimos criados
select * from sys.synonyms;

-- utilizando um sinonimo
select * from cli;
