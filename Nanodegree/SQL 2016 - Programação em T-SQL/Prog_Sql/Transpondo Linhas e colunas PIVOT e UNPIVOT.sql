-- transposição de linhas e colunas
-- operador pivot q permite transpor linhas em colunas
-- operador unpivot q permite transpor colunas em linhas
exec sp_databases;
use recursosadicionais;
exec sp_tables;
exec sp_help base1;
exec sp_help base2;
exec sp_help CotacoesPorDataMoeda;
exec sp_help Investidores;

-- Transformando Linhas Em Colunas (PIVOT)
select * from cotacoespordatamoeda;

select
		datacotacao, [USD] as Dólar, [EUR] as Euro, [LIB] as Libra
from
(
		SELECT datacotacao, codmoeda, valorcotacao
		from cotacoespordatamoeda
) as pv
pivot
(
		avg(valorcotacao)
		for codmoeda in ([USD], [EUR], [LIB])
) as p;


-- Transformando Colunas Em Linhas (UNPIVOT)
select * from investidores;

select
	banco, ano, Tipo, Valor
from investidores
unpivot(
		valor
		for tipo in(investimentos, despesas)
) as UPV
order by banco, ano, tipo;