use AdventureWorksLT2022;

exec sp_help;
exec sp_tables;

exec sp_help 'SalesLT.Address';

select * from SalesLT.Address
where AddressID = 9;

-- sub string
select SUBSTRING('Time Campeão', 6, 7);
select SUBSTRING(AddressLine1, 6, 7) from SalesLT.Address;

-- left (expression, length)
select left(AddressLine1, 4) from SalesLT.Address
where AddressID = 9;


-- right (expression, length)
select right(AddressLine1, 4) from SalesLT.Address
where AddressID = 9;

-- lower e upper
select AddressLine1, lower(AddressLine1) from SalesLT.Address;
select AddressLine1, upper(AddressLine1) from SalesLT.Address;

-- len - contagem de caracteres
select AddressLine1, len(AddressLine1) from SalesLT.Address;

-- replace
select AddressLine1, replace(AddressLine1, '.', '') from SalesLT.Address;

-- reverse
select AddressLine1, reverse(AddressLine1) from SalesLT.Address;

-- year
select ModifiedDate, YEAR(ModifiedDate) from SalesLT.Address;

-- month
select ModifiedDate, month(ModifiedDate) from SalesLT.Address;

-- day
select ModifiedDate, day(ModifiedDate) from SalesLT.Address;

-- getdate data atual do servidor
select ModifiedDate, GETDATE() from SalesLT.Address;

-- date diff
select ModifiedDate, DATEDIFF(YY, ModifiedDate, GETDATE()) from SalesLT.Address;