from blueprint import main
from flask import Flask
from flask_bootstrap import Bootstrap


def create_app():
    app = Flask(__name__)
    app.register_blueprint(main)
    app.debug = True
    Bootstrap(app)
    return app

app = create_app()

if __name__ == '__main__':
    app.run()
