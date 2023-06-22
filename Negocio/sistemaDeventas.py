import misfunciones as mf
import os
while True:
    mf.limpiarPantalla()
    print("""
    --------------------------------------
              Sistema de negocio
    --------------------------------------
    1) Registrar Producto
    2) Listar Productos
    3) Imprimir Certificados
    0) Salir
    """)
    opcion = int(input("Seleccione -->"))
    os.system("cls")
    
    if opcion == 0:
        break
    elif opcion == 1:
        mf.printRojo("REGISTRAR PRODUCTO")
        codigo = int(input("Ingrese codigo del producto -->"))
        nombre = input("Ingrese nombre del producto -->").capitalize()
        descripcion = input("Ingrese descripcion del producto -->").capitalize()
        stock = int(input("Ingrese stock del producto -->"))
        precio = int(input("Ingrese precio del producto -->"))
        mf.guardarProducto(codigo,nombre,descripcion,stock,precio)
    elif opcion == 2:
        mf.printRojo("LISTAR PRODUCTOS")
        mf.listarProductos()
    elif opcion ==3:
        mf.printRojo("IMPRIMIR CERTIFICADOS")
        codigo = int(input("Ingrese codigo del producto -->"))
        mf.imprimirCertificados(codigo)
    else:
        mf.printERROR("OPCION NO VALIDA")