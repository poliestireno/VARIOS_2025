from flask import Flask,render_template,jsonify

app = Flask(__name__)


paisFrancia = {
    "nombre":"Francia",
    "capital":"Paris",
    "moneda":"Euro",
    "poblacion":1234567
}
paisIrlanda = {
    "nombre":"Irlanda",
    "capital":"Dublin",
    "moneda":"Euro",
    "poblacion":9
}



@app.route("/")
def ini():
    return render_template("index2.html",paisIrlanda=paisIrlanda,paisFrancia=paisFrancia)

@app.route("/irlanda", methods=["GET"])
def obtenerIrlanda():
    return jsonify(paisIrlanda)

@app.route("/francia", methods=["GET"])
def obtenerFrancia():
    return jsonify(paisFrancia)

@app.route("/nacerIrlanda", methods=["POST"])
def nacer1Irlanda():
    paisIrlanda["poblacion"] = paisIrlanda["poblacion"] + 1
    return render_template("index2.html",paisIrlanda=paisIrlanda,paisFrancia=paisFrancia)

@app.route("/morirIrlanda", methods=["POST"])
def morir1Irlanda():
    if (paisIrlanda["poblacion"]>0):
        paisIrlanda["poblacion"] = paisIrlanda["poblacion"] - 1
    return render_template("index2.html",paisIrlanda=paisIrlanda,paisFrancia=paisFrancia)


@app.route("/nacerFrancia", methods=["POST"])
def nacer1Francia():
    paisFrancia["poblacion"] = paisFrancia["poblacion"] + 1
    return render_template("index2.html",paisIrlanda=paisIrlanda,paisFrancia=paisFrancia)

@app.route("/morirFrancia", methods=["POST"])
def morir1Francia():
    if (paisFrancia["poblacion"]>0):
        paisFrancia["poblacion"] = paisFrancia["poblacion"] - 1
    return render_template("index2.html",paisIrlanda=paisIrlanda,paisFrancia=paisFrancia)



if __name__ == "__main__":
    app.run()