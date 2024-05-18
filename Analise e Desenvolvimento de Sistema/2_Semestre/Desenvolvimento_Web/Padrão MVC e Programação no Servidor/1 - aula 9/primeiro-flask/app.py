from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():  # controller
    return "Olá Mundo"


@app.route('/saudacao')
def saudacao():
    return render_template("saudacao.html")


@app.route('/cursos')
def cursos():
    return render_template("cursos.html")


@app.route('/cursos/<nome>')
def curso_nome(nome):
    if nome == 'devweb':
        return render_template('curso_devweb.html')
    elif nome == 'poo':
        return render_template('curso_poo.html')
    else:
        return render_template('erro.html')


@app.route('/cursos/<nome>/<int:ano>')
def curso_dois_nomes(nome, ano):
    return (f'Rota de demonstração que recebe dois valores: nome = {nome} e ano = {ano}.')


if __name__ == '__main__':
    app.run(debug=True)
