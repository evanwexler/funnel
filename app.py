from blueprint import main
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_bootstrap import WebCDN



def create_app():
    app = Flask(__name__)
    app.register_blueprint(main)
    app.debug = True
    Bootstrap(app)
    app.extensions['bootstrap']['cdns']['jquery'] = WebCDN(
        '//cdnjs.cloudflare.com/ajax/libs/jquery/2.1.1/')
    return app

app = create_app()

if __name__ == '__main__':
    app.run()
