from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    produtos_url = '/produtos'
    return f'<p><h2>Hello, World!</h2><p><a href="{produtos_url}">Produtos</a></p></p>'


@app.route('/produtos')
def produtos():
    response = jsonify([
        {
            "title": "Caneca Personalizada de Porcelana  do back end",
            "amount": 123.45,
            "installments": {"number": 3, "total": 41.15, "hasFee": True},
        },
        {
            "title": "Caneca de Tulipa do back end",
            "amount": 123.45,
            "installments": {"number": 3, "total": 41.15},
        }
    ])

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


if __name__ == '__main__':
    app.run(debug=True)
