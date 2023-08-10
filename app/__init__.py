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
        return render_template('chat.html', username = session['alias'])
    
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        msg=''
        if request.method=='POST':
            email = request.form['email']
            password = request.form['password']
            record = datos.validar(email, password)
            session['alias'] = record[3]
            if record:
                session['loggedin'] = True
                session['correo'] = record[5]
                return redirect(url_for('chat'))
            else:
                msg = 'Nombre de Usuario/Contraseña incorrectos. Prueba de nuevo'
        return render_template('chat.html', msg=msg)

    @app.route('/register', methods=['GET', 'POST'])
    def register():
        correo = request.form['email']
        alias = request.form['alias']
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        contrasena = request.form['password']
        fec_nac = request.form['date'] 
        datos.cargar_usuario(nombre, apellido, alias, fec_nac, correo, contrasena)
        return redirect(url_for('index'))           

    @app.route('/logout')
    def logout():
        session.pop('loggedin', None)
        session.pop('correo', None)
        session.pop('alias', None)
        return redirect(url_for('index'))

    return app
    