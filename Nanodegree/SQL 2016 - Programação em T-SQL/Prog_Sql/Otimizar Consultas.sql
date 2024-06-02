-- otimizando consultas
-- plano de execução

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

-- conceito de índice
-- estruturas

-- clustered a coluna de indice é ondenada fisicamentena tabela

-- nonclustered a coluna de indicice é realizada na hora da consulta

use SysConVendas;

select * from dados;
exec sp_help dados;

-- visualizando índice
exec sp_helpindex dados;

-- configurando padrão de entrada de datas
set dateformat DMY;

-- visualizando planoo de execução (CTRL + L)
select * from Dados
where DataPedido between '1/1/2007' and '30/6/2007'
order by DataPedido desc;

-- criar índice
create index ix_datapedido
on dados (datapedido);

create index ix_vendedor
on dados (vendedor);

create index ix_produto
on dados(produto);

-- criando índices compostos
create unique index uq_registro
on dados(pedido, datapedido, vendedor, cidade, produto);

-- excluir índice
drop index dados.ix_produto;

-- hints
-- forçar o sql utilizar pesquisa no índice
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