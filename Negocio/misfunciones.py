import numpy as np
import msvcrt
import os
from colorama import Fore, Style
import random

#Print Rojo
def printRojo(texto):
    print(f"{Fore.RED}{texto}{Fore.RESET}")

def printVerde(texto):
    print(f"{Fore.GREEN}{texto}{Fore.RESET}")
#Print error
def printERROR(texto):
    print(f"{Fore.RED}{Style.BRIGHT}{texto}{Fore.RESET}{Style.RESET_ALL}")

#Funcion limpiar pantalla
def limpiarPantalla():
    printRojo("<<Presiona una tecla para continuar>>")
    msvcrt.getch()
    os.system("cls")

#CREAMOS EL ARREGLO DEL NEGOCIO
filas = 10
negocio = np.empty([filas,5],object)

def validarCodigo(codigo):
    for i in range(filas):
        if negocio[i,0] == codigo:
            return i
    return -1
    
def guardarProducto(codigo,nombre,descripcion,stock,precio):
    if None in negocio:
        if validarCodigo(codigo) < 0:
            if len(nombre) >=3:
                if stock >= 0:
                    if precio >= 0:
                        for i in range(filas):
                            if negocio[i,0] == None:
                                negocio[i,0] = codigo
                                negocio[i,1] = nombre
                                negocio[i,2] = descripcion
                                negocio[i,3] = stock
                                negocio[i,4] = precio
                                printVerde(f"Producto {nombre} guardado con exito")
                                break
                    else:
                        printERROR("El precio debe ser mayor o igual a 0")
                else:
                    printERROR("El stock debe ser mayor o igual a 0")
            else:
                printERROR("El nombre debe tener por lo menos 3 caracteres")
        else:
            printERROR("El codigo ya existe. Intente con otro")
    else:
        printERROR("No hay espacio disponible")

def listarProductos():
     cant_stock = 0
     for i in range(filas):
        cant_stock = negocio[i,3]
        if cant_stock != None:
            printRojo(f"{i+1}.- Codigo: {negocio[i,0]} | Nombre: {negocio[i,1]} | Descripcion: {negocio[i,2]} | Stock: {negocio[i,3]} | Precio: {negocio[i,4]}")
            

opiniones = []
opiniones.append("Producto muy bueno")
opiniones.append("No lo recomiendo comprar")
opiniones.append("Es el peor producto que he comprado")
opiniones.append("Despues de conocer este producto, mi vida cambió")
opiniones.append("Producto muy infravalorado")
opiniones.append("Este producto tiene las 3 B")
opiniones.append("No pierdan dinero con este producto")
opiniones.append("El peor producto de este negocio")
opiniones.append("Producto más caro de lo normal")
opiniones.append("Cumple con lo solicitado")

def imprimirCertificados(codigo):
    indice = validarCodigo(codigo)
    if indice >=0 :
        print(f"""
        --------------------------------
             Opiniones del producto
        --------------------------------
        Codigo: {negocio[indice,0]} | Nombre: {negocio[indice,1]}
        Opinion 1: {opiniones[random.randint(0,9)]}
        Opinion 2: {opiniones[random.randint(0,9)]}
        Opinion 3: {opiniones[random.randint(0,9)]}
        Opinion 4: {opiniones[random.randint(0,9)]}
        Opinion 5: {opiniones[random.randint(0,9)]}
        """)
    else:
        printERROR("Certificado no encontrado")
