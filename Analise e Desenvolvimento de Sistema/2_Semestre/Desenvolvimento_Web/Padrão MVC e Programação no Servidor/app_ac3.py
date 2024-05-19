from flask import Flask

app = Flask(__name__)


@app.route('/principal')
def abertura():  # controller
    return "abcdef"


if __name__ == '__main__':
    app.run()
