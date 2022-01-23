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

#barra de carga
def carga():
    print(f"{color.verde}")
    print("""Loading…
    █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒""")
    time.sleep(1)
    os.system("clear")
    banner()
    print(f"{color.verde}")
    print("""Loading…10%
    ███▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒""")
    time.sleep(1)
    os.system("clear")
    banner()
    print(f"{color.verde}")
    print("""Loading…30%
    █████▒▒▒▒▒▒▒▒▒▒▒▒▒▒""")
    time.sleep(1)
    os.system("clear")
    banner()
    print(f"{color.verde}")
    print("""Loading…50%
    ██████████▒▒▒▒▒▒▒▒▒""")
    time.sleep(1)
    os.system("clear")
    banner()
    print(f"{color.verde}")
    print("""Loading…70%
    █████████████▒▒▒▒▒▒""")
    time.sleep(1)
    os.system("clear")
    banner()
    print(f"{color.verde}")
    print("""Loading…100%
    ███████████████████""")
    time.sleep(1)
    os.system("clear")
    banner()

#menu principal    

def menu():
    os.system("clear")
    banner()
    carga()
    print(f"{color.verde}QUE TE GUSTARIA HACER")
    print("")
    print(f"{color.amarillo}[1]GENERAR CONTRASEÑA")
    print("[2]VER CONTRASEÑAS")
    print(f"{color.rojo}[3]BORRA TODAS LAS CONTRASEÑAS")
    print(f"[4]SALIR{color.fin}")
    eleccion =int(input("ELIJE UN NUMERO >> "))
    if eleccion == 1 :
        banner()
        generar()

    elif eleccion == 2 :
        banner()
        leer()
        time.sleep(5)
        menu()
    elif eleccion == 3 :
     banner()
     borrar()
    elif eleccion == 4 :
     banner()
     salir()
    else:
        incorrecto()
           
def incorrecto():
    banner()
    print(f"¨{color.rojo}OPCION INCORRECTA{color.fin}")
    time.sleep(3)
    menu()


#leer contraseña 
def leer(): 
 print(f"{color.morado} TUS CONTRASEÑAS{color.verde}")
 print("")
 fd = open("contraseña.txt","r")
 leer = fd.read()
 print(leer)
 fd.close()
 time.sleep(5)
 print(f"{color.fin}")
#borrar 
def borrar():
    fd = open("contraseña.txt","w")
    fd.write("") 
    fd.close()
    print(f"{color.rojo} CONTRASEÑAS BORRADAS{color.fin}")
    time.sleep(3)
    menu()


# salir


def salir(): 
    os.system("clear")
    banner()
    print(f"{color.rojo}")
    print("""SALIENDO…
    █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒""")
    time.sleep(1)
    os.system("clear")
    banner()
    print(f"{color.rojo}")
    print("""SALIENDO…10%
    ███▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒""")
    time.sleep(1)
    os.system("clear")
    banner()
    print(f"{color.rojo}")
    print("""SALIENDO…30%
    █████▒▒▒▒▒▒▒▒▒▒▒▒▒▒""")
    time.sleep(1)
    os.system("clear")
    banner()
    print(f"{color.rojo}")
    print("""SALIENDO…50%
    ██████████▒▒▒▒▒▒▒▒▒""")
    time.sleep(1)
    os.system("clear")
    banner()
    print(f"{color.rojo}")
    print("""SALIENDO…70%
    █████████████▒▒▒▒▒▒""")
    time.sleep(1)
    os.system("clear")
    banner()
    print(f"{color.rojo}")
    print("""SALIENDO…100%
    ███████████████████""")
    time.sleep(1)
    os.system("clear")
    sys.exit()

# generador de contraseña
def generar(): 
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
    carga()
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
    fd.write(f"PLATAFORMA: {plataforma} {salto}TU USUARIO ES : {usuario} {salto}TU CONTRASEÑA ES: {con}{salto}{salto}")
    fd.close()
menu()
