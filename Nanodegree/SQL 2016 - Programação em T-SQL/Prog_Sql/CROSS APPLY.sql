-- CROSS APPLY
-- CORRELA��O ENTRE CONSULTAS

-- correlacionar duas ou mais consultas

Use SisDep;

select distinct
		f.NomeFuncionario, ca.[mais novo], ca.[mais velho]
from Funcionario as f inner join Dependente as d
on f.idMatricula = d.idMatricula

cross apply
(
		select
			max(nascimentodependente) as [mais novo],
			min(nascimentodependente) as [mais velho]
		from Dependente as d
		where d.idMatricula = f.idmatricula
) as ca;

--------------------
select distinct
		d.NomeDepartamento, ca.[primeira contrata��o], ca.[ultima contrata��o]
from Funcionario as f inner join Depto as d
on f.idDepartamento = d.idDepartamento
and d.NomeDepartamento in('Administraativo','financeiro' ,'rh' ,'TI')
cross apply
(
select
	max(Admissao) as [ultima contrata��o],
	min(Admissao) as [primeira contrata��o]
	from Funcionario as f
	where f.idDepartamento = d.idDepartamento
	and YEAR(Admissao) between 2000 and 2005
) as ca;
