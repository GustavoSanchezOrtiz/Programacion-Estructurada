from Usuarios import FuncionesUsuario
from Ventas import FuncionesVenta

def BorrarPantalla():
    import os
    os.system("cls" if os.name == "nt" else "clear")

def EsperarTecla():
    input("\nPresiona enter para continuar...")

def main():
    while True:
        BorrarPantalla()
        print(".:: Bienvenido a Kumo ::.")
        eleccion =input("\n\t 1.- Crear usuario\n\t 2.- Iniciar Sesion\n\t 3.- Iniciar sesion como invitado\n\t 4.- Salir\n\tPorfavor, Selecciona una opcion para continuar:")
        match eleccion:
            case "1":
                FuncionesUsuario.crear_usuario()
            case "2":
                FuncionesUsuario.iniciar_sesion()
            case "3":
                FuncionesUsuario.iniciar_sesion_invitado()
            case "4":
                print("Saliendo del programa...")
                break
            case _:
                print("Opcion no valida, porfavor intenta de nuevo.")

def menu_insumos(ID_usuario):
    while True:
        BorrarPantalla()
        print(".:: Menu de insumos ::.")
        seleccion = input("1. Agregar insumo\n2. Modificar insumo\n3. Eliminar insumo\n4. Salir\n\tSelecciona una opcion: ")
        match seleccion:
            case "1":
                FuncionesVenta.agregar_insumo(ID_usuario)
            case "2":
                FuncionesVenta.modificar_insumo()
            case "3":
                FuncionesVenta.eliminar_insumo()
            case "4":
                print("Saliendo del menu de insumos...")
                break
            case _:
                print("Opción no válida, por favor intenta de nuevo.")
                EsperarTecla()

def menu_ventas(ID_usuario):
    while ID_usuario:
        BorrarPantalla()
        print("\n\t..:: VENTAS ::..")
        seleccion=input("\n1. Venta menudeo \n2. Venta mayoreo \n3. Menu insumos \n4. Mostrar ventas por usuario\n5. Mostrar todas las ventas\n6. Modificar venta(propia)\n7. Salir\n\tSelecciona una opcion: ")
        match seleccion:
            case "1":
                FuncionesVenta.venta_menudeo(ID_usuario)
            case "2":
                FuncionesVenta.venta_mayoreo(ID_usuario)
            case "3":
                menu_insumos(ID_usuario)
            case "4":
                FuncionesVenta.mostrar_ventas_por_usuario(ID_usuario)
            case "5":
                FuncionesVenta.mostrar_todas_las_ventas()
            case "6":
                FuncionesVenta.modificar_venta(ID_usuario)
            case "7":
                print("Saliendo del menu de ventas...")
                break
            case _:
                print("Opción no válida, por favor intenta de nuevo.")
                EsperarTecla()


