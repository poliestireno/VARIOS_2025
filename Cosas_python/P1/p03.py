# Importamos tkinter y messagebox para ventanas emergentes
import tkinter as tk
from tkinter import messagebox

# -----------------------------
# 1️⃣ Creamos la ventana principal
# -----------------------------
root = tk.Tk()                        # Creamos la ventana principal
root.title("Mi primera ventana Tkinter")  # Ponemos un título a la ventana
root.geometry("300x200")              # Definimos el tamaño: 300px ancho x 200px alto
root.configure(bg="#e0f7fa")          # Fondo de color suave (celeste claro)

# -----------------------------
# 2️⃣ Creamos una etiqueta (label) para mostrar un mensaje
# -----------------------------
mensaje = tk.Label(root, text="Hola, mundo!", font=("Helvetica", 16), bg="#e0f7fa")
# - text: el mensaje que se muestra
# - font: tamaño y tipo de letra
# - bg: color de fondo de la etiqueta
mensaje.pack(pady=20)                 # Empaquetamos la etiqueta en la ventana y ponemos margen vertical

# -----------------------------
# 3️⃣ Función que se ejecuta al presionar el botón
# -----------------------------
def cambiar_mensaje():
    mensaje.config(text="¡Has presionado el botón!")  # Cambiamos el texto de la etiqueta
    messagebox.showinfo("Mensaje", "¡Hola desde Tkinter!")  # Mostramos una ventana emergente

# -----------------------------
# 4️⃣ Creamos un botón
# -----------------------------
boton = tk.Button(root, text="Presióname", font=("Helvetica", 14), bg="#00796b", fg="white",
                  command=cambiar_mensaje)  
# - text: texto del botón
# - font: tipo y tamaño de letra
# - bg: color de fondo del botón
# - fg: color de texto
# - command: función que se ejecuta cuando se presiona

boton.pack(pady=10)                    # Empaquetamos el botón con un margen vertical

# -----------------------------
# 5️⃣ Ejecutamos el bucle principal de la ventana
# -----------------------------
root.mainloop()                        # Mantiene la ventana abierta y espera la interacción del usuario
