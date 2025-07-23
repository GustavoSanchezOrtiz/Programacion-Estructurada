
def borrar_pantalla():
    import os
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # macOS and Linux
        os.system('clear')

def esperar_tecla():
    input("\n\t\t\tPresione Enter para continuar...")

def menu_principal():
    borrar_pantalla()
    print("\t\t..::📂 Sistema de Agenda  de Contactos 📂::..\n")
    print("\t\t\t1️⃣.- Agregar Contacto\n\t\t\t2️⃣.- Mostrar Todos Los Contactos\n\t\t\t3️⃣.- Buscar Contacto Por Nombre \n\t\t\t4️⃣.- Modificar Contacto \n\t\t\t5️⃣.- Eliminar Contacto\n\t\t\t6️⃣.- Salir")
    seleccion_accion_menu_principal=input("\t\t\t💾Seleccione una opcion: ")
    return seleccion_accion_menu_principal

def agregar_contacto(agenda_contactos):
    borrar_pantalla()
    print("\t\t..::📂 Agregar Contacto 📂::..\n")
    nombre=input("\tIngrese el nombre del contacto:")
    if nombre in agenda_contactos:
        print(f"\t\t\tEl contacto {nombre} ya existe en la agenda.")
    else:
        datos_temporales=[]
        telefono=input("\tIngrese el telefono del contacto:")
        datos_temporales.append(telefono)
        email=input("\tIngrese el email del contacto:")
        datos_temporales.append(email)
        agenda_contactos[nombre]=datos_temporales
        print(f"\t\t\tContacto {nombre} agregado exitosamente")
    esperar_tecla()

def mostrar_todos_los_contactos(agenda_contactos):
    borrar_pantalla()
    print("\t\t..::📂 Mostrar Todos Los Contactos 📂::..\n")
    for nombre,datos in agenda_contactos.items():
        print(f"\tNombre: {nombre},\t\n\tTelefono: {datos[0]},\t\n\tEmail: {datos[1]}")
       
        print("_"*80)    
    esperar_tecla()

def buscar_contacto_por_nombre(agenda_contactos):
    borrar_pantalla()
    print("\t\t..::📂 Buscar Contacto Por Nombre 📂::..\n")
    nombre_buscar=input("\tIngrese el nombre del contacto a buscar:")
    if nombre_buscar in agenda_contactos:
        datos=agenda_contactos[nombre_buscar]
        print(f"\tNombre: {nombre_buscar},\t\n\tTelefono: {datos[0]},\t\n\tEmail: {datos[1]}")
        esperar_tecla()
    else:
        print(f"\t\t\tEl contacto {nombre_buscar} no existe en la agenda.")
        esperar_tecla()

def modificar_contacto(agenda_contactos):
    borrar_pantalla()
    print("\t\t..::📂 Modificar Contacto 📂::..\n")
    nombre_modificar=input("\tIngrese el nombre del contacto a modificar:")
    if nombre_modificar in agenda_contactos:
        telefono=input("\tIngrese el nuevo telefono del contacto:")
        email=input("\tIngrese el nuevo email del contacto:")
        agenda_contactos[nombre_modificar] = [telefono, email]
        print(f"\t\t\tContacto {nombre_modificar} modificado exitosamente")
        esperar_tecla()
    else:
        print(f"\t\t\tEl contacto {nombre_modificar} no existe en la agenda.")
        esperar_tecla()

def eliminar_contacto(agenda_contactos):
    borrar_pantalla()
    print("\t\t..::📂 Eliminar Contacto 📂::..\n")
    nombre_eliminar=input("\tIngrese el nombre del contacto a eliminar:")
    if nombre_eliminar in agenda_contactos:
        del agenda_contactos[nombre_eliminar]
        print(f"\t\t\tContacto {nombre_eliminar} eliminado exitosamente")
        esperar_tecla()
    else:
        print(f"\t\t\tEl contacto {nombre_eliminar} no existe en la agenda.")
        esperar_tecla()


    
