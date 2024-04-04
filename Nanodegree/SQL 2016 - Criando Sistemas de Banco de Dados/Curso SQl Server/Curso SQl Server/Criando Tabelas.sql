USE Concessionaria;

-- tabelas
-- int - campo que armazena números de tipo inteiro
-- primary key - este campo que será utilizado para busca
-- identity - será gerado números automaticamente
-- char - campo de complemento fixo
-- varchar - campo de complemento variavel
-- nchar - com textos unicode comprimento fixo
-- nvarchar - com texto unicode comprimento variavel
-- not null - campo obrigatorio (restrição)
-- unique - dados exclusivos, não pode ser mais repetido na coluna
CREATE TABLE tblMarcas
(
	idMarca			int				identity		primary key,
	nomeMarca	nchar(10)	not null		unique
	);

-- Visualizando estrutura de tabelas
EXEC sp_help tblMarcas

-- Criação da segunda tabela
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