from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/") 
def inicio():
  return render_template("inicio.html")
  
@app.route("/perfil", methods=["POST"])
def perfil():
  name = request.form.get("nombre")
  lastname = request.form.get("apellido")
  dnii = request.form.get("dni")
  genero = request.form.get("genero")

  fecha_nac = request.form.get("nacimiento")
  Correo = request.form.get("correo")
  Profesion = request.form.get("profesion")

  user = request.form.get("user")
  

  labiales = request.form.get("labiales")
  sombras =request.form.get("sombras")
  delineadores=request.form.get("delineadores")
  rubores=request.form.get("rubores")
  bases=request.form.get("bases")
  desmaquillantes=request.form.get("desmaquillantes")
  skin_care=request.form.get("skin_care")

  return render_template("perfil.html", name=name, lastname=lastname, 
    dnii=dnii,fecha_nac=fecha_nac, Correo=Correo, Profesion=Profesion, labiales=labiales, sombras=sombras, rubores=rubores, bases=bases,
    desmaquillantes=desmaquillantes, skin_care=skin_care, delineadores=delineadores, genero=genero, user=user )


