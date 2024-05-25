use AdventureWorksLT2022;

-- JOIN
EXEC sp_tables Product;
exec sp_tables;
exec sp_help 'SalesLT.Product';
exec sp_help 'SalesLT.ProductCategory';
exec sp_help 'SalesLT.ProductModel';
exec sp_help 'SalesLT.Address';
exec sp_help 'SalesLT.Customer';

select *
from SalesLT.ProductModel as p inner join SalesLT.Customer c
on p.Name = c.FirstName
;

select * from SalesLT.ProductCategory;
select * from SalesLT.ProductModel;
select * from SalesLT.Customer;
select * from SalesLT.SalesOrderDetail;



select	SalesLT.Product.ProductID, SalesLT.Product.Name, SalesLT.Product.ProductCategoryID,
			SalesLT.ProductCategory.Name, SalesLT.ProductCategory.rowguid
from	SalesLT.Product join SalesLT.ProductCategory
on		SalesLT.Product.ProductCategoryID = SalesLT.ProductCategory.ProductCategoryID
order by SalesLT.Product.ProductCategoryID;

select * from SalesLT.ProductCategory;

select distinct ProductCategoryID from SalesLT.Product
order by ProductCategoryID;

select distinct SalesLT.Product.ProductCategoryID,
						SalesLT.ProductCategory.Name
from	SalesLT.Product join SalesLT.ProductCategory
on		SalesLT.Product.ProductCategoryID = SalesLT.ProductCategory.ProductCategoryID
order by ProductCategoryID;

-- Com apelido nas tabelas
select distinct p.ProductCategoryID,
						c.Name as 'Nome Categoria'
from	SalesLT.Product as p join SalesLT.ProductCategory as c
on		p.ProductCategoryID = c.ProductCategoryID
order by ProductCategoryID;

select distinct p.ProductCategoryID, p.Name,
						c.Name as 'Nome Categoria', c.ProductCategoryID as 'Numero da Categoria'
from	SalesLT.Product as p join SalesLT.ProductCategory as c
on		p.ProductCategoryID = c.ProductCategoryID
order by ProductCategoryID;

-- tipos de join
-- left e right join

select distinct p.ProductCategoryID, p.Name,
						c.Name as 'Nome Categoria', c.ProductCategoryID as 'Numero da Categoria'
from	SalesLT.Product as p left join SalesLT.ProductCategory as c
on		p.ProductCategoryID = c.ProductCategoryID
order by ProductCategoryID;

select distinct p.ProductCategoryID, p.Name,
						c.Name as 'Nome Categoria', c.ProductCategoryID as 'Numero da Categoria'
from	SalesLT.Product as p right join SalesLT.ProductCategory as c
on		p.ProductCategoryID = c.ProductCategoryID
order by ProductCategoryID;

-- full join
select distinct p.ProductCategoryID, p.Name,
						c.Name as 'Nome Categoria', c.ProductCategoryID as 'Numero da Categoria'
from	SalesLT.Product as p full join SalesLT.ProductCategory as c
on		p.ProductCategoryID = c.ProductCategoryID
order by ProductCategoryID;