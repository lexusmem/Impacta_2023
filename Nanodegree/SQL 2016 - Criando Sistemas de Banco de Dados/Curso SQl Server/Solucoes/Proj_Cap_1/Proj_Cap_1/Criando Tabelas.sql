USE Clientes;

CREATE TABLE tblClientes
(
	idCliente								int	not null	identity
	constraint							PK_tblClientes_idCliente
	primary key						(idCliente),

	nomeCliente						nvarchar(50)	not null,

	dataCadastroCliente			datetime	default	getdate()
	constraint							CK_tblClientes_dataCadastroCliente
	check									(dataCadastroCliente <= getdate()),
	
	dataNascimentoCliente	datetime
	constraint							CK_tblCliente_dataNascimentoCliente
	check									(dataNascimentoCliente < getdate()),

	enderecoCliente				nvarchar(50)	not null,
	bairro									nvarchar(40)	not null,
	cepCliente							nchar(7),
	listaCompraCliente			int,
);
EXEC sp_help tblClientes;

-- Incluindo novas tabelas em Clientes
ALTER TABLE	tblClientes
ADD				codFoneCliente	int
constraint		FK_tblClientes_tblFone
foreign key		(codFoneCliente)
references		tblFone(codFone);

ALTER TABLE	tblClientes
ADD				codPrifissaoCliente	int
constraint		FK_tblClientes_tblProfissao
foreign key		(codPrifissaoCliente)
references		tblProfissao(codProfissao);

ALTER TABLE	tblClientes
ADD				codCidade	int	not null
constraint		FK_tblClientes_tblCidade
foreign key		(codCidade)
references		tblCidade(codCidade);

ALTER TABLE	tblClientes
ADD				codEstado	int	not null
constraint		FK_tblClientes_tblEstado
foreign key		(codEstado)
references		tblEstado(codEstado);

exec sp_help tblClientes;
-----------------------------------------------------------------------
CREATE TABLE tblFone
(
	codFone			int	not null	identity
	constraint		PK_tblFone_codFone
	primary key	(codFone),

	idCliente		int	not null
	constraint	FK_tblFone_tblClientes
	foreign key	(idCliente)
	references	tblClientes(idCliente),

	fone				nchar(9)
	constraint	UQ_tblFone_fone
	unique		(fone),

	tipoFone		varchar(15) not null
	constraint	CK_tblFone_tipoFone
	check			(tipoFone in ('Celular', 'Residencia', 'Comercial')),
);
EXEC sp_help tblFone;
-----------------------------------------------------------------------
CREATE TABLE tblProfissao
(
	codProfissao		int	not null	identity
	constraint			PK_tblProfissao_codProfissao
	primary key		(codProfissao),
	
	profissao			nvarchar(40)
	constraint			UQ_tblProfissao_profissao
	unique				(profissao),
);

-- Excluir Constraint para ajuste da tabela
	ALTER TABLE tblProfissao
	DROP CONSTRAINT UQ_tblProfissao_profissao;

-- Ajustando coluna para inclusão do not null
	ALTER TABLE			tblProfissao
	ALTER COLUMN	profissao nvarchar(40)	not null;

-- Incluindo constraint unique na coluna profissão
	ALTER TABLE		tblProfissao
	add constraint	UQ_tblProfissao_profissao
	unique				(profissao);

exec sp_help tblProfissao;
---------------------------------------------------------------
CREATE TABLE tblEstado
(
	codEstado		int	not null	identity
	constraint		PK_tblEstado_codEstado
	primary key	(codEstado),

	estado			nchar(2)	not null
	constraint	UQ_tblEstado_estado
	unique		(estado),
);
exec sp_help tblEstado;
---------------------------------------------------------------
CREATE TABLE tblCidade
(
	codCidade		int not null identity
	constraint		PK_tblCidade_codCidade
	primary key	(codCidade),

	cidade			nvarchar(40)	not null
	constraint	UQ_tblCidade_cidade
	unique		(cidade),

	codEstado		int	not null
	constraint		FK_tblCidade_tblEstado
	foreign key		(codEstado)
	references		tblEstado(codEstado),
);
exec sp_help tblCidade;
