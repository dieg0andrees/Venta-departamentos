import misfunciones as mf

while True:
    mf.limpiarpantalla()
    mf.titulo("Venta de departamentos")
    print("""
    1) Ver edificio
    2) Comprar edificio
    3) Buscar dueño
    4) Total de ganancias
    0) Salir
    """)
    opcion = int(input("Seleccione -->"))
    if opcion == 0:
        mf.printVerde("Adios")
        break
    elif opcion == 1:
        mf.titulo("VER EDIFICIO")
    elif opcion == 2:
        mf.titulo("COMPRAR EDIFICIO")
        piso = int(input("Ingrese el piso del departamento -->"))
        ubicacion = input("Ingrese la ubicación del departamento (A,B,C o D) -->").capitalize()
        rut = input("Ingrese su rut (Ej: 12.345.678-9) -->")
        nombre = input("Ingrese su nombre -->").capitalize()
        pago = int(input("Ingrese el monto que usted posee -->"))
        mf.comprarEdificio(piso,ubicacion,rut,nombre,pago)
        print(mf.edificio)

    elif opcion == 3:
        mf.titulo("BUSCAR DUEÑO")
    elif opcion == 4:
        mf.titulo("TOTAL DE GANANCIAS")
    else:
        mf.printERROR("Opción invalida")