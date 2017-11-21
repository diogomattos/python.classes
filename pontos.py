import math

x1 = float(input("Digite o ponto X inicial do trajeto: "))
y1 = float(input("Digite o ponto Y inicial do trajeto: "))
x2 = float(input("Digite o ponto X final do trajeto: "))
y2 = float(input("Digite o ponto Y final do trajeto: "))

pontoA = x2-x1 
pontoB = y2-y1

distancia = (math.sqrt(pontoA*pontoA + pontoB*pontoB))

if (distancia >= 10):
    print("longe")
else:
    print("perto")
