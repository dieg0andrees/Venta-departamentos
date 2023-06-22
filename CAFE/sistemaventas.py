import misfunciones as m

total = 0 #Acumulador

while True:
    m.limpiarpantalla
    opcion = m.titulo()
    
    if opcion == 0:
        break
    else:
        total += m.seleccion(opcion)
if total >= 3000:
    total = m.descuento(total)
else:
    m.printv("No tiene descuento")
    m.printv(f"Total a pagar {total}")
    
   