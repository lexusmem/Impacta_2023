Use SisDep;

exec sp_tables;

exec sp_columns funcionario;

select
			idMatricula, NomeFuncionario, Admissao, Salario
from	Funcionario
where	Salario between 1500 and 3000;

select
			idMatricula, NomeFuncionario, Admissao, Salario
from	Funcionario
where	Admissao between '2005/1/1' and '2005/31/12';
-- YYYY/DD/MM

select
			idMatricula, NomeFuncionario, Admissao, Salario
from	Funcionario
where	Admissao NOT between '2005/1/1' and '2005/31/12'
ORDER BY Admissao desc;
-------------------------------------------------------
select
			idDepartamento, idMatricula, NomeFuncionario, Admissao, Salario
from	Funcionario
where	idDepartamento in(1,3,5,6,10)
order by	idDepartamento asc, Admissao desc;

select
			idDepartamento, idMatricula, NomeFuncionario, Admissao, Salario
from	Funcionario
where	idDepartamento not in(1,7)
order by	1 asc, 4 asc;
-------------------------------------------------------
-- LIKE - útil para realziar pesquisas por parte de conteúdos.
/*
	Caracteres Coringa
	% = 1 ou mais caracteres desconhecidos
	_ = somente 1 caractere desconhecido
*/

select
			idMatricula, NomeFuncionario, Admissao, Salario
from	Funcionario
where NomeFuncionario like 'a%'
order by NomeFuncionario asc;

select
			idMatricula, NomeFuncionario, Admissao, Salario
from	Funcionario
where NomeFuncionario like 'A_A%'
order by NomeFuncionario asc;

select
			idMatricula, NomeFuncionario, Admissao, Salario
from	Funcionario
where NomeFuncionario like '%oliveira'
order by NomeFuncionario asc;

select
			idMatricula, NomeFuncionario, Admissao, Salario
from	Funcionario
where NomeFuncionario like '%souza%'
order by NomeFuncionario asc;