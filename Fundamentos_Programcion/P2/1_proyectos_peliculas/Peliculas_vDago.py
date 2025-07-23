peliculas=[]

def borrarPantalla():
  import os  
  os.system("cls")

def esperarTecla():
  print("Oprima cualquier tecla para continuar ...")
  input()  

def agregarPeliculas():
  borrarPantalla()
  print(".:: Alta de Peliculas ::. ")
  pelicula=input("Ingresa el nombre: ").upper().strip()
  peliculas.append(pelicula)
  input("\n\t\t\t :::LA OPERACION SE REALIZO CORRECTAMENTE:::")

def consultarPeliculas():
  borrarPantalla()
  print(".:: Consultar o Mostrar las Peliculas ::.")
  if len(peliculas)>0:
    for i in range(0,len(peliculas)):
      print(f"{i+1}:{peliculas}")
    else:
      print("\t .:: No hay peliculas en el Sistema ::.")

def vaciarPeliculas():
  borrarPantalla()
  print("\n\t.:: Borrar o quitar TODAS las peliculas ::.")
  resp=input("¿Deseas quitar o borrar todas las peliculas del sistema? (Si/No)").lower()
  if resp=="si":
    peliculas.clear()
    input("\n\t\t\t :::LA OPERACION SE REALIZO CORRECTAMENTE:::")

def buscarPelicula():
  
  borrarPantalla()
  print("\n\t.:: Buscar peliculas ::.")
  pelicula_buscar=input("Ingrese el nombre de la pelicula a buscar: ").upper().strip()
  encontro=0
  if not(pelicula_buscar in peliculas):
    print("\n\t\t ¡No se encuentra la pelicula a buscar!")
  else:
    for i in range (0,len(peliculas)):
      if pelicula_buscar==peliculas[i]:
        print(f"La pelicula {pelicula_buscar} si la tenemos y esta en la casilla: {i+1}")
        encontro+=1 
    print(f"Tenemos {encontro} pelicula(s) con este titulo")
    input("\n\t\t\t :::LA OPERACION SE REALIZO CORRECTAMENTE:::")

def eliminarPeliculas():
  borrarPantalla()
  print(".:: Borrar Peliculas ::.")
  nombre_de_pelicula_a_borrar=input("Ingrese el nombre de la pelicula que desea buscar: ").upper().strip()
  i=0
  while nombre_de_pelicula_a_borrar in peliculas:
    desea_borrar=input("¿Deseas quitar o borrar la pelicula del sistema (Si/No)? ").upper()
    if desea_borrar==("SI"):
        indice=peliculas.index(nombre_de_pelicula_a_borrar)
        peliculas.pop(indice)
        indice=indice+1
        i=i+1
        print (f"\nla pelicula que se borro es :{nombre_de_pelicula_a_borrar} y estaba en la casilla :{indice}")
        print("\n\t\t.:: ¡LA OPERACION SE REALIZO CON EXITO! ::.")
    else:
      break
  if i>0:
    print(f"Se borro {i} pelicula(s) con este titulo")  

  

    

    

        