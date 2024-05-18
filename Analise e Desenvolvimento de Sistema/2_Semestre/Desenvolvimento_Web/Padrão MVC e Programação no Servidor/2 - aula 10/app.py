from flask import Flask, render_template
from classes.curso import Curso


app = Flask(__name__)


@app.route('/')
def index():
    titulo = 'Página Inicial'
    conteudo = 'Conteúdo criado através da Jinja'
    return render_template('index.html', titulo=titulo, conteudo=conteudo)


@app.route('/cursos')
def cursos():
    lista_cursos = ['Desenvolvimento Web', 'Programação Orientada a Objetos']
    return render_template('cursos.html', lista=lista_cursos)


@app.route('/cursos/<nome>')
def curso_por_nome(nome):
    if nome == 'devweb':
        info = Curso(nome='Desenvolvimento Web',
                     descricao='Disciplina que lida com as tecnologias da Web',
                     dificuldade=1,
                     habilidade=['HTML', 'CSS', 'JavaScript'])
        return render_template('info_cursos.html', objeto=info)
    elif nome == 'poo':
        info = Curso(nome='Programação Orientado a Objetos',
                     descricao='Disciplina que ensina o paradigma de programação orientada a objetos',
                     dificuldade=2,
                     habilidade=['Dicionários',
                                 'Tratamento de exceções', 'Classes', 'Heranças'])
        return render_template('info_cursos.html', objeto=info)
    else:
        return '<h1>Curso Inexistente</h1>'


if __name__ == '__main__':
    app.run(debug=True)
