import csv
import random

trabajadores = ['Juan Pérez', 'María García', 'Carlos López', 'Ana Martínez', 'Pedro Rodríguez', 'Laura Hernández', 'Miguel Sánchez', 'Isabel Gómez', 'Francisco Díaz', 'Elena Fernández']
Sueldos = False

while True:
    print("Opciones:")
    print("1. Asignar sueldos")
    print("2. Clasificar sueldos")
    print("4. Reporte de sueldos")
    print("5. Salir del programa")
    opciones = input("Seleccione una opcion: ")

    if opciones == "1":
        Sueldos = True
        sueldo1 = random.randint(300000, 2500000)
        sueldo2 = random.randint(300000, 2500000)
        sueldo3 = random.randint(300000, 2500000)
        sueldo4 = random.randint(300000, 2500000)
        sueldo5 = random.randint(300000, 2500000)
        sueldo6 = random.randint(300000, 2500000)
        sueldo7 = random.randint(300000, 2500000)
        sueldo8 = random.randint(300000, 2500000)
        sueldo9 = random.randint(300000, 2500000)
        sueldo10 = random.randint(300000, 2500000)

        lista_sueldos = [sueldo1, sueldo2, sueldo3, sueldo4, sueldo5, sueldo6, sueldo7, sueldo8, sueldo9, sueldo10]

        sueldos = {
        trabajadores[0]: sueldo1,
        trabajadores[1]: sueldo2,
        trabajadores[2]: sueldo3,
        trabajadores[3]: sueldo4,
        trabajadores[4]: sueldo5,
        trabajadores[5]: sueldo6,
        trabajadores[6]: sueldo7,
        trabajadores[7]: sueldo8,
        trabajadores[8]: sueldo9,
        trabajadores[9]: sueldo10,
        }

        print("")
        print("")
        print("Sueldos agregados con exito")
        print("")
        print("")

    elif opciones == "2":
       if Sueldos == True:
        print("Sueldos menores a $800.000")
        print("Nombre Empleado   Sueldo")
        print("")
        print("")
        if sueldo1 < 800000:
            print(trabajadores[0], ": ", sueldo1)
        if sueldo2 < 800000:
            print(trabajadores[1], ": ", sueldo2)
        if sueldo3 < 800000:
            print(trabajadores[2], ": ", sueldo3)
        if sueldo4 < 800000:
            print(trabajadores[3], ": ", sueldo4)
        if sueldo5 < 800000:
            print(trabajadores[4], ": ", sueldo5)
        if sueldo6 < 800000:
            print(trabajadores[5], ": ", sueldo6)
        if sueldo7 < 800000:
            print(trabajadores[6], ": ", sueldo7)
        if sueldo8 < 800000:
            print(trabajadores[7], ": ", sueldo8)
        if sueldo9 < 800000:
            print(trabajadores[8], ": ", sueldo9)
        if sueldo10 < 800000:
            print(trabajadores[9], ": ", sueldo10)
        print("")

        print("Sueldos entre $800.000 y $2.000.000")
        print("Nombre Empleado   Sueldo")
        print("")

        if sueldo1 >= 800000 and sueldo1 <= 2000000:
            print(trabajadores[0], ": ", sueldo1)
        if sueldo2 >= 800000 and sueldo2 <= 2000000:
            print(trabajadores[1], ": ", sueldo2)
        if sueldo3 >= 800000 and sueldo3 <= 2000000:
            print(trabajadores[2], ": ", sueldo3)
        if sueldo4 >= 800000 and sueldo4 <= 2000000:
            print(trabajadores[3], ": ", sueldo4)
        if sueldo5 >= 800000 and sueldo5 <= 2000000:
            print(trabajadores[4], ": ", sueldo5)
        if sueldo6 >= 800000 and sueldo6 <= 2000000:
            print(trabajadores[5], ": ", sueldo6)
        if sueldo7 >= 800000 and sueldo7 <= 2000000:
            print(trabajadores[6], ": ", sueldo7)
        if sueldo8 >= 800000 and sueldo8 <= 2000000:
            print(trabajadores[7], ": ", sueldo8)
        if sueldo9 >= 800000 and sueldo9 <= 2000000:
            print(trabajadores[8], ": ", sueldo9)
        if sueldo10 >= 800000 and sueldo10 <= 2000000:
            print(trabajadores[9], ": ", sueldo10)
        print("")

        print("Sueldos superiores a $2.000.000")
        print("Nombre Empleado   Sueldo")
        print("")

        if sueldo1 > 2000000:
            print(trabajadores[0], ": ", sueldo1)
        if sueldo2 > 2000000:
            print(trabajadores[1], ": ", sueldo2)
        if sueldo3 > 2000000:
            print(trabajadores[2], ": ", sueldo3)
        if sueldo4 > 2000000:
            print(trabajadores[3], ": ", sueldo4)
        if sueldo5 > 2000000:
            print(trabajadores[4], ": ", sueldo5)
        if sueldo6 > 2000000:
            print(trabajadores[5], ": ", sueldo6)
        if sueldo7 > 2000000:
            print(trabajadores[6], ": ", sueldo7)
        if sueldo8 > 2000000:
            print(trabajadores[7], ": ", sueldo8)
        if sueldo9 > 2000000:
            print(trabajadores[8], ": ", sueldo9)
        if sueldo10 > 2000000:
            print(trabajadores[9], ": ", sueldo10)
        print("")
       elif Sueldos == False: 
        print("")
        print("Primero hay que asignar sueldos a los empleados")
        print("")

    elif opciones == "4":
       if Sueldos == True:
        Salud1 = sueldo1 * 0.07
        AFP1 = sueldo1 * 0.12
        Sueldo_liquido1 = sueldo1 - round(Salud1) - round(AFP1)
        Trabajador1 = sueldo1, round(Salud1), round(AFP1), Sueldo_liquido1

        Salud2 = sueldo2 * 0.07
        AFP2 = sueldo2 * 0.12
        Sueldo_liquido2 = sueldo2 - round(Salud2) - round(AFP2)
        Trabajador2 = sueldo2,  round(Salud2), round(AFP2), Sueldo_liquido2

        Salud3 = sueldo3 * 0.07
        AFP3 = sueldo3 * 0.12
        Sueldo_liquido3 = sueldo3 - round(Salud3) - round(AFP3)
        Trabajador3 = sueldo3, round(Salud3), round(AFP3), Sueldo_liquido3

        Salud4 = sueldo4 * 0.07
        AFP4 = sueldo4 * 0.12
        Sueldo_liquido4 = sueldo4 - round(Salud4) - round(AFP4)
        Trabajador4 = sueldo4, round(Salud4), round(AFP4), Sueldo_liquido4

        Salud5 = sueldo5 * 0.07
        AFP5 = sueldo5 * 0.12
        Sueldo_liquido5 = sueldo5 - round(Salud5) - round(AFP5)
        Trabajador5 = sueldo5, round(Salud5), round(AFP5), Sueldo_liquido5

        Salud6 = sueldo6 * 0.07
        AFP6 = sueldo6 * 0.12
        Sueldo_liquido6 = sueldo6 - round(Salud6) - round(AFP6)
        Trabajador6 = sueldo6, round(Salud6), round(AFP6), Sueldo_liquido6
        
        Salud7 = sueldo7 * 0.07
        AFP7 = sueldo7 * 0.12
        Sueldo_liquido7 = sueldo7 - round(Salud7) - round(AFP7)
        Trabajador7 = sueldo7, round(Salud7), round(AFP7), Sueldo_liquido7

        Salud8 = sueldo8 * 0.07
        AFP8 = sueldo8 * 0.12
        Sueldo_liquido8 = sueldo8 - round(Salud8) - round(AFP8)
        Trabajador8 = sueldo8, round(Salud8), round(AFP8), Sueldo_liquido8

        Salud9 = sueldo9 * 0.07
        AFP9 = sueldo9 * 0.12
        Sueldo_liquido9 = sueldo9 - round(Salud9) - round(AFP9)
        Trabajador9 = sueldo9, round(Salud9), round(AFP9), Sueldo_liquido9

        Salud10 = sueldo10 * 0.07
        AFP10 = sueldo10 * 0.12
        Sueldo_liquido10 = sueldo10 - round(Salud10) - round(AFP10)
        Trabajador10 = sueldo10, round(Salud10), round(AFP10), Sueldo_liquido10

        Reporte_sueldos = {
            trabajadores[0]: Trabajador1,
            trabajadores[1]: Trabajador2,
            trabajadores[2]: Trabajador3,
            trabajadores[3]: Trabajador4,
            trabajadores[4]: Trabajador5,
            trabajadores[5]: Trabajador6,
            trabajadores[6]: Trabajador7,
            trabajadores[7]: Trabajador8,
            trabajadores[8]: Trabajador9,
            trabajadores[9]: Trabajador10
        }

        with open ('Reporte_de_sueldos.csv', 'w', newline='') as archivo_csv:
            escritor_csv = csv.writer(archivo_csv)
            escritor_csv.writerow(["Nombre empleado: Sueldo Bruto  Salud  AFP  Sueldo líquido"])
            escritor_csv.writerow([Reporte_sueldos])
        
        with open ('Reporte_de_sueldos.csv', 'r', newline='') as archivo_csv:
            lector_csv = csv.reader(archivo_csv)
            for fila in lector_csv:
                print(fila)
        
       elif Sueldos == False: 
        print("")
        print("Primero hay que asignar sueldos a los empleados")
        print("")

    elif opciones == "5":
        print("Cerrando programa...")
        print("Desarollado por Lukas Hafemann")
        print("RUT 21.964.466-3")
        break

    else: 
        print("")
        print("Opción inválida, favor que colocar uno de los números asociados a una opción")
        print("")