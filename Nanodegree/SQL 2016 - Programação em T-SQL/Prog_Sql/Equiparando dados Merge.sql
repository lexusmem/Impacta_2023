use AdventureWorksLT2022;
use Concessionaria;
use Consorcio;
use SeguroVeiculo;
use SysConVendas;
use SisDep;
use Clientes;
use Escola;

-- saber quais bancos de dados possuí
exec sp_databases;

-- saber quais as tabelas de um banco de dados
exec sp_tables;

-- saber quais as colunas de uma tabela
exec sp_help alunos;

-- retornar todos os dados da tabela Banco: AdventureWorksLT2022.SalesLT
select * from AdventureWorksLT2022.SalesLT.Product;
select * from AdventureWorksLT2022.SalesLT.ProductCategory;

-- retornar todos os dados da tabela Banco: SisDep
select * from Cargo;
select * from Dependente;
select * from Depto;
select * from Localidade;
select * from Projeto;
select * from Funcionario;

-- CLAUSULA MERGE
-- EQUIPARAR DADOS

CREATE DATABASE RecursosAdicionais
GO
USE RecursosAdicionais;

create table Base1(
		ID					int		identity(1,1)		primary key,
		Produto		varchar(50) not null unique,
		Valor			Decimal(10,2) not null
);

create table Base2(
		ID					int		identity(1,1)		primary key,
		Produto		varchar(50) not null unique,
		Valor			Decimal(10,2) not null
);

exec sp_tables
exec sp_help base1;
exec sp_help base2;

insert into Base1 (produto, valor)
values
('Notebook Dell Inspiron 15', 2500.00),
('Smartphone Samsung Galaxy S23', 3800.00),
('Monitor LG 27 polegadas', 1200.00),
('Teclado Mecânico Redragon Kumara K552 RGB', 250.00),
('Mouse Gamer Logitech G502 Hero', 300.00),
('Fone de Ouvido HyperX Cloud II', 450.00),
('HD Externo Seagate Backup Plus 1TB', 300.00),
('SSD Samsung 870 QVO 1TB', 500.00),
('Impressora Multifuncional Epson EcoTank L3210', 800.00),
('Roteador Wi-Fi TP-Link Archer C6', 200.00),
('Cabo HDMI 2.1 2 metros', 50.00),
('Carregador de Celular Turbo 33W', 100.00),
('Power Bank Xiaomi Redmi Power Bank 20000mAh', 200.00),
('Caixa de Som Bluetooth JBL Charge 5', 500.00),
('Smartwatch Apple Watch SE', 1800.00),
('Tablet Samsung Galaxy Tab S8', 3500.00),
('Webcam Logitech C920 HD Pro', 300.00),
('Cadeira Gamer Arozzi Verona Pro', 800.00),
('Mesa Gamer Warrior GD-110', 600.00),
('Kit Teclado e Mouse Gamer Havit HV-KB390S', 200.00),
('Mochila para Notebook Knup KP-9000', 150.00),
('Pen Drive SanDisk Cruzer Blade 64GB', 50.00),
('Cartão de Memória MicroSD Kingston 128GB', 100.00),
('Adaptador USB-C para HDMI', 30.00),
('Cabo Ethernet Cat6 5 metros', 20.00),
('Filtro de Linha Multitomada 6 tomadas', 100.00);

insert into Base2 (Produto, Valor)
values
('Notebook Dell Inspiron 15', 2500.00),
('Smartphone Samsung Galaxy S23', 3800.00),
('Monitor LG 27 polegadas', 1200.00),
('Teclado Mecânico Redragon Kumara K552 RGB', 250.00),
('Mouse Gamer Logitech G502 Hero', 300.00),
('Fone de Ouvido HyperX Cloud II', 450.00),
('HD Externo Seagate Backup Plus 1TB', 300.00),
('SSD Samsung 870 QVO 1TB', 500.00),
('Impressora Multifuncional Epson EcoTank L3210', 800.00),
('Roteador Wi-Fi TP-Link Archer C6', 200.00),
('Cabo HDMI 2.1 2 metros', 50.00),
('Carregador de Celular Turbo 33W', 100.00),
('Power Bank Xiaomi Redmi Power Bank 20000mAh', 200.00),
('Caixa de Som Bluetooth JBL Charge 5', 500.00),
('Smartwatch Apple Watch SE', 1800.00),
('Tablet Samsung Galaxy Tab S8', 3500.00),
('Webcam Logitech C920 HD Pro', 300.00),
('Cadeira Gamer Arozzi Verona Pro', 800.00),
('Mesa Gamer Warrior GD-110', 600.00),
('Kit Teclado e Mouse Gamer Havit HV-KB390S', 200.00),
('Mochila para Notebook Knup KP-9000', 150.00),
('Pen Drive SanDisk Cruzer Blade 64GB', 50.00),
('Cartão de Memória MicroSD Kingston 128GB', 100.00),
('Adaptador USB-C para HDMI', 30.00),
('Cabo Ethernet Cat6 5 metros', 20.00),
('Filtro de Linha Multitomada 6 tomadas', 100.00);

INSERT INTO Base1 (Produto, Valor)
VALUES
('Notebook Lenovo IdeaPad 3', 2200.00),
('Smartphone Motorola Edge 30', 2800.00),
('Monitor Acer Nitro 24 polegadas', 1000.00),
('Teclado Gamer Razer Huntsman Mini', 400.00),
('Mouse Gamer Corsair M65 RGB Elite', 350.00),
('Headset Gamer HyperX Cloud Stinger Core', 250.00),
('SSD Samsung 980 Pro 1TB', 700.00),
('Impressora Multifuncional Brother MFC-J497DW', 600.00),
('Roteador Wi-Fi Asus RT-ACRH13', 350.00),
('Cabo USB-C 3.2 Gen 2 1 metro', 40.00),
('Carregador de Celular Quick Charge 3.0', 80.00),
('Fones de Ouvido Bluetooth JBL Tune 510BT', 200.00),
('Smartwatch Amazfit Bip 3', 300.00),
('Tablet Lenovo Tab P11 Plus', 2500.00),
('Câmera Webcam Logitech Brio 4K', 1000.00),
('Cadeira Gamer Drift DR110', 500.00),
('Mesa Gamer Redragon GD-002', 400.00),
('Combo Teclado e Mouse Gamer Logitech MK270s', 150.00),
('Mochila para Notebook Samsonite GuardLite Pro', 200.00),
('SSD Externo Samsung T7 500GB', 400.00),
('Cartão de Memória MicroSD Lexar Professional 256GB', 200.00),
('Hub USB-C 4 portas com HDMI', 150.00),
('Cabo de Rede RJ45 Cat7 10 metros', 35.00),
('Nobreak Multitomada 7 tomadas', 250.00);

INSERT INTO Base2 (Produto, Valor)
VALUES
('Notebook Acer Aspire 5', 2300.00),
('Smartphone Xiaomi Redmi Note 11 Pro', 2400.00),
('Monitor Samsung Odyssey G25F', 900.00),
('Teclado Mecânico SteelSeries Apex 3', 300.00),
('Mouse Gamer Alienware AW510M', 450.00),
('Fone de Ouvido Gamer Razer BlackShark V2 X', 320.00),
('SSD Crucial MX500 1TB', 450.00),
('Impressora Jato de Tinta Canon Pixma G3110', 400.00),
('Roteador Wi-Fi Mesh TP-Link Deco M4', 600.00),
('Adaptador MicroSD para USB-C', 25.00),
('Power Bank Anker PowerCore III Slim 10000mAh', 120.00),
('Caixa de Som Bluetooth JBL Go 3', 200.00),
('Smartwatch Samsung Galaxy Watch 4 Classic', 1500.00),
('Tablet Huawei MatePad T10s', 1800.00),
('Webcam Razer Kiyo Pro', 500.00),
('Cadeira Gamer Newave NTC-200', 350.00),
('Mesa Gamer Havit HV-T650', 500.00),
('Mousepad Gamer Corsair MM300', 100.00),
('Mochila para Notebook Targus Icon Groove', 300.00),
('HD Externo WD Elements Portable 1TB', 250.00),
('Cartão de Memória MicroSD SanDisk Extreme Pro 64GB', 120.00),
('Concentrador USB 3.0 7 portas', 80.00),
('Cabo HDMI 2.0 5 metros', 30.00),
('Protetor de Surtos 6 tomadas com cabo de 2 metros', 150.00);

-- MERGE

select * from Base1;
select * from Base2;

UPDATE Base1
SET VALOR = 3000
WHERE ID = 1;

UPDATE Base1
SET VALOR = 2000
WHERE ID = 3;


-- equiparando os dados, verificando se a base 2 possui os mesmos dados da base 1
-- e caso não possua atualizando o produto da base 2
MERGE base2 as Destino
USING  base1 as Origem
ON Destino.id = origem.id
		when matched and destino.produto <> origem.produto then
		update
		set destino.produto = origem.produto

when not matched by target then
		insert
		(produto,valor)
		values
		(produto,valor);
----------------
-- equiparando os dados, verificando se a base 2 possui os mesmos valores de produtos da base 1
-- e caso não possua atualizando o valor da base 2
merge base2 as Destino
using base1 as origem
on destino.id = origem.id
when matched and destino.valor <> origem.valor then
	update
	set destino.valor = origem.valor;

select sum(valor) from Base1;
select sum(valor) from Base2;

select * from Base1;
select * from Base2;

-- Instruções $action
merge base2 as Destino
using base1 as origem
on destino.id = origem.id
when matched and destino.valor <> origem.valor or destino.produto <> origem.produto then
		update
		set destino.valor = origem.valor,
		destino.produto = origem.produto
when not matched by target then
			insert (produto, valor)
			values (produto, valor)
when not matched by source then
			delete
output
			$action					as[ação],
			inserted.id				as[id inserido],
			inserted.produto	as[produto inserido],
			inserted.valor			as[valor inserido],
			deleted.id				as[id excluido],
			deleted.produto		as[produto excluido],
			deleted.valor			as[valor excluido];
