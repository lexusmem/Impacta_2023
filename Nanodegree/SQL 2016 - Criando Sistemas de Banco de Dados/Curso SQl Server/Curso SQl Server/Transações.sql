use Concessionaria;

exec sp_tables;

-- transação implicita
/*
Erro ocorre quando é tentado realizar por exemplo a exclusão de banco
clicando com o botão e o proprio sgbd devido ao banco estar em uso recusa 
a tranasação de exclusão do banco.
*/

use SeguroVeiculo;

exec sp_tables;

select * from Apolices;

-- Iniciar uma transação
BEGIN TRANSACTION

-- Verificar se há laguma transação ativa.
SELECT @@TRANCOUNT;

update Apolices
set valorApolice = valorApolice + 1500;

-- Cancelar uma operação.
ROLLBACK TRANSACTION;

-- Iniciar uma transação
-- E executando um update
BEGIN TRAN;
		UPDATE Apolices
		SET valorApolice = valorApolice + 1500
		WHERE nContrato = 1000;

-- Confirmar Alteração
COMMIT TRAN;

USE SisDep;

EXEC sp_tables;

EXEC sp_columns Funcionario;

-- Iniciar uma transação
-- E executando um update
-- Utilizando Output para gerar dados de como era antes
-- e como ficou após a operação.
BEGIN TRAN
		UPDATE	Funcionario
		SET			Salario = Salario * 1.1
		OUTPUT	
						deleted.idMatricula,
						deleted.NomeFuncionario,
						deleted.Salario as [Salário Anterior],
						inserted.Salario as [Novo Salário]
		WHERE	Salario <= 3000;

-- Confirmar Alteração
COMMIT