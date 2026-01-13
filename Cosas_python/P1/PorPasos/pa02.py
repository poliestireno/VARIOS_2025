#
# Paso 2:
# Un Button
# Un Entry (campo de texto)
# Un evento (al pulsar el botón)
#
#


import tkinter as tk  # Importamos Tkinter

# ---------------- VENTANA PRINCIPAL ----------------
ventana = tk.Tk()                  # Creamos la ventana principal
ventana.title("Tkinter - Paso 2")  # Título de la ventana
ventana.geometry("300x150")        # Tamaño inicial (ancho x alto)

# ---------------- ETIQUETA ----------------
# Muestra un texto fijo en la ventana
etiqueta = tk.Label(ventana, text="Escribe tu nombre:")
etiqueta.pack(pady=5)  # pady añade espacio vertical

# ---------------- CAMPO DE TEXTO ----------------
# Entry permite introducir texto por teclado
entrada = tk.Entry(ventana)
entrada.pack(pady=5)

# ---------------- FUNCIÓN ----------------
# Se ejecutará al pulsar el botón
def saludar():
    nombre = entrada.get()                 # Obtenemos el texto escrito
    etiqueta_resultado.config(
        text=f"Hola, {nombre}"
    )                                      # Cambiamos el texto del Label

# ---------------- BOTÓN ----------------
# Al pulsarlo llama a la función saludar
boton = tk.Button(ventana, text="Saludar", command=saludar)
boton.pack(pady=5)

# ---------------- ETIQUETA DE RESULTADO ----------------
# Se usará para mostrar el saludo
etiqueta_resultado = tk.Label(ventana, text="")
etiqueta_resultado.pack(pady=5)

# ---------------- BUCLE PRINCIPAL ----------------
ventana.mainloop()
