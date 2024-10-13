from pytest import param
from sqlalchemy import create_engine, text

db_path = r'C:\Users\lexus\Documents\Estudos\Impacta_2023\Analise e Desenvolvimento de Sistema\3_Semestre\Desenvolvimento_de_APIs_e_Microsserviços\Integração SQL e Python via SQLAlchemy\biblioteca.db'

# quero usar o banco de dados nesse arquivo, usando o formato sqlite
engine = create_engine('sqlite:///' + db_path)

with engine.connect() as conn:
    # Criar um objeto de consulta SQL usando text()
    id_procura = 1
    sql = text("SELECT * FROM Aluno where id = :id")

    # Executar a consulta
    result = conn.execute(sql, {"id": id_procura})

    # Processar os resultados (por exemplo, imprimir)
    for row in result:
        print(row)

# consultar chaves das colunas
with engine.connect() as con:
    sql_consulta = text("SELECT * FROM Aluno;")
    rs = con.execute(sql_consulta)
    colunas = rs.keys()
    print(colunas)
