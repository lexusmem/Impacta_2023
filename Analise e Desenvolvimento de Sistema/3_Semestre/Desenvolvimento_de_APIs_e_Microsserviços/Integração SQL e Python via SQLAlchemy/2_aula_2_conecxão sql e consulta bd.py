from sqlalchemy import create_engine
from sqlalchemy.sql import text

db_path = r'C:\Users\lexus\Documents\Estudos\Impacta_2023\Analise e Desenvolvimento de Sistema\3_Semestre\Desenvolvimento_de_APIs_e_Microsserviços\Integração SQL e Python via SQLAlchemy\biblioteca.db'

# quero usar o banco de dados nesse arquivo, usando o formato sqlite
engine = create_engine('sqlite:///' + db_path)

# mas se quisesse uma solução mais robusta, poderia
# usar mudando o código muito pouco
# engine = create_engine('postgresql://usuario:senha@localhost:5432/imobiliaria')


# criar a tabela
def criar_tabelas():
    with engine.connect() as con:
        create_tabela_aluno = """
        CREATE TABLE IF NOT EXISTS Aluno (
            id INTEGER PRIMARY KEY,
            nome TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
        """
        rs = con.execute(create_tabela_aluno)
        create_tabela_livro = """
        CREATE TABLE IF NOT EXISTS Livro (
            id_livro INTEGER PRIMARY KEY,
            id_aluno INTEGER,
            descricao TEXT NOT NULL,
            FOREIGN KEY(id_aluno) REFERENCES Aluno(id)  
        )
        """
        rs = con.execute(create_tabela_livro)


def criar_alunos():
    with engine.connect() as con:
        add_aluno = "INSERT INTO Aluno (id,nome,email) VALUES (1,'Lucas Mendes', 'lucas.mendes@exemplo.com');"
        rs = con.execute(add_aluno)
        add_aluno = "INSERT INTO Aluno (id,nome,email) VALUES (2,'Helena O. S.', 'helena@exemplo.com');"
        rs = con.execute(add_aluno)
        add_aluno = "INSERT INTO Aluno (id,nome,email) VALUES (3,'Mirtes', 'teescrevoumemail@exemplo.com');"
        rs = con.execute(add_aluno)


def criar_livros():
    with engine.connect() as con:
        add_livro = "INSERT INTO Livro (id_livro, id_aluno, descricao) VALUES (1,1,'Python Completo e Total')"
        rs = con.execute(add_livro)
        add_livro = "INSERT INTO Livro (id_livro, descricao) VALUES (2,'Memorias Póstumas de Brás Cubas')"
        rs = con.execute(add_livro)
        add_livro = "INSERT INTO Livro (id_livro, id_aluno, descricao) VALUES (3,2,'Gravidade')"
        rs = con.execute(add_livro)


# criar_tabelas()
# criar_alunos()


class AlunoNaoExisteException(Exception):
    pass
# estamos definindo uma classe AlunoNaoExisteException, que
# herda todas as funcionalidades, todos os métodos e atributos,
# de Exception
# no lugar do pass, escreveríamos as mudanças,
# as coisas que AlunoNaoExisteException faz diferente de Exception
# mas não fizemos mudança nenhuma (por isso pass)


# Consultando Tabelas e Colunas
with engine.connect() as con:  # conectar ao banco de dados
    # Consultar as tabelas do banco de dados
    sql_consulta_tabelas = text("SELECT name FROM sqlite_master")
    tabelas = con.execute(sql_consulta_tabelas)
    print('====Tabelas Existentes====')
    print(tabelas.fetchall())

    # Consultar as colunas das tabelas
    sql_consulta_colunas = text("SELECT * FROM aluno")
    resultado = con.execute(sql_consulta_colunas)
    colunas = resultado.keys()
    colunas_lista = list(colunas)
    sql_consulta_colunas_livros = text("SELECT * FROM livro")
    resultado = con.execute(sql_consulta_colunas_livros)
    colunas_livros = resultado.keys()
    colunas_lista_livros = list(colunas_livros)
    print('====Colunas Existentes====')
    print(colunas_lista)
    print(type(colunas_lista))
    print(colunas_lista_livros)
    print(type(colunas_lista_livros))


# 1b) Crie uma função todos_alunos que retorna um lista com um dicionario
# para cada aluno
def consulta_todos_aluno():
    with engine.connect() as con:  # conectar ao banco de dados
        sql_consulta = text("SELECT * FROM aluno")
        resultado = con.execute(sql_consulta)
        todos_alunos = []
        for row in resultado:
            todos_alunos.append(list(row))
    return todos_alunos


print('====Todos os Registros de Alunos====')
alunos = consulta_todos_aluno()
for aluno in alunos:
    print(aluno)


# 1) Crie uma função consulta_aluno que recebe a id de um aluno e devolve
# um dicionário com os dados desse aluno
# idéia da query no sql
# "SELECT * FROM aluno WHERE id = 2"
def consulta_aluno(id_aluno):
    with engine.connect() as con:  # conectar ao banco de dados
        sql_consulta = text("SELECT * FROM aluno WHERE id = :id_do_aluno")
        # id          : nome da coluna da tabela
        # id_aluno    : nome da variavel python que a funcao recebeu
        # id_do_aluno : nome do "buraco" definido na query sql_consulta
        #               nome passado como argumento do con.execute
        rs = con.execute(sql_consulta, {"id_do_aluno": id_aluno})
        # executamos a query definida em sql_consulta, preenchendo o "buraco" :id_do_aluno
        result = rs.fetchone()
        # fetchone: pega uma linha do resultado
        # se tiver mais linhas, podemos pegar a próxima com outro fetchone
        # se não tiver mais linhas, receberemos um None
        if result == None:  # se a query retornou 0 linhas, o primeiro fetchone já resulta None
            raise AlunoNaoExisteException
        # As linhas que o sqlalchemy devolve são parecidas com dicionários,
        # mas não é exatamente a mesma coisa. Por isso, fazemos uma conversão
        return result


aluno_1 = consulta_aluno(2)
print('====Consulta Unitária de Alunos====')
print(aluno_1)


# 1c) Crie uma função todos_livros que retorna um lista com um dicionario
# para cada livro
def consulta_todos_livros():
    with engine.connect() as con:  # conectar ao banco de dados
        sql_consulta = text("SELECT * FROM livro")
        resultado = con.execute(sql_consulta)
        todos_livros = []
        for row in resultado:
            todos_livros.append(list(row))
    return todos_livros


print('====Todos os Registros de Livros====')
livros = consulta_todos_livros()
for livro in livros:
    print(livro)


# Inserir dados na tabela
# INSERT INTO livro (id_livro, descricao) VALUES (4, "Harry Potter e a Pedra Filosofal")
# 2) Crie uma função cria livro que recebe os dados de um livro (id e descrição)
# e o adiciona no banco de dados

def cria_livro(id_livro, nome_livro):
    '''
    id_livro = Número do registro do livro.

    nome_livro = Nome do livro a ser registrado.
    '''
    with engine.connect() as con:  # conectar ao banco de dados
        data = ({'id_livro': id_livro, 'descricao': nome_livro},)
        sql_create = text(
            "INSERT INTO livro (id_livro, descricao) VALUES (:id_livro, :descricao)")
        con.execute(sql_create, data)
        con.commit()
        return print(f'Livro {nome_livro} registrado com Id: {id_livro}.')


# livro_5 = cria_livro(5, 'Harry Potter e a Câmara Secreta')
print('====Todos os Registros de Livros====')
livros = consulta_todos_livros()
for livro in livros:
    print(livro)


# 3) Crie uma função empresta_livro, que recebe a id de um livro, a id de um aluno
# e marca o livro como emprestado pelo aluno
def cria_empresta_livro():
    with engine.connect() as con:  # conectar ao banco de dados
        print('====Todos os Registros de Alunos====')
        alunos = consulta_todos_aluno()
        for aluno in alunos:
            print(aluno)

        print('====Todos os Registros de Livros====')
        livros = consulta_todos_livros()
        for livro in livros:
            print(livro)

        livro = input('Informe o ID do Livro para Atualização: ')

        aluno = input(
            'Informe o ID do Aluno que vai tomar emprestado o livro: ')

        data = ({'id_aluno': int(aluno), 'id_livro': int(livro)})
        sql_create = text(
            "UPDATE livro SET id_aluno = :id_aluno WHERE id_livro = :id_livro")
        con.execute(sql_create, data)
        con.commit()
        print('====Todos os Registros de Livros====')
        livros = consulta_todos_livros()
        for livro in livros:
            print(livro)


print('====Atualização de Emprestimo de Livros====')
cria_empresta_livro()


# 4) Crie uma função devolve_livro, que recebe a id de um livro, e marca o livro
# como disponível
def devolve_livro():
    with engine.connect() as con:  # conectar ao banco de dados
        print('====Função Devolver Livro====')
        print('====Todos os Registros de Alunos====')
        alunos = consulta_todos_aluno()
        for aluno in alunos:
            print(aluno)

        print('====Todos os Registros de Livros====')
        livros = consulta_todos_livros()
        for livro in livros:
            print(livro)

        livro = input('Informe o ID do Livro para Devolução: ')

        data = ({'id_aluno': None, 'id_livro': int(livro)})
        sql_create = text(
            "UPDATE livro SET id_aluno = :id_aluno WHERE id_livro = :id_livro")
        con.execute(sql_create, data)
        con.commit()
        print('====Todos os Registros de Livros====')
        livros = consulta_todos_livros()
        for livro in livros:
            print(livro)


# devolve_livro()


# 5) Crie uma função livros_parados que devolve a lista de todos os livros que não estão emprestados
print('====Lista todos os Livros sem Emprestimos====')


def livros_parados():
    with engine.connect() as con:  # conectar ao banco de dados
        sql_consulta = text("select * FROM livro WHERE id_aluno ISNULL")
        resultado = con.execute(sql_consulta)
        todos_livros = []
        for row in resultado:
            todos_livros.append(list(row))
    return todos_livros


livros_disponiveis = livros_parados()
for livros in livros_disponiveis:
    print(livros)


# 6) Crie uma função livros_do_aluno, recebe o nome do aluno e devolve a lista de todos
# os livros que estão com o aluno no momento
print('====Lista Livros por Nome====')


def livros_dos_alunos(nome):
    '''
    nome: Informe o nome do aluno para pesquisar
    quais livros possuem emprestados por ele.
    '''
    with engine.connect() as con:  # conectar ao banco de dados
        sql_consulta = text('''SELECT id_livro, id_aluno, nome, descricao FROM
                                livro join Aluno on livro.id_aluno = aluno.id
                                WHERE nome = :nome;''')
        resultado = con.execute(sql_consulta, {'nome': nome})
        todos = []
        for row in resultado:
            todos.append(list(row))
    return todos


alunos_livros = livros_dos_alunos('Lucas Mendes')
for livros in alunos_livros:
    print(livros)
