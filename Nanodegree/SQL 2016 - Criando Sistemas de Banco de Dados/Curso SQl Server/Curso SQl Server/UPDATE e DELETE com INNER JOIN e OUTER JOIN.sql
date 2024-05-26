use AdventureWorksLT2022;
use Concessionaria;
use Consorcio;
use SeguroVeiculo;
use SysConVendas;
use SisDep;

-- saber quais bancos de dados possuí
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

-- manipulando dados com junções
-- UPDATADE COM INNER JOIN
-- bônus de R$ 100 para todos funcionario que possuem dependentes.

begin tran
	update	Funcionario
	set			Salario = Salario + 100
	from		Funcionario as f inner join Dependente as d
	on			f.idMatricula = d.idMatricula;
-- desfazer operação ROLLBACK
--confirmar operação COMMIT
commit;

select
		f.NomeFuncionario, d.NomeDependente, f.Salario
from Funcionario as f join Dependente as d
on f.idMatricula = d.idMatricula;

-- UPDATADE COM OUTER JOIN	
-- reajuste de 10% no salario para quem não possui dependente

select
			f.NomeFuncionario, d.NomeDependente
from Funcionario as f left join Dependente as d
on f.idMatricula = d.idMatricula
where d.NomeDependente is null;

select
			f.NomeFuncionario, d.NomeDependente
from Funcionario as f left join Dependente as d
on f.idMatricula = d.idMatricula
where d.NomeDependente is not null;

begin tran
update Funcionario
set Salario = Salario * 1.1
from Funcionario as f left join Dependente as d
on f.idMatricula = d.idMatricula
WHERE d.NomeDependente is null;
ROLLBACK -- DESFAZER
commit -- aprovar alteração

-- DELETE COM INNER JOIN
-- desligamento de funcionario do depto sac com salarios acima de 1500

select
			f.NomeFuncionario, d.NomeDepartamento, f.Salario
from Funcionario f join Depto d
on f.idDepartamento = d.idDepartamento
where d.NomeDepartamento = 'sac';

select
			f.NomeFuncionario, d.NomeDepartamento, f.Salario
from Funcionario f join Depto d
on f.idDepartamento = d.idDepartamento
where d.NomeDepartamento = 'sac' and f.Salario > 1500;

begin tran
delete Funcionario
from Funcionario as f inner join Depto as d
on f.idDepartamento = d.idDepartamento
where d.NomeDepartamento = 'sac' and f.Salario > 1500;
commit;

-- DELETE COM OUTER JOIN
-- desligamento de funcionarios com salario superio a 4k
-- que não possui dependente

BEGIN TRAN
delete Funcionario
from Funcionario as f left join Dependente as d
on f.idMatricula = d.idMatricula
where d.NomeDependente is null and f.Salario > 4000;