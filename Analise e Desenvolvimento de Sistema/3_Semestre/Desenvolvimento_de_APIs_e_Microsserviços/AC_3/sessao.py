from flask import Flask, jsonify, render_template

app = Flask(__name__)

u = {'nome': 'Alex', 'idade': 37}


@app.route('/', methods=['GET'])
def start():
    return render_template('teste.html', usuario=u, nome=u['nome'], idade=u['idade'])


@app.route('/numeros/<float(signed=True):a>', methods=['GET'])
def numero(a):
    teste = {
        'Valor Recebido': a,
        'Tipo': 'Negativo' if a < 0 else 'Positivo ou Zero'
    }
    return render_template('teste_1.html', resposta=teste)


if __name__ == '__main__':
    app.run(debug=True)
