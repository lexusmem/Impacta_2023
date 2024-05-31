use AdventureWorksLT2022;
use Concessionaria;
use Consorcio;
use SeguroVeiculo;
use SysConVendas;
use SisDep;
use Clientes;
use Escola;

-- saber quais bancos de dados possuí
exec sp_databases;

-- saber quais as tabelas de um banco de dados
exec sp_tables;

-- saber quais as colunas de uma tabela
exec sp_help alunos;

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

-- MANIPULAR COLUNAS DO TIPO IDENTITY

CREATE DATABASE Escola
GO
USE Escola;

-- Criar tabela instrutores com campo identidade iniciando em 1 e ---- incrementando 1
CREATE TABLE Instrutores
( codInstrutor		INT IDENTITY,
  nomeInstrutor			VARCHAR(30),
  CONSTRAINT PK_Intrutor PRIMARY KEY (codInstrutor) )
-- Criar tabela alunos com campo identidade iniciando em 10 e 
-- incrementando 2
CREATE TABLE Alunos
( codAluno		INT IDENTITY(10,2),
  nomeAluno			VARCHAR(30),
  CONSTRAINT PK_Aluno PRIMARY KEY (codAluno) );

  -- renomear uma coluna em uma tabela
  sp_rename @objname='instrutor.codInstrutir', @newname = 'codInstrutor';

  -- renomear uma tabela
  sp_rename instrutor, Instrutores;
  sp_rename Aluno, Alunos;

  insert into Instrutores
  (nomeInstrutor)
  values
  ('MAGNO'),('AGNALDO'),('ROBERTO'), ('RENATA');

  select * from Instrutores;

  -- excluir o instrutor id 3
  delete from Instrutores where codInstrutor = 3;

  -- reutilizando o id 3
  set identity_insert instrutores on;

  insert into Instrutores
  (codInstrutor, nomeInstrutor)
  values
  (3, 'Márcio');

  -- desativando o modo de insert em colunas identity
  set identity_insert instrutores off;

  -- listar a coluna identity de uma tabela e seus valores
  select IDENTITYcol from instrutores;

  -- retornando o valor inicial
  select ident_seed('alunos');
  -- qual o valor de incremento
  select ident_incr('alunos');

  -- retornando o ultimo identity gerado no escopo da conexão de qq tabela
  select @@identity;

-- retornando o ultimo identity gerado no escopo da conexão de qq tabela
-- que tenha sido gerado através de uma procedure ou trigger
select scope_identity();

-- retornar o valor original mais atual de uma coluna odentity de uma tabela
select ident_current('instrutores');

-- zerar o contador do identity(trucate)
delete from instrutores;

insert into instrutores
values ('Alex');

select * from instrutores;

-- somente deletando os dados com truncate ele reindexa todos os dados para zerar os dados
truncate table instrutores;

-- inicio o novo registro do 1
insert into instrutores
(nomeInstrutor)
values ('Alex');

-- zerar o contador do identity (DBCC CHECKIDENT) mas pode reniciar com valor desejado
dbcc checkident('Instrutores', reseed, 5);

-- inicio o novo registro do 5
insert into instrutores
(nomeInstrutor)
values ('Alex');

