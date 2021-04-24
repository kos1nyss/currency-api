from flask import Flask
from data import currency_api

app = Flask(__name__)

if __name__ == '__main__':
    app.register_blueprint(currency_api.blueprint)
    app.run()
