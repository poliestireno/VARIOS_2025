import math
def sigmoide(x):
    if x>=0:
        return 1
    else:
        return 0

def sigmoideReal(x):
    return 1 / (1 + math.exp(-x))

peso_nota = 1
peso_asistencia = 0.3
bias = -0.5

nota = 4.0
asistencia = 80

nota_n = nota /10
asistencia_n = asistencia / 100

z = nota_n * peso_nota + asistencia_n * peso_asistencia + bias

salida = sigmoideReal(z)

print(f"z: {z}")
print(f"salida: {salida}")
if (salida>0.5):
    print("APROBADO")
else:
    print("SUSPENSO")
