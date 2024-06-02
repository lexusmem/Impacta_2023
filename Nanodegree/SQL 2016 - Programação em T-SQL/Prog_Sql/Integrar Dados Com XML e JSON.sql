-- Gerando dados XML
USE SysConVendas;
SELECT * FROM Dados;

-- XML RAW sem tag raíz (somente linha de registro)
SELECT * FROM Dados
FOR XML RAW;

-- Criando uma tag principal
SELECT * FROM Dados
FOR XML RAW('Ítem_Pedido'),ROOT('Pedidos');

-- Dados com estrutura de elemento - mais utilizado
SELECT * FROM Dados
FOR XML RAW('Ítem_Pedido'),ROOT('Pedidos'),ELEMENTS;

-- Lidando com campos nulos
BEGIN TRAN TR01
	UPDATE Dados WITH(ROWLOCK)
	SET Vendedor = NULL
	WHERE Pedido = 21768
COMMIT;

-- Perceber que o campo vendedor não é exibido no pedido 21768
SELECT * FROM Dados
FOR XML RAW('Ítem_Pedido'),ROOT('Pedidos'),ELEMENTS;

-- Solução XSINIL
SELECT * FROM Dados
FOR XML RAW('Ítem_Pedido'),ROOT('Pedidos'),ELEMENTS XSINIL;

-- XML Tag AUTO
SELECT * FROM Dados
FOR XML AUTO,ROOT('Pedidos');

-- Método QUERY
-- Declarando uma variável XML 
	DECLARE @xml XML
	-- Carrega as informações da consulta para a variável XML, utilizando o FOR XML: 
	SET @xml =  
	( 
		SELECT Pedido,DataPedido,Regiao,produto,total 
		FROM Dados AS Pedido
		FOR XML AUTO, root('Pedidos'), ELEMENTS 
	 );

	SELECT @xml.query('Pedidos');

	-- Consultando um campo específico

	SELECT @xml.query('Pedidos/Pedido/DataPedido');

-- Consultando um registro específico
SELECT @xml.query('Pedidos/Pedido[Pedido=21768]');

-- Verificar Existência de um campo
SELECT @XML.exist('Pedidos/Pedido/Codigo');
  
SELECT @XML.exist('Pedidos/Pedido/Regiao');

-- Verificar Existência de um registro
SELECT @XML.exist('Pedidos/Pedido[Pedido=21768]');

--Habilitar opções avançadas 
EXEC sp_configure 'show advanced option',1
RECONFIGURE
--Habilitar a execução da procedure XP_CMDSHELL
EXEC sp_configure 'xp_cmdshell',1
RECONFIGURE

-- Exportar XML
/*
	BCP
	• Queryout: Nome do arquivo de saída;
	• S:Nome do servidor;
	• T: Acesso através de conta do Windows;
	• w: Utiliza UNICODE;
	• r: Terminador de linha;
	• t: Terminador de campo {TAB}.

*/


DECLARE @comando VARCHAR(4000);

SET @comando = 'BCP "SELECT * FROM SysConVendas.dbo.Dados AS TIPO FOR XML AUTO, ROOT(''RESULTADO''), ELEMENTS " '
	 + ' QUERYOUT "C:\DADOS\Dados_xmlALEX.xml" -SDESKTOP-32J24GI -t -w -T'

EXEC MASTER..XP_CMDSHELL  @comando;

-- Gerar Dados JSON
SELECT * FROM Dados
FOR JSON AUTO,ROOT('Pedidos');

-- Ler Dados JSON
USE master;
SELECT * FROM OPENJSON(
	'["São Paulo", "Rio de Janeiro", "Minas Gerais", "Paraná", "Santa Catarina"]'
	);

-- Exportar JSON

DECLARE @comandojs VARCHAR(4000)
SET @comandojs = 
	'BCP "SELECT * FROM SysConVendas.dbo.Dados AS TIPO FOR JSON AUTO" '
		+ ' QUERYOUT "C:\DADOS\arquivoJson.xml" -SDESKTOP-32J24GI -t -w -T'
EXEC MASTER..XP_CMDSHELL  @comandojs

