#Crear un proyecto que permita gestionar (administrar) peliculas, colocar un menu de opciones para agregar, eliminar, modificar, y consultar 
#agregar,mostrar,calcular promedio y salir
#-----Notas-----
#1.- Utilizar funciones, mandar llamar desde otro archivo
#2.- Utilizar listas para almacenar los nombres de peliculas
import os

import calificaciones

def main():
    datos = []
    opc=True
    while opc:
        calificaciones.borrar_pantalla()
        opcion=calificaciones.menu_principal()
        match opcion:
                case "1":
                    calificaciones.agregar_calificaciones(datos)
                    calificaciones.esperar_tecla()
                case "2":
                    calificaciones.mostar_calificaciones(datos)
                    calificaciones.esperar_tecla()  
                case "3":
                    calificaciones.calcular_promedios(datos)
                    calificaciones.esperar_tecla()
                case "4":
                    opc=False
                    calificaciones.borrar_pantalla()
                case _:
                    os.system("cls") 
                    input("⚠️Opción invalida vuelva a intentarlo ... por favor⚠️")
                    
if __name__ == "__main__":
    main()