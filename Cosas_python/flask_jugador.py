"""
para instalar Flask hacerlo en un entorno virtual de python para aislar la instalacion del sistema principal

1️⃣ Instalar soporte de entornos virtuales (una sola vez)
sudo apt update
sudo apt install python3-venv python3-full -y
2️⃣ Crear el entorno virtual (en tu proyecto)
Desde la carpeta del proyecto flask_asir:

python3 -m venv venv
Se crea:

flask_asir/
 ├── app.py
 └── venv/
3️⃣ Activar el entorno virtual
source venv/bin/activate
Verás algo así:

(venv) gilbert@...
⚠️ Muy importante: mientras veas (venv) estás usando pip seguro.

4️⃣ Instalar Flask (ahora sí)
pip install flask
Comprobar:

python -c "import flask; print(flask.__version__)"
"""



# Importamos Flask y herramientas necesarias
from flask import Flask, jsonify, request  # jsonify para devolver JSON, request para manejar datos enviados por cliente

# Creamos la aplicación Flask
app = Flask(__name__)  # __name__ indica el nombre del módulo principal, Flask lo usa para encontrar recursos

# Creamos un "jugador" como diccionario de ejemplo
jugador = {
    "nombre": "Emilio Butragueño Santos",
    "posicion": "Delantero",
    "goles": 0,
    "asistencias": 0,
    "tarjetas": {
        "amarilla": 0,
        "roja": 0
    }
}

# -----------------------------
# RUTA PRINCIPAL
# -----------------------------
@app.route("/")  # Ruta principal del servidor
def inicio():
    """
    Función que devuelve un mensaje simple indicando que el servidor está activo.
    """
    return "Servidor de Jugador de Fútbol activo ✅"

# -----------------------------
# RUTA GET: Obtener datos del jugador
# -----------------------------
@app.route("/jugador", methods=["GET"])
def obtener_jugador():
    """
    Devuelve toda la información del jugador en formato JSON.
    """
    return jsonify(jugador)  # jsonify convierte diccionarios Python en JSON

# -----------------------------
# RUTA POST: Marcar un gol
# -----------------------------
@app.route("/gol", methods=["POST"])
def marcar_gol():
    """
    Incrementa el contador de goles del jugador.
    Se puede enviar opcionalmente en el body cuántos goles marcar.
    """
    # Obtenemos datos del cliente
    datos = request.get_json()  # request.get_json() convierte JSON enviado por cliente a diccionario Python

    # Si el cliente envía 'cantidad', usamos ese valor, sino 1
    cantidad = datos.get("cantidad", 1) if datos else 1

    jugador["goles"] += cantidad  # Sumamos goles al jugador

    # Devolvemos mensaje y estado actualizado
    return jsonify({"mensaje": f"{jugador['nombre']} ha marcado {cantidad} gol(es)",
                    "total_goles": jugador["goles"]})

# -----------------------------
# RUTA POST: Dar una asistencia
# -----------------------------
@app.route("/asistencia", methods=["POST"])
def dar_asistencia():
    """
    Incrementa el contador de asistencias del jugador.
    """
    datos = request.get_json()
    cantidad = datos.get("cantidad", 1) if datos else 1

    jugador["asistencias"] += cantidad

    return jsonify({"mensaje": f"{jugador['nombre']} ha dado {cantidad} asistencia(s)",
                    "total_asistencias": jugador["asistencias"]})

# -----------------------------
# RUTA POST: Recibir tarjeta amarilla
# -----------------------------
@app.route("/amarilla", methods=["POST"])
def tarjeta_amarilla():
    """
    Incrementa el contador de tarjetas amarillas del jugador.
    """
    jugador["tarjetas"]["amarilla"] += 1
    return jsonify({"mensaje": f"{jugador['nombre']} ha recibido una tarjeta amarilla",
                    "total_amarillas": jugador["tarjetas"]["amarilla"]})

# -----------------------------
# RUTA POST: Recibir tarjeta roja
# -----------------------------
@app.route("/roja", methods=["POST"])
def tarjeta_roja():
    """
    Incrementa el contador de tarjetas rojas del jugador.
    """
    jugador["tarjetas"]["roja"] += 1
    return jsonify({"mensaje": f"{jugador['nombre']} ha recibido una tarjeta roja",
                    "total_rojas": jugador["tarjetas"]["roja"]})

# -----------------------------
# RUTA PUT: Cambiar posición del jugador
# -----------------------------
@app.route("/posicion", methods=["PUT"])
def cambiar_posicion():
    """
    Permite actualizar la posición del jugador.
    Se debe enviar JSON con {'posicion': 'Nueva Posición'}
    """
    datos = request.get_json()
    if not datos or "posicion" not in datos:
        return jsonify({"error": "Debes enviar la posición"}), 400  # 400 Bad Request

    jugador["posicion"] = datos["posicion"]
    return jsonify({"mensaje": f"{jugador['nombre']} ahora juega como {jugador['posicion']}"})

# -----------------------------
# RUTA DELETE: Reiniciar estadísticas
# -----------------------------
@app.route("/reiniciar", methods=["DELETE"])
def reiniciar_estadisticas():
    """
    Reinicia todos los contadores del jugador a cero.
    """
    jugador["goles"] = 0
    jugador["asistencias"] = 0
    jugador["tarjetas"]["amarilla"] = 0
    jugador["tarjetas"]["roja"] = 0

    return jsonify({"mensaje": f"Estadísticas de {jugador['nombre']} reiniciadas",
                    "jugador": jugador})

# -----------------------------
# INICIO DEL SERVIDOR
# -----------------------------
if __name__ == "__main__":
    # host="0.0.0.0" permite que se acceda desde cualquier IP de la red
    # port=5000 define el puerto
    # debug=True activa recarga automática y mensajes de error para desarrollo
    app.run(host="0.0.0.0", port=5000, debug=True)


# -----------------------------
# 1️⃣ Servidor activo
# -----------------------------
# curl http://localhost:5000/ los que son get se pueden pedir en la url del navegador, el navegador solo hacer get a no ser que utilices postman.

#  Para crear algo POST, para modificar PUT, para borrar DELETE, el GET para obtener resultados

# -----------------------------
# 2️⃣ Obtener información del jugador
# -----------------------------
# curl http://localhost:5000/jugador los que son get se pueden pedir en la url del navegador

# -----------------------------
# 3️⃣ Marcar goles
# -----------------------------
# Marcar 1 gol (valor por defecto)
# curl -X POST -H "Content-Type: application/json" -d '{}' http://localhost:5000/gol

# Marcar 3 goles
# curl -X POST -H "Content-Type: application/json" -d '{"cantidad":3}' http://localhost:5000/gol

# -----------------------------
# 4️⃣ Dar asistencias
# -----------------------------
# Dar 1 asistencia (valor por defecto)
# curl -X POST -H "Content-Type: application/json" -d '{}' http://localhost:5000/asistencia

# Dar 2 asistencias
# curl -X POST -H "Content-Type: application/json" -d '{"cantidad":2}' http://localhost:5000/asistencia

# -----------------------------
# 5️⃣ Recibir tarjeta amarilla
# -----------------------------
# curl -X POST -H "Content-Type: application/json" -d '{}' http://localhost:5000/amarilla

# -----------------------------
# 6️⃣ Recibir tarjeta roja
# -----------------------------
# curl -X POST -H "Content-Type: application/json" -d '{}' http://localhost:5000/roja

# -----------------------------
# 7️⃣ Cambiar posición del jugador
# -----------------------------
# curl -X PUT -H "Content-Type: application/json" -d '{"posicion":"Centrocampista"}' http://localhost:5000/posicion

# Cambiar a defensa
# curl -X PUT -H "Content-Type: application/json" -d '{"posicion":"Defensa"}' http://localhost:5000/posicion

# -----------------------------
# 8️⃣ Reiniciar estadísticas
# -----------------------------
# curl -X DELETE http://localhost:5000/reiniciar
