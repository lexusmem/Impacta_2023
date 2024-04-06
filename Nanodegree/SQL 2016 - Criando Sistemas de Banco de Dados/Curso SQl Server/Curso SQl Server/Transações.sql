use Concessionaria;

exec sp_tables;

-- transa��o implicita
/*
Erro ocorre quando � tentado realizar por exemplo a exclus�o de banco
clicando com o bot�o e o proprio sgbd devido ao banco estar em uso recusa 
a tranasa��o de exclus�o do banco.
*/

use SeguroVeiculo;

exec sp_tables;

select * from Apolices;

-- Iniciar uma transa��o
BEGIN TRANSACTION

-- Verificar se h� laguma transa��o ativa.
SELECT @@TRANCOUNT;

update Apolices
set valorApolice = valorApolice + 1500;

-- Cancelar uma opera��o.
ROLLBACK TRANSACTION;

-- Iniciar uma transa��o
-- E executando um update
BEGIN TRAN;
		UPDATE Apolices
		SET valorApolice = valorApolice + 1500
		WHERE nContrato = 1000;

-- Confirmar Altera��o
COMMIT TRAN;

USE SisDep;

EXEC sp_tables;

EXEC sp_columns Funcionario;

-- Iniciar uma transa��o
-- E executando um update
-- Utilizando Output para gerar dados de como era antes
-- e como ficou ap�s a opera��o.
BEGIN TRAN
		UPDATE	Funcionario
		SET			Salario = Salario * 1.1
		OUTPUT	
						deleted.idMatricula,
						deleted.NomeFuncionario,
						deleted.Salario as [Sal�rio Anterior],
						inserted.Salario as [Novo Sal�rio]
		WHERE	Salario <= 3000;

-- Confirmar Altera��o
COMMIT