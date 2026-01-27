# =================================================================
# DEMOSTRACIÓN DE WIDGETS DE SELECCIÓN Y VARIABLES DINÁMICAS
# =================================================================

import tkinter as tk

# ---------------- CONFIGURACIÓN DE LA VENTANA ----------------
# Creamos la instancia principal de la aplicación (el contenedor raíz)
ventana = tk.Tk()
# Definimos el título que aparecerá en la barra superior
ventana.title("Tkinter - Paso 3")
# Ajustamos el tamaño inicial: ancho x alto en píxeles
ventana.geometry("300x320")

# ---------------- ETIQUETA DE TÍTULO ----------------
# Un widget Label sirve para mostrar texto estático o dinámico
etiqueta = tk.Label(ventana, text="Selecciona tus opciones")
# .pack() posiciona el widget; 'pady' añade margen vertical (arriba/abajo)
etiqueta.pack(pady=10)

# ---------------- SECCIÓN: CHECKBUTTON (Casilla de verificación) ----------------
# Creamos una variable especial de Tkinter para rastrear el estado del Checkbutton.
# BooleanVar es ideal para valores lógicos: True (marcado) o False (desmarcado).
opcion_python = tk.BooleanVar()

# Creamos el widget Checkbutton
check_python = tk.Checkbutton(
    ventana,
    text="Me gusta Python",   # El texto que ve el usuario
    variable=opcion_python    # Enlazamos el widget con nuestra variable BooleanVar
)
# 'anchor="w"' alinea el texto al Oeste (West/Izquierda)
# 'padx' añade un margen horizontal para que no esté pegado al borde
check_python.pack(anchor="w", padx=20)

# ---------------- SECCIÓN: RADIOBUTTONS (Botones de opción única) ----------------
# Para los Radiobuttons usamos StringVar porque queremos almacenar el "texto" de la opción.
# value="" asegura que al inicio no haya ninguna opción seleccionada por defecto.
nivel = tk.StringVar(value="")

# NOTA: Todos los Radiobuttons de un grupo DEBEN compartir la misma 'variable'.
# Lo que los diferencia es el 'value' que cada uno aporta a esa variable.

# Opción 1: Principiante
radio_principiante = tk.Radiobutton(
    ventana,
    text="Principiante",      # Lo que lee el usuario
    variable=nivel,           # Variable donde se guarda la elección
    value="Principiante"      # El valor real que se guardará si se marca
)
radio_principiante.pack(anchor="w", padx=20)

# Opción 2: Intermedio
radio_intermedio = tk.Radiobutton(
    ventana,
    text="Intermedio",
    variable=nivel,
    value="Intermedio"
)
radio_intermedio.pack(anchor="w", padx=20)

# Opción 3: Avanzado
radio_avanzado = tk.Radiobutton(
    ventana,
    text="Avanzado",
    variable=nivel,
    value="Avanzado"
)
radio_avanzado.pack(anchor="w", padx=20)

# ---------------- LÓGICA DE LA APLICACIÓN ----------------
def mostrar_seleccion():
    """
    Esta función se ejecuta cuando el usuario pulsa el botón.
    Extrae los datos de las variables de Tkinter y actualiza la interfaz.
    """
    # .get() es el método para obtener el valor actual almacenado en la variable
    gusta = opcion_python.get()      # Obtiene True o False
    nivel_sel = nivel.get()          # Obtiene el string ("Principiante", "Intermedio", etc.)

    # Construimos un mensaje formateado con los resultados
    texto = f"¿Te gusta Python? {gusta}\nNivel: {nivel_sel}"
    
    # .config() permite cambiar las propiedades de un widget en tiempo de ejecución
    # Aquí actualizamos el texto de la etiqueta de resultado
    etiqueta_resultado.config(text=texto)

# ---------------- BOTÓN DE ACCIÓN ----------------
# Creamos un botón que disparará la función 'mostrar_seleccion'
boton = tk.Button(
    ventana,
    text="Mostrar selección",
    command=mostrar_seleccion  # OJO: Se pasa el nombre de la función sin paréntesis
)
boton.pack(pady=15)

# ---------------- ETIQUETA DE RESULTADO ----------------
# Esta etiqueta empieza vacía y se llenará cuando el usuario pulse el botón
etiqueta_resultado = tk.Label(ventana, text="", fg="blue") # 'fg' cambia el color del texto
etiqueta_resultado.pack()

# ---------------- INICIO DEL BUCLE ----------------
# Mantiene la ventana abierta y escuchando eventos (clics, teclado, etc.)
ventana.mainloop()