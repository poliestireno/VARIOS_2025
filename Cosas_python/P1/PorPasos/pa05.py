# =================================================================
# MENÚS SUPERIORES, SUBMENÚS Y GESTIÓN DE VENTANAS MÚLTIPLES
# =================================================================

import tkinter as tk
from tkinter import messagebox

# ---------------- VENTANA PRINCIPAL (Root) ----------------
# Esta es la ventana 'madre' o raíz de toda la aplicación.
ventana = tk.Tk()
ventana.title("Tkinter - Paso 5")
ventana.geometry("350x300")

# ---------------- LÓGICA Y FUNCIONES ----------------

def mostrar_info():
    """Lanza un cuadro de diálogo informativo típico."""
    messagebox.showinfo(
        "Información",
        "Ejemplo de menú en Tkinter"
    )

def abrir_ventana_secundaria():
    """
    Función para crear una ventana nueva sin cerrar la anterior.
    tk.Toplevel() es la clave aquí.
    """
    # Creamos una ventana de tipo Toplevel. 
    # Al pasarle 'ventana' como argumento, le decimos que su "padre" es la principal.
    ventana_sec = tk.Toplevel(ventana)
    ventana_sec.title("Ventana secundaria")
    ventana_sec.geometry("250x150")

    # Los widgets de esta ventana deben tener como primer argumento 'ventana_sec'
    tk.Label(
        ventana_sec,
        text="Esta es una ventana secundaria"
    ).pack(pady=20) # 'pady' separa el texto del borde superior

    tk.Button(
        ventana_sec,
        text="Cerrar",
        # .destroy() cierra la ventana específica (en este caso, la secundaria)
        command=ventana_sec.destroy
    ).pack()

def salir():
    """Cierra la aplicación completa."""
    # Al destruir la ventana raíz (ventana), se termina el programa.
    ventana.destroy()

# ---------------- CONFIGURACIÓN DEL MENÚ ----------------

# 1. Creamos la "Barra de Menú" base que vivirá en la parte superior.
menu_barra = tk.Menu(ventana)

# 2. Le decimos a la ventana principal que use esa barra de menú.
# .config() es como ir a "Ajustes" de la ventana y cambiar el parámetro 'menu'.
ventana.config(menu=menu_barra)

# 3. CREACIÓN DEL MENÚ "ARCHIVO"
# 'tearoff=0' evita que el menú se pueda "desprender" como una ventana flotante (estilo antiguo).
menu_archivo = tk.Menu(menu_barra, tearoff=0)

# Añadimos el menú "Archivo" a la barra principal usando 'add_cascade'.
# Se llama cascada porque al hacer clic, "caen" las opciones hacia abajo.
menu_barra.add_cascade(label="Archivo", menu=menu_archivo)

# Añadimos botones (comandos) dentro del menú Archivo:
menu_archivo.add_command(label="Abrir ventana", command=abrir_ventana_secundaria)
# .add_separator() dibuja una línea horizontal divisoria (muy útil para organizar).
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=salir)

# 4. CREACIÓN DEL MENÚ "AYUDA"
menu_ayuda = tk.Menu(menu_barra, tearoff=0)
# Lo anclamos a la barra principal.
menu_barra.add_cascade(label="Ayuda", menu=menu_ayuda)
# Añadimos la opción "Acerca de".
menu_ayuda.add_command(label="Acerca de", command=mostrar_info)

# ---------------- CONTENIDO DE LA VENTANA PRINCIPAL ----------------
# Ponemos una etiqueta central para que la ventana no se vea vacía.
# Usamos un 'pady' grande (80) para empujar el texto hacia el centro vertical.
tk.Label(
    ventana,
    text="Usa el menú superior"
).pack(pady=80)

# ---------------- BUCLE DE EVENTOS ----------------
# Mantenemos la aplicación viva y atenta a los clics del menú.
ventana.mainloop()