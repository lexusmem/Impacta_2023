/*
	Triggers - O que s�o?

	O termo trigger (gatilho em ingl�s) define uma estrutura do banco de dados que funciona,
	como o nome sugere, como uma fun��o que � disparada mediante alguma a��o.

	Tipos de Triggers

	. DDL (Defini��o de Dados)
	. DML (Manipula��o de Dados)
*/

-- Trigger N�vel Servidor
GO
CREATE TRIGGER tr_LogServer
ON ALL SERVER
FOR CREATE_DATABASE,DROP_DATABASE,ALTER_DATABASE,
DDL_DATABASE_LEVEL_EVENTS
AS
	DECLARE @dados XML;
	SET @dados = EVENTDATA();
	SELECT @dados;
GO

-- Testando Trigger
CREATE DATABASE TESTE;
DROP DATABASE TESTE;

-- Visualizando triggers criados
SELECT * FROM SYS.server_triggers;

-- Visualizando somente os eventos de trigger do servidor
SELECT * FROM sys.server_trigger_events;

-- Visualizando triggers do banco
SELECT * FROM SYS.triggers;

-- Visualizando somente os eventos de trigger no banco
SELECT * FROM SYS.trigger_events;

-- Visualizando todos os eventos poss�veis de triggers
SELECT * FROM SYS.trigger_event_types;

use SisDep;

-- Triggers DML
CREATE TABLE Historico_AlteraSalario
(
	idMatricula			int,
	salarioAnterior		money,
	salarioNovo			money,	
	dataAlteracao		date,
	usuario				nvarchar(50)
);

GO
CREATE TRIGGER tr_HistAlteraSalario
ON Funcionario
FOR UPDATE
AS
	DECLARE @id int,@salarioAnterior money,@salarioNovo money,
	@dataAlt date,@user nvarchar(50)

	SELECT @id = idMatricula FROM inserted;
	SELECT @salarioAnterior = Salario FROM deleted;
	SELECT @salarioNovo = Salario FROM inserted;
	IF @salarioAnterior <> @salarioNovo
		INSERT INTO Historico_AlteraSalario
		(idMatricula,salarioAnterior,salarioNovo,dataAlteracao,usuario)
		VALUES
		(@id,@salarioAnterior,@salarioNovo,GETDATE(),SUSER_NAME()) ;

-- Testando a Triggers
BEGIN TRAN;
	UPDATE Funcionario WITH (TABLOCK)
	SET Salario += 100
	WHERE idMatricula = 1025;
COMMIT;

BEGIN TRAN;
	UPDATE Funcionario WITH (TABLOCK)
	SET Salario += 100
	WHERE idMatricula = 1010;
COMMIT;

SELECT * FROM Historico_AlteraSalario;

SELECT * FROM Funcionario WHERE salario <= 1500

-- Alterando uma Trigger
GO
ALTER TRIGGER tr_HistAlteraSalario
ON Funcionario
WITH ENCRYPTION
FOR UPDATE
AS
	DECLARE @id int,@salarioAnterior money,@salarioNovo money,@dataAlt date,@user nvarchar(50)

	SELECT @id = idMatricula FROM inserted;
	SELECT @salarioAnterior = Salario FROM deleted;
	SELECT @salarioNovo = Salario FROM inserted;
	IF @salarioAnterior <> @salarioNovo
		INSERT INTO Historico_AlteraSalario
		(idMatricula,salarioAnterior,salarioNovo,dataAlteracao,usuario)
		VALUES
		(@id,@salarioAnterior,@salarioNovo,GETDATE(),SUSER_NAME()); 

-- Testando ap�s altera��o
EXEC sp_helptext tr_HistAlteraSalario;

-- Excluindo uma trigger
DROP TRIGGER tr_HistAlteraSalario;

-- Desabilitando uma trigger
DISABLE TRIGGER tr_HistAlteraSalario
ON Funcionario;

-- Habilitando uma trigger
ENABLE TRIGGER tr_HistAlteraSalario
ON Funcionario;