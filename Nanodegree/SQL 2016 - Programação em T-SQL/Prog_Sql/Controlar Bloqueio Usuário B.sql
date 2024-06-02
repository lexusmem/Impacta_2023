-- Usu�rio B
USE SISDEP;
-- Usu�rio B tenta ler dados da tabela funcion�rio
SELECT * FROM Funcionario;
-- For�ar a ler dados com atualiza��es n�o confirmadas
SELECT * FROM Funcionario WITH(NOLOCK);
-- Isto causa leitura suja (Dirty Read)
-- Ler somente dados que n�o est�o participando da transa��o (Leitura segura)
SELECT * FROM Funcionario WITH(READPAST);
-- Isto causa uma leitura de dados segura
-- Ira at� a janela usu�rio A e aplicar um Rollback

-- Configurando TimeOut
DBCC USEROPTIONS;
SET LOCK_TIMEOUT 5000;

-- Usu�rio B tenta ler dados da tabela funcion�rio
-- Retorno de erro ap�s 5 segundos
SELECT * FROM Funcionario;

-- Confirmar Transa��o TR03 em usu�rio A

-- Alterando o n�vel de isolamento
SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;

-- V� at� usu�rio A e execute transa��o TR03


-- Usu�rio B tenta ler dados
SELECT * FROM Funcionario;

-- Retornar para o n�vel de isolamento read committed
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;

-- Usu�rio B tenta ler dados novamente
SELECT * FROM Funcionario;

-- Confirmar transa��o TR03 em usu�rio A

-- Usu�rio B inicia nova transa��o
BEGIN TRAN TR04
	UPDATE Projeto WITH (ROWLOCK)
	SET [DataTermino] = GETDATE()
	WHERE idProjeto = 2

SELECT * FROM projeto

-- Na Janela Usu�rio A visualizar
-- Bloqueios por transa��o

-- Visualizando transa��es ativas nesta se��o
SELECT @@TRANCOUNT;