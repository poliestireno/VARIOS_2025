# Listbox y mensajes emergentes (messagebox)

import tkinter as tk
from tkinter import messagebox  # Para ventanas emergentes

# ---------------- VENTANA PRINCIPAL ----------------
ventana = tk.Tk()
ventana.title("Tkinter - Paso 4")
ventana.geometry("300x350")

# ---------------- ETIQUETA ----------------
tk.Label(ventana, text="Selecciona un lenguaje").pack(pady=10)

# ---------------- LISTBOX ----------------
# Listbox permite mostrar una lista de opciones
lista = tk.Listbox(ventana, height=5)
lista.pack()

# Insertamos elementos en la lista
lista.insert(tk.END, "Python")
lista.insert(tk.END, "Java")
lista.insert(tk.END, "JavaScript")
lista.insert(tk.END, "C")
lista.insert(tk.END, "C++")

# ---------------- FUNCIÓN ----------------
def mostrar_seleccion():
    seleccion = lista.curselection()  # Devuelve una tupla con el índice

    if not seleccion:
        # Si no hay nada seleccionado
        messagebox.showerror(
            "Error",
            "No has seleccionado ningún lenguaje"
        )
    else:
        indice = seleccion[0]          # Índice del elemento seleccionado
        lenguaje = lista.get(indice)   # Texto del elemento

        messagebox.showinfo(
            "Selección",
            f"Has seleccionado: {lenguaje}"
        )

# ---------------- BOTÓN ----------------
tk.Button(
    ventana,
    text="Mostrar selección",
    command=mostrar_seleccion
).pack(pady=15)

# ---------------- BUCLE PRINCIPAL ----------------
ventana.mainloop()
