import os, time
papus = []
while True:
    os.system('cls')
    print("MENÚ TRABAJADORES")
    print("1. Registrar trabajador\n2. Listar todos los trabajadores\n3. Imprimir planilla de sueldos\n 4. Sair del programa")
    opc = int(input("Ingrese opción: "))
    os.system('cls')
    if opc==1:
        print("REGISTRAR TRABAJADOR")
        nombre_apellido = input("Ingrese nombre y apellido: ")
        cargo = int(input("Ingrese cargo(1:CEO, 2:DESARROLLADOR, 3:ANALISTA): "))
        sueldo_solido = int(input("Ingrese sueldo bruto: "))
        desc_salud = int(7/100 * sueldo_solido)
        desc_afp = int(12/100 * sueldo_solido)
        sueldo_liquido = sueldo_solido-desc_afp-desc_salud
        papu = [nombre_apellido,cargo,sueldo_solido,desc_salud,desc_afp]
        papus.append(papu)
        print("TRABAJADOR REGISTRADO CON ÉXITO!")
 
    elif opc==2:
        if len(papus)==0:
            print("No hay papus :,v")
        else:
            print("\tLISTA DE TRABAJADORES")
            print("Trabajador\tCargo\tSueldo Bruto\tDesc. Salud\tDesc. AFP\tLíquido")
            for t in papus:
                 print(f"{t[0]}\t{t[1]}\t{t[2]}\t\t\t{t[3]}\t\t\t{t[4]}\t{t[5]}")


    elif opc==3:
        if len(papus)==0:
            print("No existen trabajadores, elija la opción 1")
        else:
            opc2 = int(input("¿Qué cargo desea imprimit(1:CEO, 2:DESARROLLOR 3:ANALISTA 4:TODOS)"))
            if opc2==4:
                with open("todos_trabajadores.txt","w", newline="\n") as archivo:
                    for t in papus:
                        texto =  f"{t[0]} {t[1]} {t[2]} {t[3]} {t[4]} {t[5]}"
                        archivo.write(texto)        
            else:
                with open("trabajadores_por_cargo.txt","w") as archivo:
                    for t in papus:
                        if opc2==t[1]:
                            texto =  f"{t[0]} {t[1]} {t[2]} {t[3]} {t[4]} {t[5]}"
                            archivo.write(texto)
            print("ARCHIVO CREADO CON ÉXITO!")
    else:
        print("Gracias por usar el programa, bye bye")
        break
    time.sleep(3)