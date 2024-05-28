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


-- fun��es built-in, fun��e so proprio sgbd.
-- fun��es para manipular textos

/*
	NomeFun��o([Argumentos])
	LEN(Texto Pesquisado)
	LEFT(Texto Pesquisado,N� de caracteres)
	RIGHT(Texto Pesquisado,N� de caracteres)
	REPLACE(Texto Pesquisado,Texto Localizado,Texto Substitui��o)
	CHARINDEX(Texto Pesquisado,Texto Localizado,Posi��o Inicial)
	SUBSTRING(Texto Pesquisado,Posi��o Inicial,N� de Caracteres)
	RTRIM(Texto Pesquisado)
	LTRIM(Texto Pesquisado)
	UPPER(Texto Pesquisado)
	LOWER(Texto Pesquisado)
	REPLICATE(Texto a Repetir,Quantidade de Vezes)
	REVERSE(Texto a ser Invertido)
	STRING_SPLIT(Texto a ser separado,Caractere delimitador)
*/

use sisdep;

select
		idmatricula,
		nomefuncionario,
		len(nomefuncionario) as [n� de caracteres],
		left (idmatricula, 2) as [esquerda],
		right(idmatricula, 1) as [direita],
		replace(idmatricula,'10', '20') as [substituir],
		charindex('silva',nomefuncionario,1) as [localizar],
		substring(nomefuncionario, 1, charindex(' ', nomefuncionario, 1)-1) as [Primeiro Nome]
from funcionario;

select RTRIM('impacta       ');

select ltrim('      impacta');

select rtrim(ltrim('      impacta           '));

select 
		UPPER(nomefuncionario) as Mai�sculas,
		LOWER(nomefuncionario) as Min�sculas
from Funcionario;

select REPLICATE('--', 10);

select REVERSE('Alex');

-- extra�r tipo extens�o do arquivo

select reverse(substring(reverse('teste de nomdfasdfe de arquivo.xlxs'),CHARINDEX('.',reverse('teste de nomdfasdfe de arquivo.xlxs'))+1,255));

-- concatenar

select
		idMatricula,
		NomeFuncionario,
		CONCAT(idmatricula, idDepartamento, idCargo) as [concatenar],
		idDepartamento,
		idCargo
from Funcionario;

