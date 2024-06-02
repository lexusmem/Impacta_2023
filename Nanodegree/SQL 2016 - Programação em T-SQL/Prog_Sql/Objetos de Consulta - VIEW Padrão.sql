/*
	View: Objeto no cat�logo de banco formado por linhas e colunas formando
	uma tabela virtual que � referenciado a tabelas f�sicas definidas dentro
	de uma query.

	Tipos de View:

	Standard		Dados reunidos provenientes de tabelas ou outras views

	Indexada		Estrutura de dados criada por �ndice clusterizados
					Boa op��o para otimizar leitura de informa��es

	Particionadas	Op��o que permite que uma tabela massiva de dados seja
					dividida em tabelas menores

	Vantagens
	---------

	. Reutiliza��o
	. Redu��o no custo de execu��o
	. Seguran�a
	. Compatibilidade
	. C�pia de dados
	. Encapsulamento de c�digos complexos
	. Extensibilidade a outros aplicativos

	Restri��es
	----------

	Uma view n�o poder�:

	. Gerar duas colunas com o mesmo nome
	. Utilizar ORDER BY (exceto se inclu�da na instru��o TOP)
	. Utilizar a cl�usula INTO
	. Fazer refer�ncia a uma tabela tempor�ria ou vari�veis
	. Utilizar vari�veis
	. Utilizar (*) para referenciar todos os campos
	  (exceto se especificarmos SCHEMABINDING
	. Ultrapassar a 1024 colunas
	. Ter mais de 32 n�veis de aninhamento
	. Ter mais de um CREATE VIEW dentro de um Batch (exceto especificado com instru��o GO)

*/

-- Banco Cons�rcio
USE Consorcio;
SELECT * FROM Carteiras;
GO
CREATE VIEW vw_Vendas_SP
AS
	SELECT UF,Cidade,CAST(DataContrato AS date) AS [Data Contrato],
	CAST(ValorAprovado + Entrada AS decimal(10,2)) AS Total
	FROM Carteiras;
GO
-- Visualizando dados de uma view
SELECT * FROM vw_Vendas_SP;

-- Alterando uma view
GO
ALTER VIEW vw_Vendas_SP
AS
	SELECT UF,Cidade,CAST(DataContrato AS date) AS [Data Contrato],
	CAST(ValorAprovado + Entrada AS decimal(10,2)) AS Total
	FROM Carteiras
	WHERE Uf = 'SP';
GO

SELECT * FROM vw_Vendas_SP;

-- Visualizando o c�digo de uma view (CTRL + T = Sa�da de Texto tem melhor exibi��o)
-- Via procedure
EXEC sp_helptext vw_Vendas_SP;

-- View de Cat�logo
SELECT * FROM syscomments;
SELECT text FROM syscomments;

SELECT * FROM SYS.views;

SELECT * FROM Sys.sql_dependencies
where object_id = 773577794

-- Encriptografando a view
go
ALTER VIEW vw_Vendas_SP
with encryption
AS
	SELECT UF,Cidade,CAST(DataContrato AS date) AS [Data Contrato],
	CAST(ValorAprovado + Entrada AS decimal(10,2)) AS Total
	FROM Carteiras
	WHERE Uf = 'SP';
go

exec sp_helptext vw_Vendas_SP;

-- Banco Sisdep
USE SisDep;
GO
CREATE VIEW vw_DadosFuncionarios
WITH ENCRYPTION
AS
	SELECT
		F.idMatricula,F.NomeFuncionario,D.NomeDepartamento,
		C.NomeCargo,F.Admissao,F.Salario
	FROM Funcionario AS F 
		INNER JOIN Depto AS D		ON F.idDepartamento = D.idDepartamento
		INNER JOIN Cargo AS C		ON F.idCargo = C.idCargo;

GO
-- Tentativa de visualizar o c�digo da view
EXEC sp_helptext vw_DadosFuncionarios;

SELECT * FROM syscomments;

-- Bloqueio de Estrutura
GO
CREATE VIEW vw_MaioresSalarios
WITH SCHEMABINDING
AS
	SELECT	TOP 5 idMatricula,NomeFuncionario,Admissao,Salario
	FROM dbo.Funcionario -- Owner obrigat�rio
	ORDER BY Salario DESC;
GO

SELECT * FROM vw_MaioresSalarios;

-- Tentativa de alterar a estrutura da tabela funcion�rio
exec sp_help Funcionario;

-- Alterar tamanho do campo CPF (Vai funcionar, pois Cpf n�o participa da View)
ALTER TABLE Funcionario
ALTER COLUMN Cpf nvarchar(11);

-- Alterar tamanho do campo NomeFuncionario (Vai dar erro, pois este campo pertence a View)
ALTER TABLE Funcionario
ALTER COLUMN NomeFuncionario int;

-- CHECK OPTION (Restri��o de Entrada de Dados)
GO
CREATE VIEW vw_NovaLocalidadeSP
AS
	SELECT idLocalidade,Uf,Cidade FROM Localidade
	WHERE Uf = 'SP'
WITH CHECK OPTION;
GO 

-- Testando
-- Vai dar erro

INSERT INTO vw_NovaLocalidadeSP
(idLocalidade,Uf,Cidade)
VALUES
(12,'RJ','Parati');
--Vai Funcionar
INSERT INTO vw_NovaLocalidadeSP
(idLocalidade,Uf,Cidade)
VALUES
(12,'SP','Ribeir�o Preto');

-- Excluir uma View
DROP VIEW vw_NovaLocalidadeSP;

GO
ALTER VIEW vw_Enderecos
AS
	SELECT
		'Funcion�rio' AS [Tipo de Contato],
		NomeFuncionario AS [Nome do Contato],
		Endereco	
	FROM Funcionario
	UNION
	SELECT
		'Dependente',
		NomeDependente,
		''
	FROM Dependente
	ORDER BY 2
GO
SELECT * FROM vw_Enderecos;

-- VIEW INDEXADA (Obter Melhor Performance)
GO
CREATE VIEW vw_ConsultaSimples
WITH SCHEMABINDING
AS
	SELECT
		idMatricula,NomeFuncionario,Admissao,Salario
	FROM dbo.Funcionario;
GO
CREATE UNIQUE CLUSTERED INDEX IX_ConsultaSimples
ON dbo.vw_ConsultaSimples(NomeFuncionario,Admissao);

SELECT * FROM vw_ConsultaSimples
WHERE NomeFuncionario LIKE 'C%';

