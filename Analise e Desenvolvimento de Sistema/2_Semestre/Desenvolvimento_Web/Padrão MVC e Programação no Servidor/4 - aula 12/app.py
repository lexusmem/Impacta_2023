from flask import Flask, render_template, request, session, redirect, jsonify
import hashlib
from models.banco_de_dados import BancoDeDados

app = Flask(__name__)
app.secret_key = 'SENHA-MUITO-SECRETA'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/existe')
def existe():
    usuario = request.args.get('usuario')
    bd = BancoDeDados()
    obj_aluno = bd.obter_aluno(usuario)
    resultado = ''
    if obj_aluno is None:  # não existe Aluno com esse usuario
        resultado = 'O usuário "{0}" não existe'.format(usuario)
    return jsonify(mensagem=resultado)


@app.route('/login', methods=['GET', 'POST'])
def login():
    msg_erro = ''
    if request.method == 'POST':  # verifica se a requisição utiliza o método 'POST'
        usuario = request.form.get('usuario')
        senha = request.form.get('senha')
        # calcula o hash SHA-512 da senha digitada pelo usuário
        hash_da_senha = hashlib.sha512(senha.encode('UTF-8')).hexdigest()
        bd = BancoDeDados()  # inicializa a conexão com o BD
        # obtém os dados do aluno através do nome de usuário (se o usuário não existir, o valor devolvido será None)
        obj_aluno = bd.obter_aluno(usuario)
        if obj_aluno is not None and obj_aluno.senha == hash_da_senha:
            session['usuario'] = obj_aluno.usuario
            return redirect('/area_logada')
        else:
            msg_erro = 'Usuário e/ou senha inválidos'
    # Note que o return abaixo só será executado se nenhum outro retorn foi executado antes
    return render_template('login.html', erro=msg_erro)


@app.route('/area_logada')
def area_logada():
    # checa se existe a chave 'usuario' no dicionário da sessão (condição para o usuário estar logado)
    if 'usuario' in session:
        # obtém o nome de usuário guardado na sessão
        usuario = session['usuario']
        bd = BancoDeDados()
        # obtém os dados do aluno através do nome de usuário
        obj_aluno = bd.obter_aluno(usuario)
        return render_template('area_logada.html', aluno=obj_aluno)
    else:
        # redireciona usuários não logados para a rota de login
        return redirect('/login')


@app.route('/sair')
def sair():
    session.clear()  # limpa o objeto de sessão
    return redirect('/login')


if __name__ == '__main__':
    app.run(debug=True)
