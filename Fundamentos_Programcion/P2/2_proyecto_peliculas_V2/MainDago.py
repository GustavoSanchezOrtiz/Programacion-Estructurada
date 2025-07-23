#proyecto2
'''crear un proyecto que permita administrar peliculas; colocar
un menu de opciones para agregar, eliminar, 
modificar y consultar peliculas
Notas:
1.- utilizar funciones y mandar llamar desde otros archivos 
2.- itilizar dict para almacenar los siguientes atributos (nombre, categoria,clasificacion, genero, idioma) de las peliculas.'''



import Peliculas_vDago

opcion=True
while opcion:
    Peliculas_vDago.borrarPantalla()
    print("\n\t\t\t..::: CINEPOLIS CLON :::... \n\t\t..::: Sistema de Gestión de Peliculas :::...\n\t\t 1.- Crear  \n\t\t 2.- Borrar \n\t\t 3.- Mostrar \n\t\t 4.- Agregar Caracteristicas \n\t\t 5.- Modificar Caracteristicas \n\t\t 6.- Borrar Caracteristicas \n\t\t 7.- SALIR ")
    opcion=input("\n\t\tElige una opción: ").upper()

    match opcion:
        case "1":
            Peliculas_vDago.CrearPelicula()
            Peliculas_vDago.esperarTecla()
        case "2":
            Peliculas_vDago.borrarPeliculas()
            Peliculas_vDago.esperarTecla()
        case "3":
            Peliculas_vDago.mostrarPeliculas() 
            Peliculas_vDago.esperarTecla()
        case "4":
            Peliculas_vDago.AgregarCaracteristicaPeliculas()
            Peliculas_vDago.esperarTecla()
        case "5": 
            Peliculas_vDago.ModificarCaracteristicasPelicula()
            Peliculas_vDago.esperarTecla()
        case "6":
             Peliculas_vDago.borrarCaracteristicasPeliculas()
             Peliculas_vDago.esperarTecla()
        case "7":
            opcion=False    
            Peliculas_vDago.borrarPantalla()
            print("\n\tTerminaste la ejecucion del SW")
        case _: 
            input("\n\tOpción invalida vuelva a intentarlo ... por favor")