import tkinter as tk
from tkinter import messagebox

# -----------------------------
# Ventana principal
# -----------------------------
root = tk.Tk()
root.title("Juego de Magia Matemática")
root.geometry("400x300")           # tamaño de ventana
root.configure(bg="#f0f0f0")       # fondo claro

# -----------------------------
# Variables para el juego de magia
# -----------------------------
resultado = 0         # suma de valores de las tarjetas donde el alumno diga "Sí"
indice_tarjeta = 0    # tarjeta actual que se está mostrando

# Definimos las 3 tarjetas con su valor y números que contiene
# Valor = potencia de 2 (1, 2, 4)
tarjetas = [
    (1, [1, 3, 5, 7]),  # tarjeta 1
    (2, [2, 3, 6, 7]),  # tarjeta 2
    (4, [4, 5, 6, 7])   # tarjeta 3
]

# -----------------------------
# Canvas para mostrar la tarjeta
# -----------------------------
canvas = tk.Canvas(root, width=350, height=150, bg="#ffffff", highlightthickness=1)
canvas.place(relx=0.5, rely=0.4, anchor="center")

# Función para dibujar la tarjeta con los números
def mostrar_tarjeta_canvas(numeros):
    canvas.delete("all")   # borramos contenido previo
    # Dibujamos un rectángulo simple para la tarjeta
    canvas.create_rectangle(10, 10, 340, 140, fill="#ffffff", outline="#000000", width=4)
    # Escribimos los números en el centro
    canvas.create_text(175, 75, text=str(numeros), font=("Helvetica", 18), fill="#000000")

# -----------------------------
# Función para mostrar la tarjeta actual
# -----------------------------
def mostrar_tarjeta():
    global indice_tarjeta
    if indice_tarjeta < len(tarjetas):
        valor, numeros = tarjetas[indice_tarjeta]
        mostrar_tarjeta_canvas(numeros)
    else:
        # Si ya no hay más tarjetas, mostramos el resultado final
        messagebox.showinfo("Resultado", f"🎩 El número que estabas pensando es {resultado} 🎩")
        root.destroy()  # cerramos la ventana

# -----------------------------
# Funciones de botones
# -----------------------------
def presionar_si():
    global resultado, indice_tarjeta
    valor, _ = tarjetas[indice_tarjeta]  # obtenemos el valor de la tarjeta
    resultado += valor                     # sumamos al resultado
    indice_tarjeta += 1                    # pasamos a la siguiente tarjeta
    mostrar_tarjeta()

def presionar_no():
    global indice_tarjeta
    indice_tarjeta += 1                    # solo pasamos a la siguiente tarjeta
    mostrar_tarjeta()

# -----------------------------
# Botones Sí / No
# -----------------------------
boton_si = tk.Button(root, text="Sí", font=("Helvetica", 14), bg="#4CAF50", fg="white", command=presionar_si)
boton_no = tk.Button(root, text="No", font=("Helvetica", 14), bg="#F44336", fg="white", command=presionar_no)

boton_si.place(relx=0.3, rely=0.85, anchor="center", width=100, height=40)
boton_no.place(relx=0.7, rely=0.85, anchor="center", width=100, height=40)

# -----------------------------
# Mostramos la primera tarjeta
# -----------------------------
mostrar_tarjeta()

root.mainloop()
