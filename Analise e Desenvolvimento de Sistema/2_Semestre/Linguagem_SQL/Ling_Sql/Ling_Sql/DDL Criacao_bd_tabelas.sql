--Criando BD cadastro de IMPACTA

/*
Criando banco de cadastro de clientes
*/
CREATE DATABASE IMPACTA;
GO
USE IMPACTA;

-- criando tabela aluno
CREATE TABLE aluno
(
Matricula		Int,
Nome				varchar(20),
MeioNome		varchar(20),
SobreNome	varchar(20)
);

-- excluindo coluna matriculo
ALTER TABLE			aluno
DROP COLUMN	Matriculo;

-- incluindo nova coluna na tabela aulno com identity
ALTER TABLE			aluno
ADD						Matricula	int	NOT NULL	IDENTITY (500,1);

-- incluindo primary key
ALTER TABLE				aluno
ADD CONSTRAINT	PK_ALUNO_Matricula
PRIMARY KEY			(Matricula);

-- incluindo novos campos e unicos
ALTER TABLE		ALUNO
ADD
Cpf						VARCHAR(11)	not null
CONSTRAINT		UQ_aluno_Cpf
UNIQUE				(Cpf),

Rg						VARCHAR(12)	not null
constraint			UQ_aluno_Rg
unique				(Rg);

-- EXCLUIR CONSTRAINT
USE IMPACTA;
GO
ALTER TABLE ALUNO
DROP CONSTRAINT UQ_aluno_Cpf, UQ_aluno_Rg;

-- ALTERANDO TIPO DE VALOR DE COLUNA E INCLUINDO COSNTRAINT
ALTER TABLE		ALUNO
ALTER COLUMN Cpf	VARCHAR(11)	not null;

ALTER TABLE		ALUNO
ADD CONSTRAINT UQ_aluno_Cpf
UNIQUE				(Cpf);


ALTER TABLE		ALUNO
ALTER COLUMN Rg VARCHAR(12)	not null;

ALTER TABLE		ALUNO
ADD constraint UQ_aluno_Rg unique (Rg);

exec sp_help aluno;

CREATE TABLE	Prova
(
idProva			int		not null		identity(1,1)
constraint		PK_Prova_idProva
primary key	(idProva),

Matricula		int		not null
constraint		FK_aluno_Prova
foreign key		(Matricula)
references		aluno(Matricula),

Nota				decimal(4,2)	not null
);

exec sp_help prova;

---------------------------------------------------------------------
CREATE TABLE Cliente
(
Cpf						int	not null
constraint			PK_Cliente_Cpf
primary key		(Cpf),
constraint			UQ_Cliente_Cpf
UNIQUE				(Cpf),

Rg						int	not null
constraint			UQ_Cliente_Rg
unique				(Rg)
);
alter table cliente
drop constraint	PK_Cliente_Cpf;

-- EXCLUIR CONSTRAINT
ALTER TABLE cliente
DROP CONSTRAINT UQ_cliente_Cpf, UQ_cliente_Rg;

-- ALTERANDO TIPO DE VALOR DE COLUNA E INCLUINDO COSNTRAINT
ALTER TABLE		cliente
ALTER COLUMN Cpf	VARCHAR(11)	not null;

ALTER TABLE		cliente
ADD CONSTRAINT UQ_cliente_Cpf
UNIQUE				(Cpf);


ALTER TABLE		cliente
ALTER COLUMN Rg VARCHAR(12)	not null;

ALTER TABLE		cliente
ADD constraint UQ_cliente_Rg unique (Rg);

-- inclusao coluna cliente
ALTER TABLE cliente
ADD
NumCliente		int		not null		identity(1,1)
constraint			PK_cliente_NumCliente
primary key		(NumCliente);

CREATE TABLE veiculo
(
Placa							char(8)			NOT NULL,
Marca							varchar(20)	NOT NULL,
NomeProprietario		varchar(60)
);

ALTER TABLE veiculo
drop column	idVeículo;

-- inclusao de coluna com identity valores auto-incrementados na cula veículos
ALTER TABLE			veiculo
ADD						idVeiculo		int	NOT NULL IDENTITY;

-- inclusão de primary key veiculo
ALTER TABLE		veiculo
ADD CONSTRAINT	PK_veiculo_idVeiculo
primary key				(idVeiculo);

CREATE TABLE	venda
(
DataVenda				date		not null
constraint				DF_venda_DataVenda
default					(getdate()),
constraint				PK_venda_DataVenda
primary key			(DataVenda),

Quantidade			smallint		not null
constraint				DF_venda_Quantidade
default					(1),

NumCliente			int		not null
constraint				FK_Cliente_Venda
foreign key				(NumCliente)
references				cliente(NumCliente)
);

use IMPACTA;
exec sp_help cliente;
exec sp_help venda;
exec sp_tables;

ALTER Table venda
add
Telefone	varchar(14)
constraint CK_Telefone
check 
(
Telefone LIKE '[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]'
OR
Telefone like '([0-9][0-9][0-9]) [0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]'
),

DataEntrada datetime,

Idade tinyint not null
constraint CK_Idadea
check (Idade between 18 and 90);

exec sp_help venda;