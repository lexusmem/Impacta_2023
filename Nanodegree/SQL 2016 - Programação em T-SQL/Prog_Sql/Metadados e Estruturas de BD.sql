-- metadados são dados que compoem um banco

-- vizualizando metadados de uma view
select * from sys.objects;

-- tabelas de sistemas
select * from sysobjects;

-- tabelas de usuarios dentro de um banco
use SisDep;
select * from sysobjects where xtype = 'U';

-- chaves primarias
select * from sysobjects where xtype = 'PK';

-- constraints unique
select * from sysobjects where xtype = 'UQ';

-- retornar todas as colunas de todas as tabelas
select * from syscolumns;

-- retornar o nome de uma e suas colunas, bem como o tipo de dados
select
			t1.name, t2.name, t3.name
from sysobjects t1, syscolumns t2, systypes t3
where
			t1.id = t2.id and t3.xtype = t2.xtype and t1.xtype = 'u';

-- views de catálogo (do banco em uso)
select * from sys.tables;
select * from sys.columns;
select * from sys.types;
select * from sys.indexes;

-- procedures de catálogo (rotina / programa) 
exec sp_tables;
exec sp_helpdb sisdep;
exec sp_spaceused 'funcionario';

-- funções de catálogo
select DB_NAME();
select object_id('funcionario');