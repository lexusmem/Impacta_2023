use SisDep;

exec sp_help;
-- Linguagem DQL - DATA QUERY LANGUAGE

-- Todas as colunas de uma tabela
select * from Funcionario;

-- somente algumas colunas da tabela funcionarios
exec sp_columns funcionario;
select idMatricula, NomeFuncionario, idDepartamento, Admissao, Salario
from Funcionario;

-- ordenando dados
ORDER BY -- ORDENAR DADOS
ASC -- CRESCENTE
DESC -- DECRECENTE
TOP -- RANK DE LISTAGEM DOS DADOS
WITH TIES -- MOSTRAR QUANDO EXISTIR EMPATES
PERCENT -- MOSTRAR O PERCENTUAL NO TOP

select idMatricula, NomeFuncionario, idDepartamento, Admissao, Salario
from Funcionario
order by NomeFuncionario asc;

select idMatricula, NomeFuncionario, idDepartamento, Admissao, Salario
from Funcionario
order by Salario desc;

-- Ordenação por mais de uma coluna
select idDepartamento, Salario, idMatricula, NomeFuncionario, Admissao
from Funcionario
order by iddepartamento asc, salario desc;

-- ordenar pela posição da coluna
select idDepartamento, Salario, idMatricula, NomeFuncionario, Admissao
from Funcionario
-- numero de acordo com as colunas que constam no select
order by 1 asc, 2 desc;

-- Exibir linhas de acordo com o solicitado RANK (TOP)
-- 20 primeiras linhas DA TABELA
select top (20) idDepartamento, Salario, idMatricula, NomeFuncionario, Admissao
from Funcionario;

-- 5% DOS REGISTROS
select top 5 PERCENT idDepartamento, Salario, idMatricula, NomeFuncionario, Admissao
from Funcionario;

-- 10 MAIORES SALÁRIOS
SELECT TOP 10 idDepartamento, Salario, idMatricula, NomeFuncionario, Admissao
from Funcionario
ORDER BY Salario DESC;

-- 10 MAIORES SALÁRIOS COM EMPATES
SELECT TOP 9 WITH TIES  idDepartamento, Salario, idMatricula, NomeFuncionario, Admissao
from Funcionario
ORDER BY Salario DESC;

-- RETORNAR 5 FUNCIONARIOS MAIS ANTIGOS
SELECT TOP 5 WITH TIES  idDepartamento, Salario, idMatricula, NomeFuncionario, Admissao
from Funcionario
ORDER BY Admissao ASC;
