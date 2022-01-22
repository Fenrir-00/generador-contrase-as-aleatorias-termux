import sys
from sys import *
import os as termux
from os import *
import os
import time
import random
from io import *
class color:
    morado = '\033[95m'
    blanco = '\033[97m'
    cyan = '\033[96m'
    azul  = '\033[94m'
    verde = '\033[92m'
    amarillo = '\033[93m'
    rojo = '\033[91m'
    fin = '\033[0m'

def banner():
 termux.system("clear")
 print(f"""{color.cyan}
███████╗███████╗███╗░░██╗██████╗░██╗██████╗░
██╔════╝██╔════╝████╗░██║██╔══██╗██║██╔══██╗
█████╗░░█████╗░░██╔██╗██║██████╔╝██║██████╔╝
██╔══╝░░██╔══╝░░██║╚████║██╔══██╗██║██╔══██╗
██║░░░░░███████╗██║░╚███║██║░░██║██║██║░░██║
╚═╝░░░░░╚══════╝╚═╝░░╚══╝╚═╝░░╚═╝╚═╝╚═╝░░╚═╝""")
 print(f"{color.fin}")
banner()
carga1="""Loading…
█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒"""
carga2="""Loading…10%
███▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒"""
carga3="""Loading…30%
█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒"""
carga4="""Loading…50%
██████████▒▒▒▒▒▒▒▒▒"""
carga5="""Loading…70%
█████████████▒▒▒▒▒▒"""
carga6="""Loading…100%
███████████████████"""
#termux.system(f"echo '{var}' >cuaderno.txt")
letras =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
letrasm =['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numeros = ['1','2','3','4','5','6','7','8','9','0']
simbolos = ['.',',',':','!','?','#']
contraseña =(random.choice(letras))+(random.choice(letras))+(random.choice(numeros))+(random.choice(letrasm))+(random.choice(simbolos))+(random.choice(numeros))+(random.choice(letrasm))+(random.choice(letrasm))+(random.choice(numeros))+(random.choice(letras))+(random.choice(numeros))+(random.choice(letras))+(random.choice(letrasm))+(random.choice(numeros))+(random.choice(letras))+(random.choice(letrasm))+(random.choice(numeros))+(random.choice(letras))
plataforma =input(f"{color.verde}PARA QUE PLATAFORMA ES LA CONTRASEÑA >>> ")
usuario =input("ELIGE UN USUARIO PUEDE SER TU EMAIL >>> ")
vidas = input("QUE LARGURA DE CONTRASEÑA QUIERES >>> ")
vidas = int(vidas)
if vidas >= 19:
 print("")
 print(f"{color.rojo}LARGURA MAXIMA EXCEDIDA PASARA A SER DE 18{color.fin}")
 time.sleep(3)
elif vidas < 5:
 print("")
 print(f"{color.rojo}POR SEGURIDAD LARGURA MINIMA PASARA A SER DE  5 {color.fin}")
 time.sleep(3)
 vidas = 5
largura = 0
con = ""
for i in contraseña:
 if vidas > largura:
  con = con +(i)
  largura +=1
termux.system("clear")
banner()
print(f"{color.verde}",(carga1))
time.sleep(2)
os.system("clear")
banner()
print(f"{color.verde}",(carga2))
time.sleep(2)
os.system("clear")
banner()
print(f"{color.verde}",(carga3))
time.sleep(2)
os.system("clear")
banner()
print(f"{color.verde}",(carga4))
time.sleep(2)
os.system("clear")
banner()
print(f"{color.verde}",(carga5))
time.sleep(2)
os.system("clear")
banner()
print(f"{color.verde}",(carga6))
time.sleep(2)
os.system("clear")
banner()
print("")
print(f"{color.azul}TU PLATAFORMA ES : "+f"{color.amarillo}" + (plataforma) +f"{color.fin}")
print(f"{color.azul}TU USUARIOS ES : "+f"{color.amarillo}" + (usuario) +f"{color.fin}")
print(f"{color.azul}TU CONTRASEÑA ES : " + f"{color.amarillo}" + (con) +f"{color.fin}")
print("")
print(f"{color.verde}TU CONTRASEÑA SE GUARDO EN CONTRASEÑA.TX {color.fin}")
salto = "\n"
fd = open("contraseña.txt","a")
fd.write(f"PLATAFORMA: {plataforma} {salto}TU USUARIO ES : {usuario} {salto}TU CONTRASEÑA ES: {con}{salto}")
fd.close()
