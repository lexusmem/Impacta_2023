use SysConVendas;

exec sp_tables;

select * from Dados;

-- valores exclusivos
select distinct Produto from Dados;

select AVG( preco) as media_preco from Dados;

select distinct Produto, AVG( preco) as media_preco
from Dados
group by Produto;

select distinct Cidade, AVG( Total) as media_preco
from Dados
group by Cidade
order by media_preco desc;

select cidade, AVG( Total) as media_preco
from Dados
group by Cidade
order by media_preco desc;

select * from Dados;

-- convert(tamanho da varchar(string) 100
--dateadd(adicionar 2 meses a data
select convert(varchar(100), dateadd(MONTH, 2, '2019-12-31'), 103);

-- função DATEPART é utilizada para extrair o dia da semana do valor da data '1988-12-09'
select DATEPART(WEEKDAY, '1988-12-09');
