import tkinter as tk
from tkinter import messagebox

ventana = tk.Tk()
ventana.title("Saludo")
ventana.geometry("300x300")
def abrir_ventana_secundaria():
    ventana_sec = tk.Toplevel(ventana)
    ventana_sec.title("Ventana secundaria")
    ventana_sec.geometry("250x150")
    tk.Label(ventana_sec,text="esto es una ventana secundaria").pack(pady=20)
    tk.Button(ventana_sec,text="Close",command=ventana_sec.destroy).pack()
def mi_salir():
    ventana.destroy()
def mostrar_info():
    messagebox.showinfo("Info","Pertenece a UE")
    messagebox.showerror("Mal","error fatal")
    messagebox.showwarning("Cuidado","suelo mojado")
def mi_seleccion(miLista):
    da error, ver como pasar el parametro milista.
    messagebox.showinfo("Info","Entrando")
    #sel = milista.curselection()
    #if sel: 
    #    indice = sel[0]
    #    texto = milista.get(indice)
    #    messagebox.showinfo("Info",f" el texto es {texto}")
    

def mi_lista():
    ventana_sec2 = tk.Toplevel(ventana)
    ventana_sec2.title("La lista de turno")
    ventana_sec2.geometry("250x250")
    lista = tk.Listbox(ventana_sec2,height=4)
    lista.pack(pady=40)
    lista.insert(tk.END,"Agua")
    lista.insert(tk.END,"Tierra")
    lista.insert(tk.END,"Aire")
    lista.insert(tk.END,"Fuego")
    tk.Button(ventana_sec2,text="mi selección es",command=mi_seleccion(lista)).pack(pady=15)
    
    
    
menu_barra = tk.Menu(ventana)
ventana.config(menu=menu_barra)
menu_archivo = tk.Menu(menu_barra,tearoff=0)
menu_barra.add_cascade(label="Archivo",menu=menu_archivo)
menu_archivo.add_command(label="Abrir ventana",command=abrir_ventana_secundaria)
menu_archivo.add_separator()
menu_archivo.add_command(label="Lista",command=mi_lista)
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir",command=mi_salir)
menu_ayuda = tk.Menu(menu_barra,tearoff=0)
menu_barra.add_cascade(label="Ayuda",menu=menu_ayuda)
menu_ayuda.add_command(label="Acerca de",command=mostrar_info)






ventana.mainloop()