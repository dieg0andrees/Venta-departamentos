esp = 1500
cap =1800
la = 1600
moc=1700

import os
import msvcrt

def limpiarpantalla():
    print("Presione una tecla para continuar")
    msvcrt.getch()
    os.system("cls")

def printr(texto):
    print(f"\033[31m{texto}\033[0m")

def printv(texto):
    print(f"\033[32m{texto}\033[0m")

def titulo():
    print(f"""
    SISTEMA DE VENTA CAFÉ
    ---------------------

    1) Espreso   ${esp}
    2) Capuccino ${cap}
    3) Latte     ${la}
    4) Moca      ${moc}
    0) Salir
    """)
    return int(input("Seleccione : "))

def seleccion(opcion):
    if opcion >=1 and opcion<=4:
        cantidad = int(input("Cuantos deseá? -->"))
        if cantidad >0 :
            if opcion == 1:
                print(f"Ustes a seleccionado {cantidad} cafe espresso ")
                return cantidad * esp
            elif opcion ==2:
                print(f"Ustes a seleccionado {cantidad} cafe Capuccino ")
                return cantidad * cap
            elif opcion ==3:
                print(f"Ustes a seleccionado {cantidad} cafe latte ")
                return cantidad * la
            elif opcion ==4:
                print(f"Ustes a seleccionado {cantidad} cafe Moca ")
                return cantidad * moc
        else:
            printr("Opcion no valdia")
            return 0
    else:
        printr("Opcion no valdia")
        return 0

def descuento(total):
    printv(f"Usted tiene un descuento del 10%: ${round(total*0.1)}")
    printv(f"Total a pagar {round(total*0.9)}")
    return round(total * 0.9)