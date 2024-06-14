import os, time
from gogeta import *
while True:
    os.system('cls')
    print("MENÚ TRABAJADORES")
    print("1. Registrar trabajador\n2. Listar todos los trabajadores\n3. Imprimir planilla de sueldos\n 4. Sair del programa")
    opc = int(input("Ingrese opción: "))
    os.system('cls')
    if opc==1:
       opcion_1()
    elif opc==2:
        opcion_2()
    elif opc==3:
        opcion_3() 
    else:
       opcion_4()
    time.sleep(3)