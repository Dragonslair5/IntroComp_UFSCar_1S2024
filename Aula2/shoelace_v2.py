#!/usr/bin/python3
# *****************************
#  _     ___ ____ _____  _    
# | |   |_ _/ ___|_   _|/ \   
# | |    | |\___ \ | | / _ \  
# | |___ | | ___) || |/ ___ \ 
# |_____|___|____/ |_/_/   \_\
#                             
# *****************************

A = [1,1]
B = [5,1]
C = [3,3]

Area = A[0]*B[1] - A[1]*B[0] + B[0]*C[1] - B[1]*C[0] + C[0]*A[1] - C[1]*A[0]
Area = Area / 2

if Area < 0:
    Area = Area * -1

print("Area: " + str(Area))