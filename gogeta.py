papus = []
cargos = ("CEO","DESARROLADOR","ANALISTA")


def opcion_1():
        print("REGISTRAR TRABAJADOR")
        nombre_apellido = input("Ingrese nombre y apellido: ")
        cargo = int(input("Ingrese cargo(1:CEO, 2:DESARROLLADOR, 3:ANALISTA): "))
        sueldo_solido = int(input("Ingrese sueldo bruto: "))
        desc_salud = int(7/100 * sueldo_solido)
        desc_afp = int(12/100 * sueldo_solido)
        sueldo_liquido = sueldo_solido-desc_afp-desc_salud
        papu = [nombre_apellido,cargos[cargo-1],sueldo_solido,desc_salud,desc_afp]
        papus.append(papu)
        print("TRABAJADOR REGISTRADO CON ÉXITO!")

def opcion_2():
                if len(papus)==0:
                    print("No hay papus :,v")
                else:
                    print("\tLISTA DE TRABAJADORES")
                    print("Trabajador\tCargo\tSueldo Bruto\tDesc. Salud\tDesc. AFP\tLíquido")
                    for t in papus:
                        print(f"{t[0]}\t{t[1]}\t{t[2]}\t\t\t{t[3]}\t\t\t{t[4]}\t{t[5]}")

def opcion_3():
        if len(papus)==0:
            print("No existen trabajadores, elija la opción 1")
        else:
            opc2 = int(input("¿Qué cargo desea imprimit(1:CEO, 2:DESARROLLOR 3:ANALISTA 4:TODOS)"))
            if opc2==4:
                with open("todos_trabajadores.txt","w", newline="\n") as archivo:
                    for t in papus:
                        texto =  f"NOMBRE {t[0]}\nCARGO{t[1]}\nBRUTO {t[2]}\n DESC. SALUD {t[3]}\nDESC. AFP {t[4]}\nLIQUIDO {t[5]}"
                        archivo.write(texto)        
            else:
                with open("trabajadores_por_cargo.txt","w") as archivo:
                    for t in papus:
                        if cargos[opc2-1]==t[1]:
                            texto =  f"NOMBRE {t[0]}\nCARGO{t[1]}\nBRUTO {t[2]}\n DESC. SALUD {t[3]}\nDESC. AFP {t[4]}\nLIQUIDO {t[5]}"
                            archivo.write(texto)
            print("ARCHIVO CREADO CON ÉXITO!")
def opcion_4():
      print("Gracias por usar el programa, bye bye")
      exit()

