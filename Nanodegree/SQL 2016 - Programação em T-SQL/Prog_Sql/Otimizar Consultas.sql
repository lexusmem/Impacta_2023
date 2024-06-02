-- otimizando consultas
-- plano de execu��o

-- dicas
-- bancosnormalizados
-- constraint pk
-- quantidade de colunas
-- evitar campos binarios
-- evitar tabeals temporarias
-- evitar trabalhar com cursores
-- where - procure que possuam indice
-- evite like-not
-- evite hints ao maximo
-- utilize indices
-- evite cosnulta ad hoc

-- conceito de �ndice
-- estruturas

-- clustered a coluna de indice � ondenada fisicamentena tabela

-- nonclustered a coluna de indicice � realizada na hora da consulta

use SysConVendas;

select * from dados;
exec sp_help dados;

-- visualizando �ndice
exec sp_helpindex dados;

-- configurando padr�o de entrada de datas
set dateformat DMY;

-- visualizando planoo de execu��o (CTRL + L)
select * from Dados
where DataPedido between '1/1/2007' and '30/6/2007'
order by DataPedido desc;

-- criar �ndice
create index ix_datapedido
on dados (datapedido);

create index ix_vendedor
on dados (vendedor);

create index ix_produto
on dados(produto);

-- criando �ndices compostos
create unique index uq_registro
on dados(pedido, datapedido, vendedor, cidade, produto);

-- excluir �ndice
drop index dados.ix_produto;

-- hints
-- for�ar o sql utilizar pesquisa no �ndice
select * from Dados
with(index = ix_produto)
where Produto = 'camisa';

select * from dados
with (index = uq_registro)
where vendedor = 'gisele' and produto = 'gravata';

-- maxdop
-- definir quantidade de processadores para executar a consulta
select * from dados
where mes = 'junho'
order by regiao, cidade
option(maxdop 2); -- 2 processadores