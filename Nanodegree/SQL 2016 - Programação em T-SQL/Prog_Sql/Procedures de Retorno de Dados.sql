/*
	Procedures: Procedimentos armazenados

	Um procedimento armazenado (Stored Procedure), � uma cole��o de instru��es
	que, uma vez armazenadas ou salvas, ficam dentro do servidor de forma pr�-compilada.

	Vantagens

		. Modularidade: 
		
			Procedimento divido em partes facilitando manuten��o de uma aplica��o

		� Diminui��o de I/O: 
		
			uma vez que � passado par�metros para o servidor, chamando o procedimento armazenado,
			as opera��es s�o executadas utilizando processamento do servidor 
			e no final deste, � retornado ou n�o os resultados de uma transa��o, 
			sendo assim, n�o h� um tr�fego imenso de dados pela rede

		� Rapidez na execu��o: 
		
			os stored procedures, ap�s salvos no servidor, ficam somente aguardando,
			j� em uma posi��o da mem�ria cache, serem chamados para executarem uma opera��o,
			ou seja, como est�o pr�-compilados, as a��es tamb�m j� est�o pr�-carregadas, 
			dependendo somente dos valores dos par�metros.
			Ap�s a primeira execu��o, elas se tornam ainda mais r�pidas (CACHE)

 
		. Encapsulamento:
			
			podemos ocultar complexidades dentro de um servidor, bastante somente aos
			usu�rios que ir�o executar o procedimento conhecer seus par�metros


		� Seguran�a de dados: 
		
			 podemos bloquear o c�digo de um procedimento (criptografado) com WITH ENCRYPTION
			 e ainda criar limita��es de dados aos usu�rios.

		. Leitura de Dados Din�micos

			atrav�s de par�metros fornecidos, o resultado da busca de informa��es no
			banco poder� se dar de forma din�mica

		Restri��es

		Dentro de procedures n�o podemos:

			> Utilizar comandos:
				. CREATE PROCEDURE
				. CREATE DEFAULT
				. CREATE RULE
				. CREATE TRIGGER
				. CREATE VIEW

			> Ter mais que 32 n�veis de aninhamento

*/

-- Banco SisDep
USE SisDep;

-- Procedure sem par�metros para retorno de dados
GO
CREATE PROCEDURE spr_DadosFuncionarios
AS
	SELECT
		F.idMatricula,F.NomeFuncionario,D.NomeDepartamento,
		C.NomeCargo,F.Admissao,F.Salario
	FROM Funcionario F
		INNER JOIN Depto D		ON F.idDepartamento = D.idDepartamento
		INNER JOIN Cargo C		ON F.idCargo = C.idCargo;
GO


-- Procedure com par�metros para retorno de dados
GO
create PROCEDURE spr_AdmissoesPorAno
@inicio int,@fim int
AS
	SELECT
		F.idMatricula,F.NomeFuncionario,D.NomeDepartamento,
		C.NomeCargo,F.Admissao,F.Salario
	FROM Funcionario F
		INNER JOIN Depto D		ON F.idDepartamento = D.idDepartamento
		INNER JOIN Cargo C		ON F.idCargo = C.idCargo
	WHERE YEAR(F.Admissao) BETWEEN @inicio AND @fim;
GO

-- Par�metros opcionais
CREATE PROCEDURE spr_ParteDoNome
@parteNome varchar(50) = '%'
AS
	SELECT
		F.idMatricula,F.NomeFuncionario,D.NomeDepartamento,
		C.NomeCargo,F.Admissao,F.Salario
	FROM Funcionario F
		INNER JOIN Depto D		ON F.idDepartamento = D.idDepartamento
		INNER JOIN Cargo C		ON F.idCargo = C.idCargo
	WHERE F.NomeFuncionario Like @parteNome;
GO

-- Executando procedures

EXECUTE spr_DadosFuncionarios;
EXEC spr_AdmissoesPorAno 2000,2005;
EXEC spr_ParteDoNome '%souza';
EXEC spr_ParteDoNome '%Silva%';
EXEC spr_ParteDoNome;

-- Executando procedures com par�metros expl�citos
EXEC spr_AdmissoesPorAno  
	@inicio = 2008,
	@fim = 2008;

-- Procedures com retorno
GO
CREATE PROCEDURE spr_PesquisaMatricula
@id int
AS
	IF NOT EXISTS(SELECT * FROM Funcionario WHERE idMatricula = @id)
		RETURN -1

	SELECT
		F.idMatricula,F.NomeFuncionario,D.NomeDepartamento,
		C.NomeCargo,F.Admissao,F.Salario
	FROM Funcionario F
		INNER JOIN Depto D		ON F.idDepartamento = D.idDepartamento
		INNER JOIN Cargo C		ON F.idCargo = C.idCargo
	WHERE F.idMatricula = @id;
go

EXEC spr_PesquisaMatricula 1025;

EXEC spr_PesquisaMatricula 5000; -- N�o conseguimos ver o retorno -1

-- Recuperando retorno
DECLARE @ret int;
EXEC @ret = spr_PesquisaMatricula 5000;
IF @ret < 0 PRINT 'Matr�cula Inexistente';

-- Alterando procedure
GO
ALTER PROCEDURE spr_ParteDoNome
@parteNome varchar(50) = '%'
WITH ENCRYPTION
AS
	SELECT
		F.idMatricula,F.NomeFuncionario,D.NomeDepartamento,
		C.NomeCargo,F.Admissao,F.Salario
	FROM Funcionario F
		INNER JOIN Depto D		ON F.idDepartamento = D.idDepartamento
		INNER JOIN Cargo C		ON F.idCargo = C.idCargo
	WHERE F.NomeFuncionario Like @parteNome;

-- Visualizando c�digo de uma procedure
EXEC sp_helptext spr_AdmissoesPorAno;

EXEC sp_helptext spr_ParteDoNome; -- Proc est� criptografada

-- Excluir Procedure
DROP PROCEDURE spr_AdmissoesPorAno;

