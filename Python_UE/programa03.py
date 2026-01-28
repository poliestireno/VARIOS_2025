import tkinter as tk

ventana = tk.Tk()
ventana.title("Elementos")
ventana.geometry("300x400")

esCara = tk.BooleanVar()
mi_check = tk.Checkbutton(ventana,text="Cara de moneda",variable=esCara)
mi_check.pack()
level = tk.StringVar()
mi_radioButton1 = tk.Radiobutton(ventana,text="nivel 1",variable=level,value="nivel 1")
mi_radioButton1.pack()
mi_radioButton2 = tk.Radiobutton(ventana,text="nivel 2",variable=level,value="nivel 2")
mi_radioButton2.pack()
mi_radioButton3 = tk.Radiobutton(ventana,text="nivel 3",variable=level,value="nivel 3")
mi_radioButton3.pack()

def mostrar():
    s1 = esCara.get()
    nivel = level.get()
    resultado.config(text=str(s1)+" "+nivel)

boton1 = tk.Button(ventana, text="mostrar", command=mostrar)
boton1.pack(pady=10)
resultado = tk.Label(ventana, text="")
resultado.pack()
ventana.mainloop()