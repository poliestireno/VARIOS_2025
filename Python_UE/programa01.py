import tkinter as tk

ventana = tk.Tk()
ventana.title("Hola")
ventana.geometry("300x200")
etiqueta = tk.Label(ventana, text="Hola mundo")
etiqueta.pack()
etiqueta2 = tk.Label(ventana, text="Viva Viva")
etiqueta2.pack()
entrada1 = tk.Entry(ventana)
entrada1.pack(pady=20)

def saludar():
    nombre = entrada1.get()
    etiqueta3.config(text=nombre)


boton1 = tk.Button(ventana, text="Dame", command=saludar)
boton1.pack(pady=10)
etiqueta3 = tk.Label(ventana, text="")
etiqueta3.pack()

ventana.mainloop()


