from flask import Flask, jsonify, request, render_template,redirect,url_for  # Importamos Flask, JSON y renderizado de HTML

# -----------------------------
# Creamos la app Flask
# -----------------------------
app = Flask(__name__)

# -----------------------------
# Datos del jugador
# -----------------------------
jugador = {
    "nombre": "Emilio Butragueño Santos",
    "posicion": "Delantero",
    "goles": 0,
    "asistencias": 0,
    "tarjetas": {"amarilla": 0, "roja": 0}
}

# -----------------------------
# Página principal con formularios
# -----------------------------
@app.route("/", methods=["GET"])
def index():
    # Flask busca automáticamente en la carpeta /templates/
    return render_template("index.html", jugador=jugador)

# -----------------------------
# Rutas originales adaptadas para recibir datos de formulario
# -----------------------------
@app.route("/gol", methods=["POST"])
def marcar_gol():
    """
    Incrementa los goles del jugador. 
    Recibe cantidad desde formulario o JSON.
    """
    # Intentamos leer de JSON
    datos = request.get_json(silent=True)
    cantidad = datos.get("cantidad", 1) if datos else None

    # Si no hay JSON, leemos del formulario
    if cantidad is None:
        cantidad = int(request.form.get("cantidad", 1))

    jugador["goles"] += cantidad
    
    #si se quiere que vuelva se redirige al index
    return redirect(url_for('index'))
    # si se quiere que muestre los datos se descomenta lo siguiente
    #return jsonify({"mensaje": f"{jugador['nombre']} ha marcado {cantidad} gol(es)",
     #               "total_goles": jugador["goles"]})

@app.route("/asistencia", methods=["POST"])
def dar_asistencia():
    """
    Incrementa las asistencias del jugador.
    Recibe cantidad desde formulario o JSON.
    """
    datos = request.get_json(silent=True)
    cantidad = datos.get("cantidad", 1) if datos else None

    if cantidad is None:
        cantidad = int(request.form.get("cantidad", 1))

    jugador["asistencias"] += cantidad
    return jsonify({"mensaje": f"{jugador['nombre']} ha dado {cantidad} asistencia(s)",
                    "total_asistencias": jugador["asistencias"]})

@app.route("/amarilla", methods=["POST"])
def tarjeta_amarilla():
    """
    Incrementa tarjetas amarillas.
    """
    jugador["tarjetas"]["amarilla"] += 1
    return jsonify({"mensaje": f"{jugador['nombre']} ha recibido una tarjeta amarilla",
                    "total_amarillas": jugador["tarjetas"]["amarilla"]})

@app.route("/roja", methods=["POST"])
def tarjeta_roja():
    """
    Incrementa tarjetas rojas.
    """
    jugador["tarjetas"]["roja"] += 1
    return jsonify({"mensaje": f"{jugador['nombre']} ha recibido una tarjeta roja",
                    "total_rojas": jugador["tarjetas"]["roja"]})

@app.route("/posicion", methods=["POST"])
def cambiar_posicion():
    """
    Cambia la posición del jugador.
    Recibe datos desde formulario o JSON.
    """
    datos = request.get_json(silent=True)
    nueva_pos = datos.get("posicion") if datos else request.form.get("posicion")

    if not nueva_pos:
        return jsonify({"error": "Debes enviar la posición"}), 400

    jugador["posicion"] = nueva_pos
    return jsonify({"mensaje": f"{jugador['nombre']} ahora juega como {jugador['posicion']}"})

@app.route("/reiniciar", methods=["POST"])
def reiniciar_estadisticas():
    """
    Reinicia todas las estadísticas a cero.
    """
    jugador["goles"] = 0
    jugador["asistencias"] = 0
    jugador["tarjetas"]["amarilla"] = 0
    jugador["tarjetas"]["roja"] = 0
    return jsonify({"mensaje": f"Estadísticas de {jugador['nombre']} reiniciadas",
                    "jugador": jugador})

# -----------------------------
# Ejecutar servidor
# -----------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)