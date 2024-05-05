use AdventureWorksLT2022;
exec sp_help;
exec sp_tables;

select * from SalesLT.Product;

-- IN
select * from SalesLT.Product
where ProductID in (842,741,788);

-- LIKE
select * from SalesLT.Product
where Name like 'Mountain%';

-- NULL
select * from SalesLT.Product
where Name like 'Mountain%' and Weight is not null;

select * from SalesLT.Product
where Name like 'Mountain%' and Weight is null;

-- ORDER BY
select * from SalesLT.Product
where Name like 'Mountain%' and Weight is not null
ORDER BY ProductID asc;

select * from SalesLT.Product
where Name like 'Mountain%' and Weight is null
ORDER BY ProductCategoryID asc, ProductID asc;