import math
def sigmoide(x):
    if x>=0:
        return 1
    else:
        return 0

def sigmoideReal(x):  # cualquier x lo pasa a entre 0 y 1
    return 1 / (1 + math.exp(-x))

peso_nota = 1
peso_asistencia = 0.3
bias = -0.5 # Es una tendencia inicial de la neurona,empujón inicial. Desplaza la decisión hacia aprobado o suspenso. Hace aprobar o suspender más fácil o más difícil.

#nota = 3.0
#asistencia = 80

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

datos = [
    [4.0,80,0],
    [4.5,80,0],
    [4.76,80,0],
    [5.0,80,1],
    [5.1,80,1],
    [6.5,80,1]
]

learning_rate = 0.1
epocas = 10000
for _ in range(epocas):
    for nota, asistencia,esperado in datos:
        nota_n = nota /10 # 0-1
        asistencia_n = asistencia / 100 # 0-1
        z = nota_n * peso_nota + asistencia_n * peso_asistencia + bias
        salida = sigmoideReal(z)
        error = esperado - salida
        print(f"error: {error}")
        peso_nota = peso_nota + error * nota_n * learning_rate
        peso_asistencia = peso_asistencia + error * asistencia_n * learning_rate
        bias = bias + error * learning_rate

print(f"peso_nota: {peso_nota}")
print(f"peso_asistencia: {peso_asistencia}")
print(f"bias: {bias}")


nota = 3
asistencia = 80
nota_n = nota /10 # 0-1
asistencia_n = asistencia / 100 # 0-1
z = nota_n * peso_nota + asistencia_n * peso_asistencia + bias
salida = sigmoideReal(z)
print(f"nota: {nota}")
print(f"asistencia: {asistencia}")
if (salida>0.5):
   print("APROBADO")
else:
  print("SUSPENSO")