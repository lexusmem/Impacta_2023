/*
	Vari�veis:
	
	. S�o endere�os de mem�ria utilizados para alocar informa��es tempor�rias
	. Podem ser criadas em procedures ou batches
	. Devem obrigatoriamente ser declaradas (DECLARE)
	. Devem obrigatoriamente ser inicializadas (SET)
	. Possuem escopo local (@nome) e global (@@nome)
	. Nomes de vari�veis:
		> N�o podem iniciar por numeral
		> N�o podem utilizar palavras reservadas
		> Tamanho m�ximo de 255 caracteres
		> Restri��o a caracteres especiais !@#$%&*(){}[]<>,.;:
*/ 

-- Exemplos
DECLARE @a int,@b int,@c decimal(6,2);
SET @a = 20;
SET @b = 4;
SET @c = @a / @b;
PRINT @c;

-- Falha na convers�o impl�cita de tipos
DECLARE @a2 int,@b2 int,@c2 decimal(6,2);
SET @a2 = 20;
SET @b2 = 3;
SET @c2 = CAST(@a2 AS decimal(6,2)) / CAST(@b2 AS decimal(6,2));
PRINT @c2;

/*
	Operadores Aritim�ticos
	+	Adi��o
	-	Subtra��o
	/	Divis�o
	*	Multiplica��o
	%	Resto da divis�o

	Operadores Relacionais

	>		Maior
	<		Menor
	>=		Maior ou igual
	!<		Maior ou igual
	<=		Menor ou igual
	!>		Menor ou igual
	=		igual
	<>		Diferente
	!=		Diferente
	
	Operadores L�gicos

	ALL			Verdadeiro se todas as condi��es forem (V)
	AND			Verdadeiro se duas express�es forem (V)
	ANY			Verdadeiro se qualquer condi��o for (V)
	BETWEEN		Verdadeiro se estiver dentro do intervalo de valores
	EXISTS		Verdadeiro se existir no conjunto de valores
	IN			Verdadeiro se existir na lista de valores
	LIKE		Verdadeiro se parte da informa��o � encontrada
	NOT			Reverter um valor l�gico (Boleano)
	OR			Verdadeiro se uma das express�es for (V)
	SOME		Verdadeiro se parte das compara��es for (V)


*/

-- Controle de Fluxo

-- IF / ELSE
DECLARE @rnd1 float, @rnd2 float; 
SET @rnd1 = (SELECT RAND());
SET @rnd2 = (SELECT RAND());
select @rnd1 = RAND() 
IF @rnd1 > @rnd2
	PRINT 'O 1� Aleat�rio � maior'
ELSE
	PRINT 'O 2� Aleat�rio � maior';

-- Bloco com mais de um comando
DECLARE @rnd3 float, @rnd4 float ;
SET @rnd3 = (SELECT RAND());
SET @rnd4 = (SELECT RAND());

IF @rnd3 > @rnd4
	BEGIN
		PRINT @rnd3;
		PRINT 'O 1� Aleat�rio � maior';
	END
ELSE
	IF @rnd4 > @rnd3
		BEGIN
			PRINT @rnd4;
			PRINT 'O 2� Aleat�rio � maior';
		END
		ELSE
			PRINT 'Valores S�o Iguais';

-- Aleat�rio entre 1 e 60
DECLARE @rnd5 int
SET @rnd5 = ((SELECT RAND() * 59) + 1);
PRINT @rnd5;

-------
declare @a int, @b int,@c int;
set @a = 40;
set @b = 20;
set @c = @c + @a + @b;
print @c;

-----
declare @a int, @b int,@c int = 0;
set @a = 10;
set @b = 5;
set @c = ((@a + @b)/3)*2
set @c  *= 1.2
print @c;

