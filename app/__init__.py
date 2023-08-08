from flask import Flask, render_template
from config import Config

def init_app():
    app = Flask(__name__, static_folder=Config.STATIC_FOLDER, template_folder=Config.TEMPLATE_FOLDER)
    app.config.from_object(Config)

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/crear_cuenta')
    def crear_cuenta():
        return render_template('crear_cuenta.html')
        
    return app
    