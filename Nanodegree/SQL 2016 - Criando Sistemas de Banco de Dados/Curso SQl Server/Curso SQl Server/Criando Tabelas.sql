USE Concessionaria;

-- tabelas
-- int - campo que armazena n�meros de tipo inteiro
-- primary key - este campo que ser� utilizado para busca
-- identity - ser� gerado n�meros automaticamente
-- char - campo de complemento fixo
-- varchar - campo de complemento variavel
-- nchar - com textos unicode comprimento fixo
-- nvarchar - com texto unicode comprimento variavel
-- not null - campo obrigatorio (restri��o)
-- unique - dados exclusivos, n�o pode ser mais repetido na coluna
CREATE TABLE tblMarcas
(
	idMarca			int				identity		primary key,
	nomeMarca	nchar(10)	not null		unique
	);

-- Visualizando estrutura de tabelas
EXEC sp_help tblMarcas

-- Cria��o da segunda tabela
CREATE TABLE  tblModelos
(
	idModelo		int		identity
	Constraint		PK_tblModelos_idModelo
	Primary Key	(idModelo),

	-- FK
	idMarca			int		not null
	Constraint		FK_tbl_Modelos_tblMarcas_idMarca
	Foreign Key	(idMarca)
	References		tblMarcas(IdMarca),

	nomeModelo		nchar(30)		not null
	Constraint			UQ_tblModelos_nomeModelo
	Unique				(nomeModelo)
);

EXEC sp_help tblModelos;