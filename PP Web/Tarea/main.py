from flask import Flask, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)
app.secret_key = "123ok"

#configuracion de la base de datos
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
db=SQLAlchemy(app)

#crear tabla usuarios
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    correo = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(50), nullable=False)
    notas = db.relationship("Nota", backref = "usuario", lazy = True)

class Nota(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Title = db.Column(db.String(100), nullable=False)
    Text = db.Column(db.String(1000), nullable=False)
    id_usuario = db.Column(db.Integer, db.ForeignKey("usuario.id"), nullable = False)


facts_list = ["La mayoría de las personas que sufren adicción tecnológica experimentan un fuerte estrés cuando se encuentran fuera del área de cobertura de la red o no pueden utilizar sus dispositivos",
              "Según un estudio realizado en 2018, más del 50 por ciento de las personas de entre 18 y 34 años se consideran dependientes de sus smartphones",
              "El estudio de la dependencia tecnológica es una de las áreas más relevantes de la investigación científica moderna",
              "Según un estudio de 2019, más del 60 por ciento de las personas responden a mensajes de trabajo en sus smartphones en los 15 minutos siguientes a salir del trabajo",
              "Una forma de combatir la dependencia tecnológica es buscar actividades que aporten placer y mejoren el estado de ánimo",
              "Elon Musk afirma que las redes sociales están diseñadas para mantenernos dentro de la plataforma, para que pasemos el mayor tiempo posible viendo contenidos",
              "Elon Musk también aboga por la regulación de las redes sociales y la protección de los datos personales de los usuarios. Afirma que las redes sociales recopilan una enorme cantidad de información sobre nosotros, que luego puede utilizarse para manipular nuestros pensamientos y comportamientos",
              "Las redes sociales tienen aspectos positivos y negativos, y debemos ser conscientes de ambos cuando utilicemos estas plataformas"]

coin = ["cara", "cruz"]

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/login", methods = ["POST"])
def login_data():
    correo = request.form.get("email")
    password = request.form.get("password")
    usuario_db = Usuario.query.filter_by(correo = correo).first()
    if usuario_db and usuario_db.password==password:
        session["usuario_id"] = usuario_db.id
        return render_template("notes.html",
                               correo = usuario_db.correo)
    else:
        return "correo o contraseña incorrectos"

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/data_recolection", methods = ["POST"])
def data_recolection():
    name = request.form.get("name")
    lastname = request.form.get("lastname")
    mail = request.form.get("email")
    password = request.form.get("password")
    birthday = request.form.get("birthday")
    country = request.form.get("country")
    new_user = Usuario(correo = mail, password = password, name = name, lastname = lastname, country = country)
    db.session.add(new_user)
    db.session.commit()

    return f"registro con exito {name} {lastname}. Tu correo electronico es {mail} y tu contraseña {password}. Naciste el {birthday}, esperamos que uses la pagina con responsabilidad. Esperamos que las disfrutes mucho desde {country}"

@app.route("/home")
def home():
    return """<h1>¡Hola! En esta página puedes aprender un monton de cosas interesantes acerca de la dependencia tecnológica</h1>
    <a href="/random_fact">¡Ver un dato aleatorio!</a>"""

@app.route("/home/random_fact")
def random_fact():
    return f'<p>{random.choice(facts_list)}</p>'

@app.route("/secret")
def cara_o_cruz():
    return f"<h1>¡Lanza una moneda!</h1><p>¡Prueba tu suerte! ¿Saldrá cara o cruz?</p><h2>{random.choice(coin)}</h2><button>Para lanzar de nuevo recarga la pagina</button>"

@app.route("/notas", methods = ["POST"])
def notas():
    Note_title = request.form.get("note")
    Note_text = request.form.get("contenido")
    usuario_id = session.get("usuario_id")
    new_note = Nota(Title=Note_title, Text=Note_text, id_usuario=usuario_id)
    db.session.add(new_note)
    db.session.commit()
    return f"Nota guardada con exito: {Note_title} - {Note_text}"

if __name__ == "__main__":
    app.run(debug=True)