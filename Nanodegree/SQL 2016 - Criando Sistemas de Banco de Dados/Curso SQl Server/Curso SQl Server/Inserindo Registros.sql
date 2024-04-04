USE Concessionaria;

EXEC sp_help tblMarcas;

-- Insert Posicional
INSERT INTO tblMarcas
VALUES			('FIAT');

-- Insert de várias linhas
INSERT INTO tblMarcas
VALUES			('FORD'),('CHEVROLET'),('VOLKSWAGEN'),('HONDA');

-- Visualizar dados
SELECT * FROM tblMarcas;

-- Insert Declarativo
INSERT INTO tblModelos
(idMarca, nomeModelo)
VALUES
(4, 'Onix'),(1, 'Uno'),(3, 'Eco Sport');

EXEC sp_help tblModelos;

-- Visualizar Dados
SELECT * FROM tblModelos;

-- Insert Declarativo
INSERT INTO tblEstoque
(idModelo, dataEntrada, precoEstoque, placa)
VALUES
(1, '2024-04-03',25000,'AAVISAR');

-- Visualizar Dados
SELECT * FROM tblEstoque;

-- Erro
INSERT INTO tblEstoque
(idModelo, dataEntrada, precoEstoque, placa)
VALUES
(2, '2024-04-03',25000,'AAVISAR');

EXEC sp_help tblEstoque;

-- Visualizar dados
SELECT * FROM tblEstoque;