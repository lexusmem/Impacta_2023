USE SisDep;
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
----------------------------
use SysConVendas;

select * from dados;

exec sp_helpindex dados;

go
create view vw_pesquisacidade
with schemabinding
as
select
			Pedido, Vendedor, Regiao,Cidade,Produto,Total
from dbo.Dados;
go

select * from vw_pesquisacidade;

create unique clustered index uq_cidade
on vw_pesquisacidade(Pedido, Vendedor, Regiao,Cidade,Produto,Total);

select * from vw_pesquisacidade
where Cidade = 'São Paulo';

select * from Dados
where cidade = 'são paulo';
