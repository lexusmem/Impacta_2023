-- Uau�rio A
USE SISDEP;
-- Atualiza��o na tabela funcion�rios
BEGIN TRAN TR01;
	UPDATE FUNCIONARIO
	SET Salario += 100
	WHERE Salario <= 1500;
-- Usu�rio A ainda n�o confirmou a transa��o
COMMIT;
ROLLBACK;
-- Ir at� a janela Usu�rio B e tentar selecionar dados da tabela funcionario

-- Customizando n�vel de bloqueio
-- (N�vel de Linha) Default
BEGIN TRAN TR02;
	UPDATE FUNCIONARIO WITH(ROWLOCK)
	SET Salario += 100
	WHERE idMatricula IN(1000,1025,1040);
-- Usu�rio A ainda n�o confirmou a transa��o
COMMIT;
-- Ir at� a janela usu�rio B e executar o select with readpast (97 linhas)
-- Confirmar transa��o
-- (N�vel de Tabela)
BEGIN TRAN TR03;
	UPDATE FUNCIONARIO WITH(TABLOCK)
	SET Salario += 100
	WHERE idMatricula IN(1000,1025,1040);
-- Ir at� a janela usu�rio B e executar o select ReadPast e NoLock
-- Confirmar transa��o
COMMIT;
-- Configurando TimeOut (nesta Se��o)
-- Unidade de Tempo (Milisegundos)
DBCC USEROPTIONS;
SET LOCK_TIMEOUT 5000; -- 5 segundos

-- Executar novamente a transa��o TR03
-- Ir at� a janela usu�rio B e configurar timeout

-- visualizando bloqueios Pelo nome do objeto
SELECT * FROM sys.dm_tran_locks
WHERE resource_associated_entity_id = OBJECT_ID('Funcionario')

-- visualizando bloqueios por transa��o
select * from sys.dm_tran_locks
where request_owner_type = 'transaction';

-- Executar a transa��o TR02 (Usu�rio A) e TR04 (Usu�rio B)
COMMIT

-- Executar a transa��o TR01 e TR03

-- Visualizando transa��es ativas nesta se��o
SELECT @@TRANCOUNT;
-- Visualizando Active Monitor
-- CTRL + ALT + A

-- Visualizando Report All Transactions
