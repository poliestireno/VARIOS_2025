# Menú superior y ventanas secundarias


import tkinter as tk
from tkinter import messagebox

# ---------------- VENTANA PRINCIPAL ----------------
ventana = tk.Tk()
ventana.title("Tkinter - Paso 5")
ventana.geometry("350x300")

# ---------------- FUNCIONES ----------------
def mostrar_info():
    messagebox.showinfo(
        "Información",
        "Ejemplo de menú en Tkinter"
    )

def abrir_ventana_secundaria():
    # Creamos una nueva ventana
    ventana_sec = tk.Toplevel(ventana)
    ventana_sec.title("Ventana secundaria")
    ventana_sec.geometry("250x150")

    # Contenido de la ventana secundaria
    tk.Label(
        ventana_sec,
        text="Esta es una ventana secundaria"
    ).pack(pady=20)

    tk.Button(
        ventana_sec,
        text="Cerrar",
        command=ventana_sec.destroy
    ).pack()

def salir():
    ventana.destroy()

# ---------------- MENÚ SUPERIOR ----------------
menu_barra = tk.Menu(ventana)
ventana.config(menu=menu_barra)

# Menú Archivo
menu_archivo = tk.Menu(menu_barra, tearoff=0)
menu_barra.add_cascade(label="Archivo", menu=menu_archivo)
menu_archivo.add_command(label="Abrir ventana", command=abrir_ventana_secundaria)
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=salir)

# Menú Ayuda
menu_ayuda = tk.Menu(menu_barra, tearoff=0)
menu_barra.add_cascade(label="Ayuda", menu=menu_ayuda)
menu_ayuda.add_command(label="Acerca de", command=mostrar_info)

# ---------------- CONTENIDO PRINCIPAL ----------------
tk.Label(
    ventana,
    text="Usa el menú superior"
).pack(pady=80)

# ---------------- BUCLE PRINCIPAL ----------------
ventana.mainloop()
