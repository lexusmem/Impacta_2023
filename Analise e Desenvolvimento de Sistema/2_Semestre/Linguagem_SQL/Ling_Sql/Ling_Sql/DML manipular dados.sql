use IMPACTA;

exec sp_help ALUNO;
exec sp_tables;
exec sp_columns_100 aluno;

-- inserindo dados na tabela aluno
INSERT INTO aluno
(Nome, MeioNome, SobreNome, Cpf, Rg)
VALUES
('ALEX', 'SILVA DE', 'SOUSA', '22920975838','433291333'),
('LAURA', 'MELO DE', 'SOUSA', '22158758685','47523265844');

INSERT INTO aluno
(Nome, MeioNome, SobreNome, Cpf, Rg)
VALUES
('ALEX', 'SILVA DE', 'SOUSA', '22920975838','433291333');

SELECT * FROM aluno;

exec sp_help;
exec sp_help cliente;
exec sp_tables;
exec sp_tables cliente;
exec sp_columns_100 cliente; 

--inserindo dados na tabela cliente a partir dos dados de aluno
insert into cliente (Cpf, Rg)
select Cpf, Rg
from aluno;
	
select * from cliente;

select Nome from aluno
where nome like 'a%';

select * from aluno
where nome like 'a%';

select * from aluno;

-- deletar a tabela inteira aluno
delete from aluno;

-- trucate / deletar a tabela inteira aluno
truncate table aluno;

-- deletar com where
delete from aluno
where cpf = '22920975838';

delete from aluno
where Nome like 'a%';

-- alterar dados de uma tupla, alterar toda coluna nome
UPDATE aluno
set nome = 'teste';

-- alterar dados de uma tupla, alterar toda coluna nome
UPDATE aluno
set nome = 'LAURA'
where MeioNome = 'melo de';

UPDATE aluno
set nome = 'ALEX'
where MeioNome LIKE 'SILVA%';

select * from aluno;