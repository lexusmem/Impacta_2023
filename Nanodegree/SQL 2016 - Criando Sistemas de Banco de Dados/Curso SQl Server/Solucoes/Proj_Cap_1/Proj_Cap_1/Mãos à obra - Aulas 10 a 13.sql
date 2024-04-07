--Criando BD cadastro de Pedidos Venda
/*
Criando banco de cadastro de Pedidos Venda
*/
CREATE DATABASE Pedidos_Venda;

USE Pedidos_Venda;

-- Criando Tabelas
CREATE TABLE tblTb_Produto
(
codigo_produto						int	identity
constraint								PK_tblTb_Produto_codigo_produto
primary key							(codigo_produto),

nome_do_produto				nvarchar(30),

codigo_unidade_medida		int,

qtd_estoque							numeric,

qtd_minima							numeric,

preco_custo							decimal (10,2),

preco_venda							decimal (10,2),

carac_tecnica							nvarchar(max),

fotografia								image
);

-- verificar dados do banco pedido venda
exec sp_help;

-- verificar tabelas do banco pedido de venda
exec sp_tables;

-- verificar quais colunas da tabela tb produto
exec sp_columns tbltb_produto;

-- verificar dados da tabela tb produto
exec sp_help tblTb_Produto;

-- criando tabela tb unidade
CREATE TABLE tblTb_Unidade
(
codigo_unidade	int not null identity
constraint			PK_tblTb_Unidade_codigo_unidade
primary key		(codigo_unidade),

nome_unidade nvarchar(30)
);

-- Excluindo tabela
DROP TABLE tblTb_Unidade;

-- adicionando novas tabelas
ALTER TABLE	tblTb_Unidade
ADD				pecas				int,
						metros			decimal(10,2),
						quilogramas	decimal(10,2),
						duzias				int,
						pacote				int,
						caixa				int;

exec sp_columns tblTb_unidade;

-- excluindo colunas
ALTER TABLE			tblTb_Unidade
DROP COLUMN	pecas, metros, quilogramas, duzias, pacote, caixa;

-- incluindo dados na tabela tb unidade
INSERT INTO tblTb_Unidade
(nome_unidade)
values
('PECAS'),
('METROS'),
('QUILOGRAMAS'),
('DUZIA'),
('PACOTE'),
('CAIXA');

SELECT * FROM tblTb_Unidade;

-- verificar dados da tabela tb unidade
exec sp_help tblTb_Unidade;

-- verificando colunas da tabela tb unidade
exec sp_columns tblTb_unidade;

-- criando nova tabela TB_CATEGORIA
CREATE TABLE tblTb_Categoria
(
codigo_categoria	int not null identity
constraint				PK_tblTb_Categoria_codigo_categoria
PRIMARY KEY		(codigo_categoria),

nome_categoria		nvarchar(30)
);

-- Excluindo tabela
DROP TABLE tblTb_Categoria;

INSERT INTO tblTb_Categoria
(nome_categoria)
VALUES
('MOUSE'),
('PEN-DRIVE'),
('MONITOR DE VIDEO'),
('TECLADO'),
('CPU'),
('CABO DE REDE');

select * from tblTb_Categoria;

exec sp_columns tblTb_Produto;

exec sp_help tbltb_produto;

-- incluindo FK na tabela produto ligando o tipo da unidade
ALTER TABLE	tblTb_Produto
ADD				codigo_tipo_unidade	int	not null
constraint		FK_tblTb_Produto_tblTb_Unidade
foreign key		(codigo_tipo_unidade)
references		tblTb_Unidade(codigo_unidade);

-- incluindo FK na tabela produto ligando o tipo da categoria
ALTER TABLE	tblTb_Produto
ADD				codigo_tipo_categoria	int	not null
constraint		FK_tblTb_Produto_tblTb_Categoria
foreign key		(codigo_tipo_categoria)
references		tblTb_Categoria(codigo_categoria);

exec sp_help tbltb_produto;

-- inserindo valores na tabela tbl produto
INSERT INTO tblTb_Produto
(nome_do_produto, codigo_tipo_unidade, codigo_tipo_categoria, qtd_estoque, qtd_minima, preco_custo, preco_venda)
OUTPUT
inserted.nome_do_produto as Produto,
Inserted.codigo_tipo_unidade as Unidade,
inserted.codigo_tipo_categoria as Categoria,
inserted.qtd_estoque as Quant,
inserted.qtd_minima as Qtd_Mínima,
inserted.preco_custo as Preço_Custo,
inserted.preco_venda as Preço_Venda
VALUES
('Caneta Azul', 1,1,150,40,0.50,0.75),
('Caneta Verde',1,1,50,40,0.50,0.75),
('Caneta Vermelha',1,1,80,35,0.50,0.75),
('Lápis',1,1,400,80,0.50,0.80),
('Régua',1,1,40,10,1.00,1.50);

SELECT * FROM tblTb_Produto;

ALTER TABLE tblTb_Produto
DROP COLUMN codigo_unidade_medida;

exec sp_columns tblTb_Produto;