# =================================================================
# MANEJO DE LISTAS (LISTBOX) Y VENTANAS EMERGENTES (MESSAGEBOX)
# =================================================================

import tkinter as tk
# Importamos 'messagebox' explícitamente porque es un submódulo de tkinter
from tkinter import messagebox  

# ---------------- VENTANA PRINCIPAL ----------------
# Creamos la base de nuestra interfaz
ventana = tk.Tk()
ventana.title("Tkinter - Paso 4")
# Dimensiones: 300px de ancho por 350px de alto
ventana.geometry("300x350")

# ---------------- ETIQUETA INFORMATIVA ----------------
# Creamos el Label y aplicamos .pack() directamente en la misma línea.
# El método .pack() es el "empaquetador": coloca el widget en el primer
# espacio disponible (arriba por defecto). 
# 'pady=10' añade un colchón de 10 píxeles arriba y abajo para que no esté pegado.
tk.Label(ventana, text="Selecciona un lenguaje").pack(pady=10)

# ---------------- LISTBOX (Lista de opciones) ----------------
# El Listbox es un contenedor donde el usuario puede elegir uno o varios ítems.
# 'height=5' define cuántas filas serán visibles al mismo tiempo.
lista = tk.Listbox(ventana, height=5)

# .pack() sin parámetros adicionales lo centra horizontalmente y lo 
# coloca justo debajo del widget anterior (la etiqueta).
lista.pack()

# Insertamos elementos en la lista usando el índice especial tk.END.
# tk.END le dice a Python: "pon este elemento al final de la lista actual".
lista.insert(tk.END, "Python")      # Índice 0
lista.insert(tk.END, "Java")        # Índice 1
lista.insert(tk.END, "JavaScript")  # Índice 2
lista.insert(tk.END, "C")           # Índice 3
lista.insert(tk.END, "C++")         # Índice 4

# ---------------- LÓGICA DE SELECCIÓN ----------------
def mostrar_seleccion():
    """
    Función que analiza qué se ha marcado en el Listbox y 
    lanza una ventana emergente según el caso.
    """
    # .curselection() devuelve una TUPLA con los índices seleccionados.
    # Ejemplo: si eliges "Python", devuelve (0,). Si no hay nada, devuelve ().
    seleccion = lista.curselection()  

    # Comprobamos si la tupla está vacía (evalúa a False si no hay selección)
    if not seleccion:
        # messagebox.showerror lanza una ventana de alerta con icono de error (X roja)
        # Argumentos: ("Título de ventana", "Mensaje del cuerpo")
        messagebox.showerror(
            "Error",
            "No has seleccionado ningún lenguaje"
        )
    else:
        # Como es una tupla, accedemos al primer valor [0] para obtener el índice
        indice = seleccion[0]          
        # Con el índice, usamos .get(indice) para recuperar el texto (ej: "Java")
        lenguaje = lista.get(indice)   

        # messagebox.showinfo lanza una ventana informativa con icono azul (i)
        messagebox.showinfo(
            "Selección",
            f"Has seleccionado: {lenguaje}"
        )

# ---------------- BOTÓN DE ACCIÓN ----------------
# El botón se encarga de ejecutar la lógica definida arriba.
# 'pady=15' le da aire visual respecto al Listbox de arriba.
tk.Button(
    ventana,
    text="Mostrar selección",
    command=mostrar_seleccion  # Llamamos a la función sin ()
).pack(pady=15)

# ---------------- BUCLE PRINCIPAL ----------------
# Este método bloquea la ejecución del script de Python para que la ventana
# se quede abierta y responda a los clics del usuario.
ventana.mainloop()