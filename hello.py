#ER2_Daví Lucas.py

from math import pi
import math
while True:
    print("----Força = módulo * cos(ângulo)----")
    n=int(input("Digite o número de contas que serão usadas para caucular a força resultante: "))
    N=n+1
    fr=0
    for i in range(1,N,+1):
        modulo=float(input("Digite o %i° modulo da força(N): "%i))
        angulo=float(input("Digite o %i° angulo(graus): "%i))
        rad=angulo*pi/180
        v=modulo*math.cos(rad)
        fr+=v
    print("A força resultante é de %g"%fr)
    op=input("Digite [s] pra sair ou outra tecla pra continuar: ")
    if op=='s'or op=='S':   #o outro é elif
        break


