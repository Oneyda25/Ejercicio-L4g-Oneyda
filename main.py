from flask import Flask, render_template

app = Flask(__name__)
@app.get("/")
def inicio():
    return render_template("index.html")

@app.get("/contactos")
def listarContactos():
    return render_template("contactos.html")

@app.get("/contactos/<int:contactoId>")
def editarContacto(contactoId):
    return render_template("editarContactos.html", id = contactoId)

@app.get("/edad/<int:edadId>")
def edadContacto(edadId):
    return render_template("edad.html", idd = edadId)



app.run(debug=True)
