from flask import Flask, render_template, request, redirect, url_for
from banco.banco import Banco
from banco.conta import Conta


app = Flask(__name__)

contas_banco = Banco()


@app.route("/")
def home():
    return '<h1>Aplicativo de banco</h1>'


@app.route("/nova_conta", methods=["GET"])
def form_criar_conta():
    return render_template("form_conta.html")


@app.route("/nova_conta", methods=["POST"])
def criar_conta():
    numero = request.form["numero"]
    saldo = int(request.form["saldo"])
    contas_banco.incluir_conta(Conta(numero, saldo))
    return redirect('/consulta')


@app.route("/consulta")
def consulta():
    numero_conta = request.args.get('numero_conta')
    try:
        saldo = contas_banco.obter_saldo_da_conta(numero_conta)
        return render_template('form_consulta_conta.html', saldo=saldo)
    except KeyError:
        return render_template('form_consulta_conta.html', conta_nao_encontrada=numero_conta)


@app.route("/contas")
def listar_contas():
    contas = []
    for conta in contas_banco.contas.items():
        c = {}
        c['numero'] = conta[0]
        c['saldo'] = conta[1].saldo
        contas.append(c)
    contas = sorted(contas, key=lambda d: d['numero'])
    return render_template("lista_conta.html", contas=contas)


if __name__ == "__main__":
    app.run(debug=True)
