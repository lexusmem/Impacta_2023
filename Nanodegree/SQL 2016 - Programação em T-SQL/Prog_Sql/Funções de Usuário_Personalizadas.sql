-- Criando Fun��es Escalares
GO
CREATE FUNCTION fn_Maior(@n1 int,@n2 int)
RETURNS int -- tipo de dado do retorno.
AS
	BEGIN
		DECLARE @retorno int
		IF @n1 > @n2
			SET @retorno = @n1
		ELSE
			if @n2 > @n1
				SET @retorno = @n2
			else
				set @retorno = 0;
		RETURN @retorno -- valor de retorno
	END
GO
-- Utilizando nossa fun��o
-- Ao chamar a fun��o � obrigat�rio especificar OWNER (dbo)
SELECT dbo.fn_Maior(7,7);
SELECT dbo.fn_Maior(7,5);
SELECT dbo.fn_Maior(1,3);

---------------------
GO
CREATE FUNCTION fn_AdicionarData2(@dt date,@op char(1),@n int)
RETURNS date
WITH ENCRYPTION
AS
	BEGIN
		DECLARE @ret date
		SET @ret = 
			CASE UPPER(@op)
				WHEN 'D'	THEN DATEADD(DAY,@n,@dt)
				WHEN 'S'	THEN DATEADD(WEEK,@n,@dt)
				WHEN 'M'	THEN DATEADD(MONTH,@n,@dt)
				WHEN 'T'	THEN DATEADD(QUARTER,@n,@dt)
				WHEN 'A'	THEN DATEADD(YEAR,@n,@dt)
			END
		RETURN @ret
	END
GO
-- Utilizando func��o
SELECT dbo.fn_AdicionarData(GETDATE(),'d',20);
SELECT dbo.fn_AdicionarData(GETDATE(),'s',6);
SELECT dbo.fn_AdicionarData(GETDATE(),'m',3);
SELECT dbo.fn_AdicionarData(GETDATE(),'t',2);
SELECT dbo.fn_AdicionarData(GETDATE(),'a',5);

-- Visualizar o c�digo da function (SEM OWNER)
EXEC sp_help fn_Maior;
exec sp_help fn_AdicionarData; -- n�o ser� poss�vel

SELECT
	T2.name,T1.text
FROM SYSCOMMENTS T1,SYSOBJECTS T2
WHERE T2.xtype = 'FN' AND T2.uid = 1 AND T1.id = T2.id;

-- excluir uma fun��o
drop function fn_Maior;

-- Fun��es Tabulares
-- Banco Seguro Ve�culo
USE SeguroVeiculo;
GO
CREATE FUNCTION fn_Apolices(@ano int)
RETURNS table
AS
RETURN
(SELECT        
Clientes.nomeSegurado, Clientes.cadastroSegurado, Seguradoras.nomeSeguradora, 
Apolices.valorApolice, Apolices.dataContratacao, Apolices.prazoMeses, Cidades.nomeCidade
FROM Apolices INNER JOIN
       Cidades ON Apolices.idCidade = Cidades.idCidade INNER JOIN
       Clientes ON Apolices.nContrato = Clientes.nContrato INNER JOIN
       Seguradoras ON Apolices.idSeguradora = Seguradoras.idSeguradora
	   WHERE YEAR(Clientes.cadastroSegurado) = @ano
);
GO

-- Testando a fun��o
SELECT * FROM dbo.fn_Apolices(2012);

go
create function f_media (@n1 int, @n2 int, @n3 int, @n4 int)
	returns float
as
begin
	declare @ret float
		set @ret = (@n1 + @n2 + @n3 + @n4)
	return (@ret)
end
go

select dbo.f_media(10,4,5,1);
----------------------------------------------
go
create function f_media2 (@n1 int, @n2 int, @n3 int, @n4 int)
	returns float
as
begin
	declare @ret float
		set @ret = (cast(@n1 as float) + cast(@n2 as float) + cast(@n3 as float) + cast(@n4 as float)) / 4
	return (@ret)
end
go

select dbo.f_media2 (11,4,5,1);