use SeguroVeiculo;

exec sp_help;
exec sp_columns apolices;

select * from apolices;

-- operadores relacionais
select * from apolices
where valorApolice >= 50000;

-- operadores lógicos
select * from apolices
where idSeguradora = 1 or idseguradora = 3
order by idSeguradora asc, valorApolice desc;

select * from apolices
where idSeguradora = 1 and valorApolice >= 50000
order by valorApolice desc;

select * from Apolices
where not idCidade = 5
order by idCidade asc;

-- operadores aritimeticos
select ncontrato, valorapolice, valorapolice * 1.1 as [reajuste anual]
from Apolices;

-- operadores compostos
BEGIN TRAN
	UPDATE Apolices
	SET valorApolice *= 1.1
COMMIT

SELECT * FROM Apolices;