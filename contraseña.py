from googlesearch import search
import sys
from sys import *
import os as termux
from os import *
import os
import threading
import time
import requests
import traceback
import string
import random
from contextlib import suppress
from binance.exceptions import *
from binance.client import Client
from binance.enums import *
from binance.helpers import round_step_size
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
 print(f"{color.azul}")
 print( """       ##############################""")
 print( """       # ____ ____ _  _ ____ _ ____ #""")
 print( """       # |___ |___ |\ | |__/ | |__/ #""")
 print( """       # |    |___ | \| |  \ | |  \ #""")
 print( """       #                            #""")
 print( """       #          CONTRASEÑA        #""")
 print( """       ##############################""")
 print(f"{color.fin}")
banner()
#termux.system(f"echo '{var}' >cuaderno.txt")
letras =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
letrasm =['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numeros = ['1','2','3','4','5','6','7','8','9','0']
simbolos = ['.',',',':','!','?','#']
contraseña =(random.choice(letras))+(random.choice(letras))+(random.choice(numeros))+(random.choice(letrasm))+(random.choice(simbolos))+(random.choice(numeros))+(random.choice(letrasm))+(random.choice(letrasm))+(random.choice(numeros))+(random.choice(letras))+(random.choice(numeros))+(random.choice(letras))+(random.choice(letrasm))+(random.choice(numeros))+(random.choice(letras))+(random.choice(letrasm))+(random.choice(numeros))+(random.choice(letras))
usuario =input("ELIGE UN USUARIO>>> ")
vidas = input("QUE LARGURA DE CONTRASEÑA QUIERES>>> ")
vidas = int(vidas)
if vidas >= 18:
 print(f"{color.rojo}LARGURA MAXIMA EXCEDIDA PASARA A SER DE 18{color.fin}")
elif vidas < 5:
 print("LARGURA MINIMA PASARA A SER DE  5 ")
 vidas = 5
largura = 0
con = ""
for i in contraseña:
 if vidas > largura:
  con = con +(i)
  largura +=1
termux.system("clear")
banner()
print("")
print(f"{color.azul}TU USUARIOS ES : "+f"{color.amarillo}" + (usuario) +f"{color.fin}")
print(f"{color.azul}TU CONTRASEÑA ES : " + f"{color.amarillo}" + (con) +f"{color.fin}")
salto = "\n"
termux.system(f"echo 'TU USUARIO ES : ''{usuario}' '{salto}''TU CONTRASENA ES : ''{con}' >contraseña.txt")
