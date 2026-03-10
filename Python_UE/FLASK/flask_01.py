from flask import Flask,render_template,jsonify,request

app = Flask(__name__) 

animal = {
    "raza":"gato",
    "altura":60,
    "edad":1
}

@app.route("/")
def inicio():
    return render_template("index.html",animal=animal)

@app.route("/animal", methods=["GET"])
def obtenerAnimal():
    return jsonify(animal)

@app.route("/incrementarEdad", methods=["POST"])
def incrementarEdad():
    animal["edad"] = animal["edad"] + 1
    return render_template("index.html",animal=animal)

@app.route("/incrementarEdadCantidad", methods=["POST"])
def incrementarEdadCantidad():
    cantidad = request.form.get("mi_cantidad",1,type=int)
    mul = request.form.get("mi_multiplicador",1,type=int)
    animal["edad"] = (animal["edad"] + cantidad) * mul
    return render_template("index.html",animal=animal)

@app.route("/cambiarRaza", methods=["POST"])
def cambiarRaza():
    animal["raza"] = request.form.get("nueva_raza",1,type=str)
    return render_template("index.html",animal=animal)



if __name__ == "__main__":
    app.run()

