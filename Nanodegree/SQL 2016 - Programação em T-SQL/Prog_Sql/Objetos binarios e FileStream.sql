-- objetos binarios
-- inclusão de arquivos binarios na tabelas
use RecursosAdicionais;

CREATE TABLE tblDocsClientes(
	idDoc			int		identity	primary key,
	descricao		varchar(50),
	documento		varbinary(Max)
);

-- Inserção de um arquivo binário - inserção manual
-- Single_Blob - Utilizado para codificação de leitura binária para arquivos
-- EX:
-- XML (Codificação de Esquema)
-- TXT (Codificação ASCII)
-- PDF (Codificação Binária)
insert into tblDocsClientes(descricao,documento)
select 'Planilha Excel', BulkColumn
from openrowset (bulk 'C:\Dados\Pessoa.xlsx', single_blob) as arq;

select * from tblDocsClientes;

-- atualização
update tblDocsClientes
set documento = (select * from openrowset
		(bulk 'C:\Dados\Pessoa.xls', single_blob) as arq);

select * from tblDocsClientes;


-- filetable
-- criação e inclusão de arquivos binarios

-- passo 1: habilitar filestream no sql server configuration manager

-- passo 2: habilitar filestream no servidor (permissão full)
EXEC sp_configure filestream_access_level, 2
RECONFIGURE;

-- passo 3: banco de dados em grupo de arquivos
CREATE DATABASE Banco_Filestream 
ON PRIMARY (
	NAME = FG_Filestream_PRIMARY, 
	FILENAME = 'C:\DADOS\Filestream_DATA.mdf'), 
	FILEGROUP FG_Filestream_FS 
	CONTAINS FILESTREAM (
		NAME = Filestream_ARQ, 
		FILENAME='C:\DADOS\Filestream_ARQ') 
	LOG ON (
		NAME = Filestream_log, 
		FILENAME = 'C:\DADOS\Filestream_log.ldf') 
		WITH FILESTREAM (NON_TRANSACTED_ACCESS = FULL, 
		DIRECTORY_NAME = N'Filestream_ARQ');

-- Passo 4: Verificar Options - FileStream - Directory Name (Propriedades do Banco)

-- Passo 5: Criar FileTable
USE Banco_Filestream;

CREATE TABLE FT_Documento AS FileTable    
	WITH 
	(
		FileTable_Directory = 'Filestream_ARQ',
		FileTable_Collate_Filename = database_default
	); 

exec sp_help ft_documento;
select * from ft_documento;
SELECT FileTableRootPath('ft_documento');

-- A próxima consulta apresenta as informações básicas dos arquivos e pastas:
SELECT Tab.Name as Nome,
IIF(Tab.is_directory=1,'Diretório','Arquivo') as Tipo,
Tab.file_type as Extensao,
Tab.cached_file_size/1024.0 as Tamanho_KB,
Tab.creation_time as Data_Criacao,
Tab.file_stream.GetFileNamespacePath(1,0) as Caminho,
ISNULL(Doc.file_stream.GetFileNamespacePath(1,0),'Root Directory')
[Parent Path]
FROM FT_Documento as Tab
LEFT JOIN FT_Documento as Doc
ON Tab.path_locator.GetAncestor(1) = Doc.path_locator;

