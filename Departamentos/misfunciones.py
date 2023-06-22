#Funciones de color y titulo
from colorama import Fore, Style
import numpy
import msvcrt
import os
import random

#Funciones de diseño
def printRojo(texto):
    print(F"{Fore.RED}{texto}{Fore.RESET}")

def printERROR(texto):
    print(F"{Fore.RED}{Style.BRIGHT}{texto}{Fore.RESET}{Style.RESET_ALL}")

def printVerde(texto):
    print(F"{Fore.GREEN}{texto}{Fore.RESET}")

def printAmarillo(texto):
    print(F"{Fore.YELLOW}{texto}{Fore.RESET}")

def printAzul(texto):
    print(F"{Fore.BLUE}{texto}{Fore.RESET}")

def titulo(texto):
    printRojo("_________________________________")
    printAzul(f"**{texto}")
    printRojo("_________________________________")

def limpiarpantalla():
    printRojo("<<PRESS ANY KEY TO CONTINUE>>")
    msvcrt.getch()
    os.system("cls")

#Funciones operacionales
filas = 10
columnas = 4
edificio = numpy.empty([filas, columnas], object)

def verEdificio():
    pass

def comprarEdificio(piso,ubicacion,rut,nombre,pago):
    if ubicacion == "A":
        ubicacion = 0
    elif ubicacion == "B":
        ubicacion = 1
    elif ubicacion == "C":
        ubicacion = 2
    elif ubicacion == "D":
        ubicacion = 3
    if None in edificio:
        if piso >=8 and piso <=10:
            if pago >=200000000:
                for i in range(piso):
                    for j in range (ubicacion):
                        if edificio[i,j] == None:
                            edificio[i,j] = piso, ubicacion, rut, nombre, pago
                            printVerde("Departamento comprado con exito!")
                            break
        else:
            if pago >=150000000:
                for i in range(piso):
                    for j in range (ubicacion):
                        if edificio[i,j] == None:
                            edificio[i,j] = piso, ubicacion, rut, nombre, pago
                            printVerde("Departamento comprado con exito!")
                            break
            else:
                printERROR("Monto insuficiente")
    else:
        printERROR("No hay departamentos disponibles")