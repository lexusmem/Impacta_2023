use Clientes_Alex;

exec sp_help;

-- Incluindo nova coluna Clientes
ALTER TABLE tblClientes
ADD complEnderecoCliente nvarchar(15);

exec sp_help tblclientes;
-- Excluir Constraint CK para ajuste da coluna data de nascimento
ALTER TABLE tblClientes
DROP CONSTRAINT CK_tblCliente_dataNascimentoCliente;

exec sp_help tblclientes;
-- Alterando tipo de dado da coluna data nascimento
ALTER TABLE			tblClientes
ALTER COLUMN	dataNascimentoCliente DATE;

exec sp_help tblclientes;
-- Incluindo Constraint coluna data nascimento
ALTER TABLE				tblClientes
ADD CONSTRAINT	CK_tblCliente_dataNascimentoCliente
CHECK						(dataNascimentoCliente < GETDATE());

-- Incluindo Clientes
INSERT INTO tblClientes
(nomeCliente, dataNascimentoCliente, enderecoCliente, complEnderecoCliente, bairro, cepCliente, codPrifissaoCliente, codCidade, codEstado)
values
('Alex Silva de Sousa', '2024-04-06','Rua Antonio Fernandes Aguillar, 137', 'Bl07 Ap32 Q B','Jardim Imperador',04177250,1,1,1);

select * from tblClientes;

-- excluindo registro de cliente
delete from tblClientes
where idCliente = 5;

-- alterando registro de cliente
UPDATE	tblClientes
SET			dataNascimentoCliente = '1987-01-19'
WHERE	idCliente = 6;

-- alterando registro de cliente com output
UPDATE	tblClientes
SET			dataNascimentoCliente = '1987-01-19'
OUTPUT	inserted.idCliente, inserted.nomeCliente, deleted.dataNascimentoCliente as Nascimento_Anterior, inserted.dataNascimentoCliente as Novo_Nascimento
WHERE	idCliente = 6;

-- alterando registro de cliente
UPDATE	tblClientes
SET			codFoneCliente = 7
WHERE	idCliente = 6;

select * from tblClientes;

-- Incluindo Fone
exec sp_help tblfone;
INSERT INTO	tblFone
(idCliente, fone, tipoFone)
VALUES			(6,23313236,'Celular');
select * from tblFone;
-- Incluindo Profiss�o
exec sp_help tblprofissao;
INSERT INTO	tblProfissao
VALUES			('Securit�rio');
select * from tblProfissao;

-- Incluindo Estado
exec sp_help tblEstado;
INSERT INTO	tblEstado
VALUES			('SP');
select * from tblEstado;

-- Incluindo Cidade
exec sp_help tblCidade;
INSERT INTO	tblCidade
						([cidade], [codEstado])
VALUES			('S�o Paulo', 1);
select * from tblCidade;

exec sp_help;

select * from tblClientes;

-- Abrir processo de transa��o
BEGIN TRANSACTION;

-- Verificar se costa processo de transa��o em aberto
SELECT @@TRANCOUNT;

UPDATE	tblClientes
SET			bairro = 'Jd. Imperador'
OUTPUT	inserted.idCliente, inserted.nomeCliente, deleted.bairro as Bairro_Anterior, inserted.bairro as Novo_Bairro
where		idCliente = 6;

select * from tblClientes;

-- Confirmar e fechar processo de altera��o atrav�s da transa��o aberta a altera��o estiver ok
COMMIT TRANSACTION

-- Caso a altera��o estiver incorreta
ROLLBACK TRANSACTION
