import numpy as np
import os 
import msvcrt
from colorama import Fore, Style

#Creamos el arreglo
productos = np.empty([10,5], object)

#Texto rojo
def printr(texto):
    print(f"{Fore.RED}{texto}{Fore.RESET}")

#Texto verde
def printv(texto):
    print(f"{Fore.GREEN}{texto}{Fore.RESET}")

#Texto amarillo
def printa(texto):
    print(f"{Fore.YELLOW}{texto}{Fore.RESET}")

#Texto verde y negrita
def printvv(texto):
    print(f"{Fore.GREEN}{Style.BRIGHT}{texto}{Style.RESET_ALL}{Fore.RESET}")



#Detener y limpar pantalla
def limpiarpantalla():
    printa("<<PRESS ANY KEY TO CONTINUE>>")
    msvcrt.getch()
    os.system("cls")
#Funcion para verificar que el cod no exista 
def validarCodigo(cod):
    for i in range(10):
        if productos[i,0] == cod:
            return i #Retorno la posición donde se encuentra el cod repetido
    return -1 #Significa que el código no está


#Guaradar en el arreglo
def guardar(cod,nom,desc,prec,stock):
    if None in productos: #validamos que haya espacio
        if validarCodigo(cod) == -1: #Validamos que no este repetido
            if len(nom)>=3:
                if prec >0:
                    if stock >0:
                        for i in range (10): #Buscamos donde hay un none
                            if productos[i,0] == None: #Si lo encontramos lo guardamos
                                productos[i,0] = cod
                                productos[i,1] = nom
                                productos[i,2] = desc
                                productos[i,3] = prec
                                productos[i,4] = stock
                                printv("Producto registrado")
                                break
                    else:
                        printr("El stock deber ser mayor a 0")
                else:
                    printr("El precio debe ser mayor a 0")
            else:
                printr("El nombre debe tener por lo menos 3 caracteres")
        else:
            printr("Codigo repetido")
    else:
        print("No hay espacio")


def listar():
    print(productos)


guardar(1, "Papas", "Papas muy ricas",700,5)
guardar(1, "Papas", "Papas muy ricas",700,5)
guardar(2, "Coca-Cola", "Bebida refrescante",1550,5)

