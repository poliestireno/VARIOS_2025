import tkinter as tk  # Importamos la librería Tkinter y la renombramos como 'tk'

# Creamos la ventana principal de la aplicación
ventana = tk.Tk()

# Establecemos el título que aparecerá en la barra de la ventana
ventana.title("Hola Tkinter")

# Creamos una etiqueta (Label) que mostrará el texto "Hola mundo"
# 'ventana' indica que la etiqueta pertenece a la ventana principal
etiqueta = tk.Label(ventana, text="Hola mundo")

# Colocamos la etiqueta dentro de la ventana
# 'pack()' es un gestor de geometría que posiciona el widget automáticamente
etiqueta.pack()

# Iniciamos el bucle principal de la aplicación
# Mantiene la ventana abierta y a la espera de eventos (clics, teclado, etc.)
ventana.mainloop()
