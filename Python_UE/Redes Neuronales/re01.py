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
bias = -0.5 # Es una tendencia inicial de la neurona,empujón inicial. Desplaza la decisión hacia aprobado o suspenso. Hace aprobar o suspender más fácil o más difícil.

nota = 3.0
asistencia = 80

#5.4 APROBADO
#4.6 SUSPENSO
#7.8 APROBADO
#10  APROBADO
#3   SUSPENSO


# 9.1 SOBRE
# 8.8 NO SOBRE
# 10 SOBRE
# 4 NO SOBRE

# 9.2


#if nota >= 5 APROBADO
#else SUSPENSO


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
