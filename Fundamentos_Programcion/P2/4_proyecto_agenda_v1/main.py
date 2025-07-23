import os 
import agenda

agenda_contactos = {"Juan Perez": ["123456789", "juan.perez@example.com"]}

while True:
    seleccion_accion_menu_principal = agenda.menu_principal()
    match seleccion_accion_menu_principal:
        case "1":
            agenda.agregar_contacto(agenda_contactos)
        case "2":
            agenda.mostrar_todos_los_contactos(agenda_contactos)
        case "3":
            agenda.buscar_contacto_por_nombre(agenda_contactos)
        case "4":
            agenda.modificar_contacto(agenda_contactos)
        case "5":
            agenda.eliminar_contacto(agenda_contactos)
        case "6":
            print("\t\t\tGracias por usar el sistema de agenda de contactos")
            break
        case _:
            print("\t\t\tOpcion no valida, por favor intente nuevamente")
            agenda.esperar_tecla()