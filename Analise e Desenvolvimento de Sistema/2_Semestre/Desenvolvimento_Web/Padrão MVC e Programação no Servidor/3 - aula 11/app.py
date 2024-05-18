from flask import Flask, request, render_template, session, redirect

app = Flask('__name__')
app.secret_key = 'SENHA-MUITO-SECRETA'


@app.route('/get')
def exemplo_get():
    usuario = request.args.get('usuario')
    senha = request.args.get('senha')
    if usuario != None and senha != None:
        return f'Os dados recebidos são usuario = {usuario} e senha = {senha}.'
    else:
        return render_template("get.html")


@app.route('/post', methods=['get', 'post'])
def exemplo_post():
    usuario = request.form.get('usuario')
    senha = request.form.get('senha')
    if usuario != None and senha != None:
        return f'Os dados recebidos são usuario = {usuario} e senha = {senha}.'
    else:
        return render_template("post.html")


@app.route('/login', methods=['get', 'post'])
def login():
    msg_erro = ''
    if request.method == 'POST':
        usuario = request.form.get('usuario')
        senha = request.form.get('senha')
        if usuario == 'Alex Sousa' and senha == '123456':
            session['usuario'] = 'Alex Sousa'
            return redirect('/area_logada')
        elif usuario == 'Maria' and senha == '654321':
            session['usuario'] = 'Maria'
            return redirect('/area_logada')
        else:
            msg_erro = 'Usuário e/ou Senha inválidos!'
    return render_template("login.html", erro=msg_erro)


@app.route('/area_logada')
def area_logada():
    if 'usuario' in session:
        nome_pessoa = ''
        media_pessoa = 0.0
        if session['usuario'] == 'Alex Sousa':
            nome_pessoa = 'Alex Silva de Sousa'
            media_pessoa = 7.5
        elif session['usuario'] == 'Maria':
            nome_pessoa = 'Maria dos Santos'
            media_pessoa = 8.6
        return render_template('area_logada.html', nome=nome_pessoa, media=media_pessoa)
    else:
        return redirect('/login')


@app.route('/sair')
def sair():
    session.clear()
    return redirect('/login')


if __name__ == '__main__':
    app.run(debug=True)
