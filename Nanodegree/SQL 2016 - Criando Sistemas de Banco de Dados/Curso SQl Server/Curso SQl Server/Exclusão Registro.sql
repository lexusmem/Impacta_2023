USE Consorcio;

exec sp_tables;

exec sp_columns carteiras;

-- Visualizando dados da tabela carteira.
SELECT * FROM Carteiras;

-- Exclu�ndo Registros
delete from	Carteiras
where				Cpf = 83699151180;

delete from	Carteiras
where				uf = 'go'


use SisDep;

exec sp_tables;

select * from Funcionario;

-- Exclus�o bem sucedida
delete from Funcionario
where idMatricula = 1001;

-- Exclus�o mal sucedida (ERRO)
-- erro pq existe uma FK dependente desta idmatricula 1000
delete from Funcionario
where idMatricula = 1000;

-- verificar dependentes dos funcionarios com id matricula 1000
SELECT * FROM Dependente
where idMatricula = 1000;