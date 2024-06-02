-- colunas computadas
-- campos calculados

use SisDep;

select
	idMatricula, NomeFuncionario,Salario,Admissao,
	floor (cast((getdate()-Admissao) as float) / 365.25) as [tempo de serviço]
from Funcionario;

alter table funcionario
add temposevico as
floor (cast((getdate()-Admissao) as float) / 365.25);

select idMatricula, NomeFuncionario, Salario, Admissao, temposevico
from Funcionario;

exec sp_help funcionario;