from werkzeug.datastructures import RequestCacheControl
from werkzeug.exceptions import abort
#from typing_extensions import runtime
from flask import Flask, render_template


app=Flask(__name__)

app.secret_key='mi_llave_secretata'

@app.route('/')
@app.route('/index')
@app.route('/index.html')
def index():
    return render_template('index.html')
 
@app.route('/contacto')
@app.route('/contacto.html')
def contacto():
    return render_template('contacto.html')

@app.route('/acceder')
@app.route('/acceder.html')
def acceder():
    return render_template('acceder.html')

@app.route('/registrar')
@app.route('/registrar.html')
def registrar():
    return render_template('registrar.html')

@app.route('/iniciosesion')
@app.route('/iniciosesion.html')
def ingreso():
    return render_template('iniciosesion.html')

@app.route('/acercade')
@app.route('/acercade.html')
def acercade():
    return render_template('acercade.html')

@app.route('/salir')
def salir():
    return abort(404)

#Manejo de errores.
@app.errorhandler(404)
def pagina_no_encontrada(error):
    return render_template('error404.html', error=error), 404

#REST: representational state tranfer. 
#JSON:javascript object notation Servicios web
#API: aplcacion program interface 
@app.route('/api/mostrar/<nombre>')
def mostrar_json(nombre):
    valores = {
        'nombre': nombre,
        'metodo_http': RequestCacheControl.method
    }
    return valores

@app.route('/signup_form.html', methods=["GET", "POST"])
def show_signup_form():
    return render_template("signup_form.html")

if __name__== "__main__":
    app.run(debug=True, port=5000)