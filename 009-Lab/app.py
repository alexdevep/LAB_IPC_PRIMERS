#https://flask.palletsprojects.com/en/2.1.x/quickstart/#a-minimal-application
# Importamos flask
# render_template, nos permite renderizar html
from flask import Flask, render_template

# Creamos una instancia, por defecto el nombre app.
# __name__ hace posible el manejo de nuestro recursos
app = Flask(__name__)

#URL = Decorador 
#Funcion = Vista

#Nuestra raiz o inicio
@app.route('/') #Decorador, define la ruta
def hola():
    return "Hola, mundo"#"<h1>Hola, mundo</h1>"

@app.route('/ipc2')
def ipc2():
    return "Hola, Bienvenidos a IPC2!"

#@app.route('/<nombre>/')
#@app.route('/<string:nombre>/') #Ser explicitos en tipo de variable
#def saludo(nombre):
#    return f"Hola, {nombre}"

#------------------------- TEMPLATES -------------------------
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/numeros')
def numeros():
    num = 100 
    return render_template("temp.html", num=num)

@app.route('/<string:nombre>/') #Ser explicitos en tipo de variable
def saludo(nombre):
    return render_template("saludo.html", name=nombre) #Revisar sintaxis

#Si obtienen este error -> "Error: Could not import 'development'.", agregar siguiente linea
#Corre el servidor
if __name__ == '__main__':
    app.run(debug=True)

#Inicializar application
#python app.py