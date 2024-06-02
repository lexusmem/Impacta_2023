-- Tabelas CTE Common table expression

-- conjunto de dados temporarios utilizados para:
-- select, update, insert e deletade

use SysConVendas;

with cte(ano, mês, maiorpedido)
as
(
	select YEAR(datapedido) as ano, Mes as Mês,
	max(datapedido) as [maior pedido]
	from Dados
	group by YEAR(datapedido) , Mes
)
select * from cte where ano = 2006 and mês = 'Abril'
union
select * from cte where ano = 2006 and mês = 'junho';

-------------------------
use SisDep;

-- aplicar um reajuste de salarios em 10 para funcionarios
-- que ganham ate 2 mil e ser admitido antes de 2005
-- somente os 10 mais antigos

with reajuste
as
(
		select top 10 Salario, Admissao, NomeFuncionario
		from Funcionario
		where Salario <= 2000 and YEAR(admissao) < 2005
		order by Admissao asc
)
update reajuste
set salario *= 1.1
output
		deleted.NomeFuncionario,
		deleted.Salario as[salario anterior],
		inserted.Salario as [novo salario]