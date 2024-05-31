use AdventureWorksLT2022;
use Concessionaria;
use Consorcio;
use SeguroVeiculo;
use SysConVendas;
use SisDep;
use Clientes;

-- saber quais bancos de dados possu�
exec sp_databases;

-- saber quais as tabelas de um banco de dados
exec sp_tables;

-- saber quais as colunas de uma tabela
exec sp_help;

-- retornar todos os dados da tabela Banco: AdventureWorksLT2022.SalesLT
select * from AdventureWorksLT2022.SalesLT.Product;
select * from AdventureWorksLT2022.SalesLT.ProductCategory;

-- retornar todos os dados da tabela Banco: SisDep
select * from Cargo;
select * from Dependente;
select * from Depto;
select * from Localidade;
select * from Projeto;
select * from Funcionario;

-- func��es adicionais
-- func��es de tomada de decis�es e deslocamentos
use SisDep;

-- iif - choose - fun��es de decis�es
select
NomeFuncionario, Admissao, Salario,
iif(salario <= 2000, 'Reajuste', '') as [analise salarial]
from Funcionario;

begin tran
		update funcionario
		set Salario *= iif(Salario <= 2000, 1.1, 1.05)
		output
			deleted.NomeFuncionario,
			format(deleted.Salario, 'c', 'pt-br') as [Sal�rio Anterior],
			format(inserted.Salario, '$ #,##0.00', 'en-us') as [Novo Sal�rio];
	commit

-- choose
select
		idMatricula, NomeFuncionario, Admissao,
		choose(datepart(WEEKDAY, Admissao), 'Dom','seg','ter','qua','qui','sex','sab')
from Funcionario;

-- lag- lead - fun��es de deslocamento

select
		idMatricula, NomeFuncionario, Admissao, Salario,
		lag(Admissao, 1) over(order by idmatricula) as [admiss�o da linha acima],
		lead(admissao, 1) over(order by idmatricula) as abaixo
from Funcionario;

select
		idMatricula, NomeFuncionario, Admissao,Salario,
		lag(Salario, 1) over(order by idmatricula) as [sal�rio da linha acima],
		lead(Salario, 1) over(order by idmatricula) as [sal�rio da linha abaixo],
		DATEDIFF(day, Admissao, LAG(admissao,1,0) over(order by idmatricula)),
		salario - lag(Salario, 1) over(order by idmatricula)
from Funcionario;

-- fetch-offset
-- 20 priemiras ligas a partir da 50 linha

select * from funcionario
order by idmatricula
offset 50 rows fetch next 20 rows only;

-- 10 linhas aleat�rias a partir da 30
select * from funcionario
order by newid()
offset 15 rows fetch next 10 rows only;
