# Importamos tkinter para la interfaz gráfica y random para colores aleatorios
import tkinter as tk
import random

# -----------------------------
# 1️⃣ Ventana principal
# -----------------------------
root = tk.Tk()                        
# Creamos la ventana principal de la aplicación
root.title("Ejemplo Canvas + Checkbutton + after")  
# Ponemos un título que aparece en la barra superior
root.geometry("400x300")              
# Definimos el tamaño de la ventana: 400px ancho x 300px alto
root.configure(bg="#f0f0f0")          
# Configuramos un color de fondo suave para la ventana

# -----------------------------
# 2️⃣ Canvas para dibujar
# -----------------------------
canvas = tk.Canvas(root, width=200, height=200, bg="white")
# Creamos un canvas (lienzo) de 200x200 px con fondo blanco
canvas.pack(pady=20)
# Empaquetamos el canvas en la ventana con un margen vertical de 20 px

# Dibujamos un círculo inicial en el canvas
circulo = canvas.create_oval(50, 50, 150, 150, fill="red")  
# create_oval(x1, y1, x2, y2) dibuja un óvalo/círculo dentro del rectángulo definido
# fill="red" pone el color inicial del círculo

# -----------------------------
# 3️⃣ Checkbutton para activar/desactivar el cambio de color
# -----------------------------
activar = tk.BooleanVar()              
# Creamos una variable booleana que almacenará True o False según el Checkbutton
check = tk.Checkbutton(root, text="Activar cambio de color", variable=activar, bg="#f0f0f0")
# Creamos un Checkbutton (casilla) que activa/desactiva el cambio de color
# text: texto que se muestra al lado de la casilla
# variable: conecta el Checkbutton con la variable activar
# bg: color de fondo de la casilla
check.pack()
# Empaquetamos el Checkbutton en la ventana

# -----------------------------
# 4️⃣ Función que cambia el color del círculo
# -----------------------------
def cambiar_color():
    # Esta función se llamará cada segundo usando after()
    if activar.get():  
        # Solo cambia el color si el Checkbutton está activado (True)
        colores = ["red", "green", "blue", "yellow", "orange", "purple"]
        # Lista de colores posibles
        nuevo_color = random.choice(colores)
        # Elegimos un color al azar de la lista
        canvas.itemconfig(circulo, fill=nuevo_color)
        # Cambiamos el color del círculo en el canvas

    # Llamamos a esta función de nuevo después de 1000 ms (1 segundo)
    root.after(1000, cambiar_color)
    # Esto crea un bucle continuo para que la función se ejecute cada segundo

# -----------------------------
# 5️⃣ Iniciamos la función con after
# -----------------------------
cambiar_color()  
# Llamamos a la función por primera vez para que comience el ciclo de cambio de color

# -----------------------------
# 6️⃣ Bucle principal
# -----------------------------
root.mainloop()
# Iniciamos el bucle principal de la ventana
# Mantiene la ventana abierta y espera la interacción del usuario
# Permite que el Checkbutton se pueda marcar/desmarcar y el canvas se actualice
