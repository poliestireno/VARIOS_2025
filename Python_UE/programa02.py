import tkinter as tk

ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("200x400")
entrada1 = tk.Entry(ventana)
entrada1.pack(pady=20)
entrada2 = tk.Entry(ventana)
entrada2.pack()


def sumar():
    s1 = entrada1.get()
    s2 = entrada2.get()
    resultado = int(s1) + int(s2)
    etiqueta4.config(text=resultado)
def restar():
    s1 = entrada1.get()
    s2 = entrada2.get()
    resultado = int(s1) - int(s2)
    etiqueta4.config(text=resultado)
def unir():
    s1 = entrada1.get()
    s2 = entrada2.get()
    resultado = s1 + s2
    etiqueta4.config(text=resultado)

boton1 = tk.Button(ventana, text="+", command=sumar)
boton1.pack(pady=10)
boton2 = tk.Button(ventana, text="-", command=restar)
boton2.pack(pady=10)
boton3 = tk.Button(ventana, text="unir", command=unir)
boton3.pack(pady=10)
etiqueta3 = tk.Label(ventana, text="Resultado:")
etiqueta3.pack()
etiqueta4 = tk.Label(ventana, text="0")
etiqueta4.pack()

ventana.mainloop()


