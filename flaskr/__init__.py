import os

from flask import Flask

def create_app(test_config=None):
    # crea y configura la app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # cargar la configuración de la instancia, si existe, cuando no se está probando
        app.config.from_pyfile('config.py', silent=True)
    else:
        # cargar la configuración de prueba si se pasa
        app.config.from_mapping(test_config)

    # Asegúrese de que la carpeta de instancia exista
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # una página sencilla que dice hola
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    from . import db
    db.init_app(app)

    

    return app

