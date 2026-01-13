print("Piensa un número entre 0 y 7 (no lo digas)")
resultado = 0

# Tarjeta 1: números con 1 en el primer “patrón”
tarjeta1 = [1, 3, 5, 7]
print("Tarjeta 1:", tarjeta1)
respuesta = input("¿Está tu número aquí? (s/n): ")
if respuesta == "s":
    resultado += 1

# Tarjeta 2: números con 1 en el segundo “patrón”
tarjeta2 = [2, 3, 6, 7]
print("Tarjeta 2:", tarjeta2)
respuesta = input("¿Está tu número aquí? (s/n): ")
if respuesta == "s":
    resultado += 2

# Tarjeta 3: números con 1 en el tercer “patrón”
tarjeta3 = [4, 5, 6, 7]
print("Tarjeta 3:", tarjeta3)
respuesta = input("¿Está tu número aquí? (s/n): ")
if respuesta == "s":
    resultado += 4

print("El número que estás pensando es:", resultado)
