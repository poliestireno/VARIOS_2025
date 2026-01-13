import tkinter as tk

# -----------------------------
# Creamos la ventana principal
# -----------------------------
root = tk.Tk()                 # Ventana principal
root.title("Ejemplo pack()")   # Título de la ventana
root.geometry("400x300")       # Tamaño inicial (ancho x alto)

# -----------------------------
# Etiqueta arriba
# -----------------------------
label_top = tk.Label(
    root,
    text="TOP (arriba)",
    bg="lightblue"
)
# pack() sin indicar nada:
# - se coloca arriba
# - centrada horizontalmente
label_top.pack(side="top", pady=5)

# -----------------------------
# Etiqueta abajo
# -----------------------------
label_bottom = tk.Label(
    root,
    text="BOTTOM (abajo)",
    bg="lightcoral"
)
# side="bottom" → se pega abajo
label_bottom.pack(side="bottom", pady=5)

# -----------------------------
# Etiqueta izquierda
# -----------------------------
label_left = tk.Label(
    root,
    text="LEFT (izquierda)",
    bg="lightgreen"
)
# side="left" → se pega a la izquierda
# fill="y" → se estira verticalmente
label_left.pack(side="left", fill="y", padx=5)

# -----------------------------
# Etiqueta derecha
# -----------------------------
label_right = tk.Label(
    root,
    text="RIGHT (derecha)",
    bg="khaki"
)
# side="right" → se pega a la derecha
# fill="y" → ocupa toda la altura disponible
label_right.pack(side="right", fill="y", padx=5)

# -----------------------------
# Etiqueta central
# -----------------------------
label_center = tk.Label(
    root,
    text="CENTRO\nfill + expand",
    bg="plum"
)
# fill="both" → se estira en horizontal y vertical
# expand=True → ocupa todo el espacio libre
label_center.pack(fill="both", expand=True, padx=10, pady=10)

# -----------------------------
# Bucle principal
# -----------------------------
root.mainloop()
    