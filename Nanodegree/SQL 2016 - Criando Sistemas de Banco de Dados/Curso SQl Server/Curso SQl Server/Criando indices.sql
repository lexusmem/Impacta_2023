USE Concessionaria;

-- visualizando índices
exec sp_help tblEstoque;

-- Criando índices
CREATE NONCLUSTERED INDEX	IX_tblEstoque
ON														tblEstoque(dataEntrada DESC);

EXEC sp_helpindex tblEstoque;

-- Excluir um índice
DROP INDEX IX_tblEstoque
ON tblEstoque;
