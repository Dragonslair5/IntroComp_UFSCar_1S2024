#!/usr/bin/python3
# *************************************************************************
#  ____ _____ ____ ___ _   _   ____  _____ ____ ___ ____  _____ ____ _____ 
# / ___|_   _|  _ \_ _| \ | | |  _ \| ____|  _ \_ _|  _ \| ____/ ___|_   _|
# \___ \ | | | | | | ||  \| | | |_) |  _| | | | | || |_) |  _|| |     | |  
#  ___) || | | |_| | || |\  | |  _ <| |___| |_| | ||  _ <| |__| |___  | |  
# |____/ |_| |____/___|_| \_| |_| \_\_____|____/___|_| \_\_____\____| |_|  
#                                                                          
# *************************************************************************


pontos = []
while True:
    ponto = input()
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