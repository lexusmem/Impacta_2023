from flask import Flask
from flask_ngrok import run_with_ngrok
from pyngrok import ngrok

app = Flask(__name__)

ngrok.set_auth_token("2ouAeli6Z9ke8yR2fvlvTVF7cWb_4xpoEKV2qrgfBRp48RX2J")
ngrok.connect("5000")
run_with_ngrok(app)


@app.route('/')
def start():
    return 'Pamela eu te amo!'


if __name__ == '__main__':
    app.run()
