#EF1_Daví Lucas.py

def velcorpo (raio, ang, intemp):
    return raio*ang/intemp
    
def acentr (velocidade, raio):
    return velocidade*velocidade/raio
    
while(True):
    print("----Velocidade e aceleração de um corpo em MRU----\n")
    dang=float(input("Digite o deslocamento angular(rad):  "))
    r=float(input("Digite o raio da trajetória(m):  "))
    temp=float(input("Digite o intervalo de tempo(s):  "))
    vel=velcorpo(r,dang,temp)
    print("A velocidade do corpo é %g m/s"% vel)
    print("A aceleração centrípeta do corpo é %g m/s²"% acentr(vel, r))
    op=input("\nDigite [Enter] para repetir ou outra tecla pra sair: \n")
    if op!="":
        break
