USE Concessionaria;

-- Criando a terceira tabela
CREATE TABLE tblEstoque
(
		idEstoque		int		identity
		Constraint		PK_tblEstoque_idEstoque
		Primary Key	(idEstoque),

		idModelo			int				not null
		Constraint			FK_tblEstoque_tblModelos
		Foreign Key		(idModelo)
		References			tblModelos(idModelo),

		dataEntrada		date				default getdate(),

		precoEstoque		money		not null
		Constraint			CK_tblEstoque_precoEstoque
		CHECK				(precoEstoque >= 10000 and precoEstoque <= 200000)
);

-- Incluindo nova coluna
ALTER TABLE tblEstoque
ADD placa nchar(8) not null;

-- Alterar coluna (tamanho do campo)
ALTER TABLE tblEstoque
ALTER COLUMN placa nchar(7) not null;

exec sp_help tblestoque;

-- Excluir Coluna
ALTER TABLE tblEstoque
DROP COLUMN placa;

exec sp_help tblestoque;

/*
Não é possível alterar ou excluir colunas que possuem constraints
Uma coluna PK/FK devemos excluir estas constrainsts primeiro
Exemplo:
ALTER TABLE NomeTable
DROP CONSTRAINT NomeConstraint;
*/