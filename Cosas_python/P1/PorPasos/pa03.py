# Checkbutton, Radiobutton y uso de variables
# ariables Tkinter
# BooleanVar → True / False
# StringVar → texto seleccionado
# .get() → leer valor actual


import tkinter as tk

# ---------------- VENTANA PRINCIPAL ----------------
ventana = tk.Tk()
ventana.title("Tkinter - Paso 3")
ventana.geometry("300x320")

# ---------------- ETIQUETA PRINCIPAL ----------------
etiqueta = tk.Label(ventana, text="Selecciona tus opciones")
etiqueta.pack(pady=10)

# ---------------- CHECKBUTTON ----------------
# Variable asociada al Checkbutton (True / False)
opcion_python = tk.BooleanVar()

check_python = tk.Checkbutton(
    ventana,
    text="Me gusta Python",
    variable=opcion_python
)
check_python.pack(anchor="w", padx=20)

# ---------------- RADIOBUTTONS ----------------
# Variable común para los Radiobuttons
nivel = tk.StringVar(value="")

radio_principiante = tk.Radiobutton(
    ventana,
    text="Principiante",
    variable=nivel,
    value="Principiante"
)
radio_principiante.pack(anchor="w", padx=20)

radio_intermedio = tk.Radiobutton(
    ventana,
    text="Intermedio",
    variable=nivel,
    value="Intermedio"
)
radio_intermedio.pack(anchor="w", padx=20)

radio_avanzado = tk.Radiobutton(
    ventana,
    text="Avanzado",
    variable=nivel,
    value="Avanzado"
)
radio_avanzado.pack(anchor="w", padx=20)

# ---------------- FUNCIÓN ----------------
def mostrar_seleccion():
    gusta = opcion_python.get()      # True o False
    nivel_sel = nivel.get()          # Texto seleccionado

    texto = f"¿Te gusta Python? {gusta}\nNivel: {nivel_sel}"
    etiqueta_resultado.config(text=texto)

# ---------------- BOTÓN ----------------
boton = tk.Button(
    ventana,
    text="Mostrar selección",
    command=mostrar_seleccion
)
boton.pack(pady=15)

# ---------------- RESULTADO ----------------
etiqueta_resultado = tk.Label(ventana, text="")
etiqueta_resultado.pack()

# ---------------- BUCLE PRINCIPAL ----------------
ventana.mainloop()
