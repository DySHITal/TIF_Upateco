from flask import Flask, render_template, request, session, url_for, redirect
from config import Config
import datos

datos.create_if_not_exists()

def init_app():
    app = Flask(__name__, static_folder=Config.STATIC_FOLDER, template_folder=Config.TEMPLATE_FOLDER)
    app.secret_key = "super secret key"
    app.config.from_object(Config)

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/crear_cuenta')
    def crear_cuenta():
        return render_template('crear_cuenta.html')
    
    @app.route('/chat')
    def chat():
        username = session['email']
        return render_template('chat.html')
    
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        msg=''
        if request.method=='POST':
            email = request.form['email']
            password = request.form['password']
            record = datos.validar(email, password)
            if record:
                session['loggedin'] = True
                session['email'] = record[5]
                return redirect(url_for('chat'))
            else:
                msg = 'Nombre de Usuario/Contraseña incorrectos. Prueba de nuevo'
        return render_template('chat.html', msg=msg)

    return app
    