from sqlalchemy import create_engine
from sqlalchemy.sql import text

# caminho do arquivo BD
db_path = r'C:\Users\lexus\Documents\Estudos\Impacta_2023\Analise e Desenvolvimento de Sistema\3_Semestre\Desenvolvimento_de_APIs_e_Microsserviços\Aprofundamento e segurança em SQL\autentica.db'

# quero usar o banco de dados nesse arquivo, usando o formato sqlite
engine = create_engine('sqlite:///' + db_path)


def criar_tabelas():
    with engine.connect() as con:
        create_tabela_senhas = text("""
        CREATE TABLE IF NOT EXISTS users (
            login TEXT NOT NULL,
            senha TEXT NOT NULL
        )
        """)
        con.execute(create_tabela_senhas)
        con.commit()


def criar_usuarios():
    with engine.connect() as con:
        add_usuaria = text(
            "INSERT INTO users (login, senha) VALUES ('Minerva','123')")
        con.execute(add_usuaria)
        con.commit()
        add_usuario = text(
            "INSERT INTO users (login, senha) VALUES ('Jose','Carabina')")
        con.execute(add_usuario)
        add_admin = text(
            "INSERT INTO users (login, senha) VALUES ('admin','eLl96BFLVsoPrcOJGa0PhvwFnxt7ThKn')")
        con.execute(add_admin)
        con.commit()


# criar_tabelas()
# criar_usuarios()


# Validação de Senha de forma 'fraca'
def validar_admin_fraca(senha):
    with engine.connect() as con:
        sql_admin = text(
            f"SELECT * FROM users WHERE login='admin' and senha='{senha}'")
        print(sql_admin)
        rs = con.execute(sql_admin)
        result = rs.fetchone()
        if result == None:
            return 'nao autorizado'
        return 'autorizado'


# ataque
print(validar_admin_fraca("não sei' OR 'a'='a"))
print(validar_admin_fraca('não sei'))
print(validar_admin_fraca("eLl96BFLVsoPrcOJGa0PhvwFnxt7ThKn"))

# Forma correta de validação


def validar_admin_forte(senha):
    with engine.connect() as con:
        sql_admin = text(
            "SELECT * FROM users WHERE login='admin' and senha= :senha")
        print(sql_admin)
        rs = con.execute(sql_admin, {'senha': senha})
        result = rs.fetchone()
        if result == None:
            return 'nao autorizado'
        return 'autorizado'


print(validar_admin_forte("não sei' OR 'a'='a"))
print(validar_admin_forte('não sei'))
print(validar_admin_forte("eLl96BFLVsoPrcOJGa0PhvwFnxt7ThKn"))

# sql injection
#  sql injection é uma vulnerabilidade de segurança que ocorre quando
#  usamos input do usuário para montar a string SQL a ser executada

# prepared statement
# prepared statement é a proteção contra sql injection
# criamos strings sql que informam à nossa biblioteca de acesso
# ao banco de dados qual parte da string é codificada por nós
# e qual parte é input do usuário
# no nosso caso, a sintaxe para prepared statement é como no exemplo:
# sql_admin = text ("SELECT * FROM users WHERE login='admin' and senha= :senha")
# rs = con.execute(sql_admin , senha=senha)
