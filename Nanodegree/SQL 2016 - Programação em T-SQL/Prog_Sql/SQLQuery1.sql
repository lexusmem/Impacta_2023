-- IMPORTAR DADOS DDE TEXTO

-- bulk insert
use DadosExternos;
exec sp_help;
select * from Produtos;

-- importando dados de um arquivo de texto para uma tabela
truncate table produtos;
bulk insert produtos
from 'c:\dados\produtos.txt'
with
(
fieldterminator = ';',
rowterminator = '\n',
codepage = 'ACP'
);
select * from Produtos;

CREATE TABLE Cursos(
	idCurso		int		primary key,
	nomeCurso	nvarchar(50),
	valorCurso	smallMoney
);
---------- nova importação
bulk insert cursos
from 'c:\dados\cursos.txt'
with
(
fieldterminator = ';',
rowterminator = '\n',
codepage = 'ACP'
);
select * from Cursos;