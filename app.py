from flask import Flask, render_template, request
from flask import flash
from flask_wtf.csrf import CSRFProtect

import math
import forms

app =  Flask(__name__)
app.secret_key = 'clave secreta'

csrf = CSRFProtect()

@app.route("/")
def index():
    titulo = "Flask IDGS801"
    lista = ["Juan", "Mario", "Pedro", "Dario"]
    return render_template("index.html", titulo=titulo, lista=lista)

@app.route("/alumnos")
def alumnos():
    return render_template("alumnos.html")

@app.route("/usuarios", methods=['GET', 'POST'])
def usuarios():
    mat = 0
    nom = ''
    apa = ''
    ama = ''
    email = ''

    usuarios_class = forms.UserForm(request.form)

    if request.method == 'POST' and usuarios_class.validate():
        mat = usuarios_class.matricula.data
        nom = usuarios_class.nombre.data
        apa = usuarios_class.apaterno.data
        ama = usuarios_class.amaterno.data
        email = usuarios_class.correo.data
        mensaje = 'Bienvenido {}'.format(nom)
        flash(mensaje)

    return render_template("usuarios.html", form=usuarios_class, mat=mat, nom=nom, apa=apa, ama=ama, email=email)

@app.route("/operasBas", methods=['GET', 'POST'])
def operas1():
    n1 = 0
    n2 = 0
    res = 0

    if request.method == 'POST':
        n1 = request.form.get('n1')
        n2 = request.form.get('n2')
        res = float(n1) + float(n2)
    return render_template("operasBas.html", n1=n1, n2=n2, res=res)

@app.route("/resultado", methods=['GET', 'POST'])
def resultado():
    n1 = request.form.get('n1')
    n2 = request.form.get('n2')

    tem = float(n1)+float(n2)

    return f"La suma es: {tem}"


@app.route("/distancia", methods=['GET', 'POST'])
def distancia():
    v1 = 0
    v2 = 0
    x1 = 0
    x2 = 0
    y1 = 0
    y2 = 0
    res = 0

    if request.method == "POST":
        x1 = request.form.get("x1")
        x2 = request.form.get("x2")
        y1 = request.form.get("y1")
        y2 = request.form.get("y2")
        v1 = (float(x2)-float(x1))**2
        vx1 = math.exp(v1)
        v2 = (float(y2)-float(y1))**2
        vy2 = math.exp(v2)
        res = math.sqrt(float(v1) + float(v2))

    return render_template("distancia.html", x1=x1, x2=x2, y1=y1, y2=y2, res=res)



@app.route("/cinepolis", methods=["GET", "POST"])
def cine():
    resultado = None
    form = forms.UserFormc(request.form)

    if request.method == "POST" and form.validate():
        cantidad = form.cantidad.data
        compradores = form.compradores.data
        cineco = form.cineco.data

        max_boletos = compradores * 7
        if cantidad > max_boletos:
            return render_template(
                "cinepolis.html",
                form=form,
                resultado=f"Máximo {max_boletos} boletos para {compradores} compradores"
            )

        subtotal = cantidad * 12

        if cantidad > 5:
            descuento = 0.15
        elif cantidad >= 3:
            descuento = 0.10
        else:
            descuento = 0

        total = subtotal - (subtotal * descuento)

        if cineco == "si":
            total -= total * 0.10

        resultado = int(total)

    return render_template(
        "cinepolis.html",
        form=form,
        resultado=resultado
    )

@app.route("/hola")
def hola():
    return "¡Hola, Mundo!"

@app.route("/user/<string:user>")
def user(user):
    return f"Hello, {user}!"

@app.route("/numero/<int:n>")
def numero(n):
    return f"<h1>El numero es: {n}<h1>"

@app.route("/user/<int:id>/<string:user>")
def username(id, username):
    return f"<h1>¡Hola, {username}! tú ID es: {id}<h1>"

@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1, n2):
    return f"<h1>La suma es: {n1+n1}<h1>"

@app.route("/default/")
@app.route("/default/<string:param>")
def func(param = "juan"):
    return f"<h1>¡Hola, {param}!<h1>"

@app.route("/operas")
def operas():
    return '''
        <form>
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        </br>
        <label for="name">apaterno:</label>
        <input type="text" id="name" name="name" required>
    </form>
            '''

if __name__ == "__main__":
    csrf.init_app(app)
    app.run(debug=True)