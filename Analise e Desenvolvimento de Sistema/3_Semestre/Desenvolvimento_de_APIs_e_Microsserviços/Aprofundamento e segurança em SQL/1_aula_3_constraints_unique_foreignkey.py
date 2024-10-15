from sqlalchemy import create_engine
from sqlalchemy.sql import text

# caminho do arquivo BD
db_path = r'C:\Users\lexus\Documents\Estudos\Impacta_2023\Analise e Desenvolvimento de Sistema\3_Semestre\Desenvolvimento_de_APIs_e_Microsserviços\Aprofundamento e segurança em SQL\biblioteca.db'

# quero usar o banco de dados nesse arquivo, usando o formato sqlite
engine = create_engine('sqlite:///' + db_path)


def criar_tabelas():
    with engine.connect() as con:
        create_tabela_aluno = text("""
        CREATE TABLE IF NOT EXISTS Aluno (
            id INTEGER PRIMARY KEY,
            nome TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
        """)
        con.execute(create_tabela_aluno)
        con.commit()
        create_tabela_livro = text("""
        CREATE TABLE IF NOT EXISTS Livro (
            id_livro INTEGER PRIMARY KEY,
            id_aluno INTEGER,
            descricao TEXT NOT NULL,
            FOREIGN KEY(id_aluno) REFERENCES Aluno(id)  -- essa constraint é uma boa,
                                                        -- mas o SQLite está ignorando
                                                        -- em bancos mais sofisticados,
                                                        -- (como MySQL e Postgres)
                                                        -- ela impede que haja livro
                                                        -- com id_aluno invalida
                                                        -- id_aluno pode ser null, 
                                                        -- mas se tiver algum valor,
                                                        -- tem que ser válido
        )
        """)
        con.execute(create_tabela_livro)
        con.commit()


def criar_alunos():
    with engine.connect() as con:
        add_aluno = text(
            "INSERT INTO Aluno (id,nome,email) VALUES (1,'Alex Sousa', 'lucas.mendes@exemplo.com');")
        con.execute(add_aluno)
        con.commit()
        add_aluno = text(
            "INSERT INTO Aluno (id,nome,email) VALUES (2,'Pamela Melo', 'helena@exemplo.com');")
        con.execute(add_aluno)
        con.commit()
        add_aluno = text(
            "INSERT INTO Aluno (id,nome,email) VALUES (3,'Laura Melo', 'teescrevoumemail@exemplo.com');")
        con.execute(add_aluno)
        con.commit()


def criar_livros():
    with engine.connect() as con:
        add_livro = text(
            "INSERT INTO Livro (id_livro, id_aluno, descricao) VALUES (1,1,'Python completo e total')")
        con.execute(add_livro)
        con.commit()
        add_livro = text(
            "INSERT INTO Livro (id_livro, descricao) VALUES (2,'Memorias Póstumas de brás cubas')")
        con.execute(add_livro)
        con.commit()
        add_livro = text(
            "INSERT INTO Livro (id_livro, id_aluno, descricao) VALUES (3,2,'Gravidade')")
        con.execute(add_livro)
        con.commit()


# criar_tabelas()
# criar_alunos()
# criar_livros()

# podemos executar a função criar livros várias vezes?
# nao, ocasiona um erro, por violar a constraint de unicidade porque é primery key

# podemos executar a função criar tabelas várias vezes?
# sim, porque o comando usado é create table CREATE TABLE IF NOT EXISTS

# fetchall

print('===Consultar Todos Alunos===')


def consulta_todos_aluno():
    with engine.connect() as con:  # conectar ao banco de dados
        sql_consulta = text("SELECT * FROM aluno")
        resultado = con.execute(sql_consulta)
        rs = resultado.fetchall()
    return rs


alunos = consulta_todos_aluno()
print(alunos)
print(type(alunos))

for aluno in alunos:
    print(aluno)

# fetchone, fetchmany(20), fetchall
# pegam, respectivamente, uma linha do resultado
#                         vinte linhas do resultado
#                         todas as linhas do resultado
# fetchone pode ser ineficiente por fazer muitos acessos ao disco rígido
#           (pois o disco rígido é muito mais lento que a RAM, onde ficam as variáveis normais)
# fetchall pode ser ineficiente por carregar dados demais para a RAM,
#            impedindo o servidor de processar outras demandas
