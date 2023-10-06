from flask import Flask, render_template

# esta variable nos ayuda para crerar las rutas del servidor
app = Flask(__name__)

# Para crear una ruta se tiene que utilizar un decorador "@" a la variable antes creada app
# El metodo route nos ayuda a crear la ruta de direccionamiento de las paginas
# la pagina principal se puede crear con solamente un slash "/" ---> route('/')


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


# Esta sentencia hace que siempre se este ejecuntando todo el tiempo
# Le dices que si este es el archivo principal arranque la app
if __name__ == '__main__':
    # app.run()  # .run() es el metodo que arranca la app, cuando el desarrollo ya esta terminado
    # el parametro debug=True le dice a la consola que estaras haciendo cambios seguido y que no es necesario inicializarlo todo momento
    app.run(debug=True)
# Para que los cambios se reflejen una vez ya hallas inicializado un servidor
# tendras que cerrarlo con 'ctrl + c' y volver a inicializarlo en consola con "python nombre_archivo.py"
