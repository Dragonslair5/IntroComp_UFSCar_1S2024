#!/usr/bin/python3
# ***************************
#  ____ _____ ____ ___ _   _ 
# / ___|_   _|  _ \_ _| \ | |
# \___ \ | | | | | | ||  \| |
#  ___) || | | |_| | || |\  |
# |____/ |_| |____/___|_| \_|
#                            
# ***************************

print("Escreva as coordenadas dos pontos (X,Y) separados por um espaco. Escreva P apos escrever todos os pontos")

pontos = []
while True:
    ponto = input("Novo ponto (X Y), ou P para parar: ")
    if ponto == "P":
        break
    ponto = ponto.split(" ");
    ponto[0] = int(ponto[0])
    ponto[1] = int(ponto[1])
    pontos.append(ponto)

pontos.append(pontos[0])

Area = 0

for i in range(len(pontos)-1):
    determinante = pontos[i][0]*pontos[i+1][1] - pontos[i][1]*pontos[i+1][0]
    Area += determinante

Area = Area / 2

if Area < 0:
    Area = Area * -1

print("Area: " + str(Area))