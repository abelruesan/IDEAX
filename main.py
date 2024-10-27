# -*- coding: utf-8 -*-

print("Bienvenido a IDEAX, el software que te permite hacer un seguimiento de tus proyectos.")


def menu():
    print("""\n1. - Añadir proyecto
2. - Visualizar proyectos y su progreso
3. - Actualizar progreso
4. - Eliminar proyecto
5. - Ver historial de proyectos completados
6. - Borrar historial de poryectos
7. - Salir del programa""")

    opcion = int(input("\nIntroduce la opcion deseada: "))

    while opcion not in range(1, 8):
        print("\nLa opción introducida no es válida.")
        opcion = int(input("Introduce la opcion deseada: "))

    return opcion


proyectos = []
progreso = []
historial = []

while True:
    # Comprueba si algún progreso es 100. En ese caso añade el proyecto al historial y lo elimina de ambas listas
    for pos, elemento in enumerate(progreso):
        if elemento == 100:
            historial.append(proyectos[pos])
            print(f"\nEl proyecto {pos} ha sido completado. ")
            proyectos.pop(pos)
            progreso.pop(pos)

    opcion = menu()

    # Opción añadir proyecto
    if opcion == 1:
        nuevo_proyecto = input(
            "\nIntroduce el nuevo proyecto que desea crear: ")
        proyectos.append(nuevo_proyecto)
        progreso.append(0)

    # Opción visualizar proyectos y progeso
    elif opcion == 2:
        if len(proyectos) != 0:
            print()  # Línea en blanco
            for pos, elemento in enumerate(proyectos):
                print(f"- {elemento}       Progreso:  {progreso[pos]} %")
        else:
            print("\nTodavía no hay ningún proyecto creado.")

    # Opciçon actualizar progreso
    elif opcion == 3:
        print()
        for pos, elemento in enumerate(proyectos):
            print(f"{pos}. {elemento}")

        progreso_a_actualizar = int(
            input("\nIntroduce la posicion del progreso a modificar: "))

        while progreso_a_actualizar not in range(0, len(proyectos)):
            print("\nLa opción introducida no es válida.")
            progreso_a_actualizar = int(
                input("Introduce la posicion del progreso a modificar: "))

        nuevo_progreso = int(input("\nIntroduce el nuevo progreso: "))

        while nuevo_progreso not in range(0, 101):
            print("\nEl progreso introducido no es válido.")
            nuevo_progreso = int(input("Introduce el nuevo progreso: "))

        progreso[progreso_a_actualizar] = nuevo_progreso

        print(
            f"\nEl pogreso del proyecto {progreso_a_actualizar} ha sido actualizado correctamente")

    # Opción eliminar un proyecto
    elif opcion == 4:
        print()
        for pos, elemento in enumerate(proyectos):
            print(f"{pos}. {elemento}")

        proyecto_a_eliminar = int(
            input("\nIntroduce la posicion del proyecto que desea eliminar: "))

        while proyecto_a_eliminar not in range(0, len(proyectos)):
            print("\nLa posición introducida no es válida.")
            proyecto_a_eliminar = int(
                input("Introduce la posicion del proyecto que desea eliminar: "))

        # Eliminamos el proyecto y su respectivo progreso
        proyectos.pop(proyecto_a_eliminar)
        progreso.pop(proyecto_a_eliminar)

        print(f"\nEl proyecto {
              proyecto_a_eliminar} ha sido eliminado correctamente.")

    # Opción ver el historial de proyectos completados
    elif opcion == 5:
        if len(historial) != 0:
            print("\nProyectos completados: ")
            for elemento in historial:
                print(f"- {elemento}")
        else:
            print("\nEl historial de proyectos está vacío.")

    # Opción borrar el historial
    elif opcion == 6:
        # Pedimos una comprobación al usuario para asegurarnos de que desea borrar el historial
        confirmacion = int(input(
            "\nIntroduce un 1 si está seguro de que desea borrar el historial de proyectos: "))

        if confirmacion == 1:
            historial.clear()
            print("\nEl historial de proyectos ha sido borrado correctamente.")

    else:
        print("\nGracias por utilizar IDEAX")
        break
