import Peliculas_vDago

opcion=True
while opcion:
    Peliculas_vDago.borrarPantalla()
    print("\n\t\t\t..::: CINEPOLIS CLON :::... \n\t\t..::: Sistema de Gestión de Peliculas :::...\n\t\t 1.- Agregar  \n\t\t 2.- Eliminar \n\t\t 3.- Actualizar \n\t\t 4.- Consultar \n\t\t 5.- Buscar \n\t\t 6.- Vaciar \n\t\t 7.- SALIR ")
    opcion=input("\n\t\tElige una opción: ").upper()

    match opcion:
        case "1":
            Peliculas_vDago.agregarPeliculas()
            Peliculas_vDago.esperarTecla()
        case "2":
            Peliculas_vDago.eliminarPeliculas()
            Peliculas_vDago.esperarTecla()
        case "3":
            Peliculas_vDago.modificarPeliculas() 
            Peliculas_vDago.esperarTecla()
        case "4":
            Peliculas_vDago.consultarPeliculas()
            Peliculas_vDago.esperarTecla()
        case "5": 
            Peliculas_vDago.buscarPelicula()
            Peliculas_vDago.esperarTecla()
        case "6":
             Peliculas_vDago.vaciarPeliculas()
             Peliculas_vDago.esperarTecla()
        case "7":
            opcion=False    
            Peliculas_vDago.borrarPantalla()
            print("\n\tTerminaste la ejecucion del SW")
        case _: 
            input("\n\tOpción invalida vuelva a intentarlo ... por favor")