use AdventureWorksLT2022;

EXEC sp_tables Product;
exec sp_tables;
exec sp_help 'SalesLT.Product';
exec sp_help 'SalesLT.ProductCategory';
exec sp_help 'SalesLT.ProductModel';

select * from SalesLT.ProductCategory;

select * from SalesLT.Product;

select * from SalesLT.ProductModel;

-- join entre 3 tabelas
-- produtos, categoria do produto e modelo do produto
select p.ProductID, p.Name,
			p.ProductCategoryID, c.Name as NameCategoria,
			p.ProductModelID, m.name as NameModelo
from	SalesLT.Product as p join SalesLT.ProductCategory as c
on		p.ProductCategoryID = c.ProductCategoryID
join		SalesLT.ProductModel as m
on		p.ProductModelID = m.ProductModelID
order by c.ProductCategoryID asc;

-- full join entre 3 tabelas
-- produtos, categoria do produto e modelo do produto
select p.ProductID, p.Name,
			c.ProductCategoryID, c.Name as NameCategoria,
			m.ProductModelID, m.name as NameModelo
from	SalesLT.Product as p full join SalesLT.ProductCategory as c
on		p.ProductCategoryID = c.ProductCategoryID
full join		SalesLT.ProductModel as m
on		p.ProductModelID = m.ProductModelID
order by c.ProductCategoryID asc;

-- categorias utilizadas na tabela produto
select  distinct p.ProductCategoryID, c.Name as NameCategoria
from	SalesLT.Product as p join SalesLT.ProductCategory as c
on		p.ProductCategoryID = c.ProductCategoryID
order by p.ProductCategoryID asc;

select  p.ProductCategoryID, c.Name as NameCategoria
from	SalesLT.Product as p join SalesLT.ProductCategory as c
on		p.ProductCategoryID = c.ProductCategoryID
where p.ProductCategoryID = 6
order by p.ProductCategoryID asc;

-- modelos utilizadas na tabela produto
select	distinct p.ProductModelID, m.name as NameModelo
from	SalesLT.Product as p join SalesLT.ProductModel as m
on		p.ProductModelID = m.ProductModelID
order by p.ProductModelID asc;

select	p.ProductModelID, m.name as NameModelo
from	SalesLT.Product as p join SalesLT.ProductModel as m
on		p.ProductModelID = m.ProductModelID
where m.ProductModelID = 5
order by p.ProductModelID asc;

-- todos os modelos na tabela modelos
select ProductModelID, Name from SalesLT.ProductModel
order by ProductModelID;

-- todas as categorias na tabela categorias
select ProductCategoryID, Name from SalesLT.ProductCategory
order by ProductCategoryID;


-- Fazendo group by
-- quantas categorias aparecem na tabela produtos
select	c.Name as NomeCategoria,
			p.ProductCategoryID as IDcategoria,
			count(p.ProductID) as qtdCategoria
from	SalesLT.Product as p join SalesLT.ProductCategory as c
on		p.ProductCategoryID = c.ProductCategoryID
group by c.Name, p.ProductCategoryID
order by p.ProductCategoryID;

-- quantas modelos aparecem na tabela produtos
select	m.Name as NomeModelo,
			p.ProductModelID as IDcategoria,
			count(p.ProductModelID) as qtdModelo
from	SalesLT.Product as p join SalesLT.ProductModel as m
on		p.ProductModelID = m.ProductModelID
group by m.Name, p.ProductModelID
order by p.ProductModelID;

select	CountryRegion,
			count(CountryRegion) as 'Qtd Region'
from SalesLT.Address
group by CountryRegion;

-- group by com having
select	CountryRegion,
			count(CountryRegion) as 'Qtd Region'
from SalesLT.Address
group by CountryRegion
having CountryRegion = 'Canada';

select CountryRegion, count(*)
from SalesLT.Address
group by CountryRegion;