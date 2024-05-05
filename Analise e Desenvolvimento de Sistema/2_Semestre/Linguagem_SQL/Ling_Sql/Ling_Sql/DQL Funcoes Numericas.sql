use AdventureWorksLT2022;

exec sp_databases;

exec sp_help;

exec sp_tables;

exec sp_help 'SalesLT.SalesOrderDetail';

select * from SalesLT.SalesOrderDetail;

select top (1) SalesOrderDetailID ,UnitPrice, UnitPrice * -1 as 'valor_negativo' from SalesLT.SalesOrderDetail;

-- abs
select top (10) UnitPrice, abs(unitprice), UnitPrice * -1 as 'valor_negativo', abs(UnitPrice * -1) from SalesLT.SalesOrderDetail;

-- ceiling
select top (10) UnitPrice, ceiling(unitprice), UnitPrice * -1 as 'valor_negativo', ceiling(UnitPrice * -1) from SalesLT.SalesOrderDetail;

-- power
select power(2,2), power(3,4), power(5,2);

-- sqrt - raiz quadrada
select sqrt(4), sqrt(100);

-- rand - gera numero randomico de 0 a 1
select rand()

-- cast
select SalesOrderID, 'Venda n° ' + CAST(SalesOrderID as varchar) as Venda from SalesLT.SalesOrderDetail;

-- convert - converte tipo de data em outro tipo
select	GETDATE() as Dt1,
			cast(getdate() as varchar(30)) as Dtcast,
			convert(varchar(30), GETDATE(), 112) as DtConvert;