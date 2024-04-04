USE SisDep;

-- B�nus de R$ 100 para todos os funcion�rios
UPDATE Funcionario
SET Salario = Salario + 100;

-- Visualizar dados
SELECT * FROM Funcionario;

-- Operador Composto
-- Reajuste de 10% para todos os funcion�rios
UPDATE Funcionario
SET Salario *= 1.1;
-- SET Salario = Salario * 1.1;
-- SET Salario = Salario * 0.1 + Salario;

SELECT * FROM Funcionario;

-- Atualiza��o de mais de uma coluna simultaneamente
UPDATE Funcionario
SET Salario *= 1.05, idCargo = 2
WHERE idMatricula = 1000;

USE Concessionaria;
-- Visualizar nome das tabelas de um banco
exec sp_tables;

SELECT * FROM tblEstoque;

SELECT * FROM tblModelos;

-- Alterando o valor do ve�culo do estoque n� 4
UPDATE tblEstoque
SET precoEstoque = 45000
WHERE idEstoque = 4;