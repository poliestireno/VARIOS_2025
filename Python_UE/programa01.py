import tkinter as tk  # Importa la librería para crear interfaces gráficas y la abrevia como 'tk'

ventana = tk.Tk()  # Crea la ventana principal de la aplicación
ventana.title("Hola")  # Define el texto que aparece en la barra de título de la ventana
ventana.geometry("300x200")  # Establece el tamaño de la ventana (ancho x alto en píxeles)

etiqueta = tk.Label(ventana, text="Hola mundo")  # Crea un letrero (etiqueta) con el texto "Hola mundo"
etiqueta.pack()  # Posiciona la etiqueta en la ventana (por defecto, arriba al centro)

etiqueta2 = tk.Label(ventana, text="Viva Viva")  # Crea una segunda etiqueta con el texto "Viva Viva"
etiqueta2.pack()  # La coloca debajo de la primera etiqueta

entrada1 = tk.Entry(ventana)  # Crea una caja de texto (input) para que el usuario escriba
entrada1.pack(pady=20)  # La coloca en la ventana con un espacio (margen) vertical de 20 píxeles

# Define qué pasará cuando el programa reciba una acción
def saludar():
    nombre = entrada1.get()  # Obtiene el texto que el usuario escribió en la caja 'entrada1'
    etiqueta3.config(text=nombre)  # Cambia el texto de la 'etiqueta3' por lo que se guardó en 'nombre'

# Crea un botón, le pone el texto "Dame" y le asigna la función 'saludar' al hacer clic
boton1 = tk.Button(ventana, text="Dame", command=saludar)
boton1.pack(pady=10)  # Lo coloca en la ventana con un margen vertical de 10 píxeles

etiqueta3 = tk.Label(ventana, text="")  # Crea una etiqueta vacía (servirá para mostrar el resultado)
etiqueta3.pack()  # La coloca al final de la interfaz

ventana.mainloop()  # Inicia el ciclo de espera de eventos (mantiene la ventana abierta)