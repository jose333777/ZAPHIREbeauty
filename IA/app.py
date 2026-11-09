from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os



app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

app.config["SECRET_KEY"] = "clave_super_secreta"
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{os.path.join(basedir, 'database.db')}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    content = db.Column(db.Text, nullable=False)
    sender = db.Column(db.String(10))  # "user" o "ia"
    timestamp = db.Column(db.DateTime, server_default=db.func.now())


class Memory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    key = db.Column(db.String(100), nullable=False)
    value = db.Column(db.Text, nullable=False)

with app.app_context():
    db.create_all()

def guardar_memoria(username, key, value):
    memoria = Memory.query.filter_by(username=username, key=key).first()

    if memoria:
        memoria.value = value
    else:
        memoria = Memory(username=username, key=key, value=value)
        db.session.add(memoria)

    db.session.commit()


def cargar_memorias(username):
    memorias = Memory.query.filter_by(username=username).all()
    return {m.key: m.value for m in memorias}

def analizar_estilo(username, mensaje):
    texto = mensaje.lower()
    estilos = []

    if len(mensaje.split()) <= 4:
        estilos.append("frases_cortas")

    if mensaje.endswith("?"):
        estilos.append("pregunta")

    if any(p in texto for p in ["ok", "vale", "bien", "entonces"]):
        estilos.append("informal")

    if any(p in texto for p in ["error", "modelo", "función", "configurar", "codigo"]):
        estilos.append("tecnico")

    if estilos:
        guardar_memoria(username, "estilo", ", ".join(estilos))


def responder_con_estilo(username, mensaje):
    memorias = cargar_memorias(username)
    estilo = memorias.get("estilo", "")

    respuesta = "Te escucho"

    if "frases_cortas" in estilo:
        respuesta = "Dime."

    if "pregunta" in estilo:
        respuesta += " ¿Qué pasa?"

    if "tecnico" in estilo:
        respuesta = "Entendido. Explica el problema."

    if "informal" in estilo:
        respuesta += " 🙂"

    return respuesta


@app.route("/")
def home():
    if "user" in session:
        return redirect(url_for("chat"))
    return redirect(url_for("login"))


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if User.query.filter_by(username=username).first():
            flash("El usuario ya existe")
            return redirect(url_for("register"))

        hashed_password = generate_password_hash(password)
        user = User(username=username, password=hashed_password)

        db.session.add(user)
        db.session.commit()

        return redirect(url_for("login"))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            session["user"] = username
            return redirect(url_for("chat"))

        flash("Usuario o contraseña incorrectos")

    return render_template("login.html")


@app.route("/chat", methods=["GET", "POST"])
def chat():
    if "user" not in session:
        return redirect(url_for("login"))

    username = session["user"]

    if request.method == "POST":
        mensaje = request.form.get("mensaje")

        analizar_estilo(username, mensaje)

        db.session.add(Message(
            username=username,
            content=mensaje,
            sender="user"
        ))

        respuesta = responder_con_estilo(username, mensaje)

        db.session.add(Message(
            username=username,
            content=respuesta,
            sender="ia"
        ))

        db.session.commit()

    historial = Message.query.filter_by(username=username)\
        .order_by(Message.timestamp).all()

    return render_template("chat.html", historial=historial)


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
