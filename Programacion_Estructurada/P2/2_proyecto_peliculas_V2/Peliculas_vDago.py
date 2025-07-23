

peliculas=[]


#dict u objeto para almacenar los atributos (nombre, categoria, clsdificscion, genero, idioma)

'''pelicula=(
  "nombre":"",
  "categoria":"",
  "clasificiacion":"",
  "genero":"",
  "idioma":"",
)'''
pelicula={}



def borrarPantalla():
  import os  
  os.system("cls")

def esperarTecla():
  print("Oprima cualquier tecla para continuar ...")
  input()  

def CrearPelicula():
  borrarPantalla()
  print(".:: Alta de Peliculas ::. ")
  pelicula.update({"nombre":input("ingresa el nombre de la pelicula: ").upper().strip()})
  pelicula.update({"categoria":input("ingresa la categoria de la pelicula: ").upper().strip()})
  pelicula.update({"clasificacion":input("ingresa la clasificacion de la pelicula: ").upper().strip()})
  pelicula.update({"genero":input("ingresa el genero de la pelicula: ").upper().strip()})
  pelicula.update({"idioma":input("ingresa el idioma de la pelicula: ").upper().strip()})
  input("\n\t\t\t :::LA OPERACION SE REALIZO CORRECTAMENTE:::")

def mostrarPeliculas():
  borrarPantalla()
  print(".:: Consultar o Mostrar la Pelicula ::. \n")
  if len(pelicula)>0:
    for i in pelicula:
      print(f"\t {(i)}: {pelicula[i]}")
    else:
      print("\t..:: No hay peliculas en el sistema ::..")

def borrarPeliculas():
  borrarPantalla()
  print(".:: Borrar o Quitar TODAS las Peliculas ::. \n")
  resp=input("¿Deseas quitar o borrar todas las peliculas del sistema? SI/NO ")
  if resp=="SI":
    pelicula.clear()
    print("\n\t..:::: La operacion se realizo con exito::::..")
  

def AgregarCaracteristicaPeliculas():
  borrarPantalla
  print(".:: Agregar Caracteristicas a peliculas ::. ")
  atributo=input("Ingresa la nueva caracteristica a agregar: ").lower().strip()
  pelicula.update({atributo:input("ingresa el nombre: ").upper().strip()})
  print("\n\t\t\t :::LA OPERACION SE REALIZO CORRECTAMENTE:::")

def ModificarCaracteristicasPelicula():
  borrarPantalla()
  print(".:: Modificar Caracteristicas de Peliculas ::. \n")
  if len(pelicula) > 0:
    for i in pelicula:
      print(f"\t {(i)}: {pelicula[i]}")
    else:
      print("\t..:: No hay peliculas en el sistema ::..")

      Caracteristica_a_modificar = input("¿Qué característica deseas modificar?: ").lower().strip()
      if Caracteristica_a_modificar in pelicula:
        NuevaCaracteristica = input(f"Ingresa el nuevo valor para {Caracteristica_a_modificar}: ").upper().strip()
        pelicula[Caracteristica_a_modificar] = NuevaCaracteristica
        print("\n\t..:: La operacion se realizo con exito ::..")
      else:
        print("\n\t..:: La caracteristica no existe ::..")
  else:
    print("\n\t..:: No hay peliculas en el sistema ::..")

def borrarCaracteristicasPeliculas():
  borrarPantalla()
  print(".:: Borrar Características de la Película ::.\n")
  if len(pelicula) == 0:
    print("\t..:: No hay películas registradas ::..")
    return
  print("Características actuales de la película:")
  for i in pelicula:
    print(f"\t{i}: {pelicula[i]}")  
  Caracteristica_a_borrar = input("\nEscribe el nombre de la característica que deseas borrar: ").lower().strip()
  if Caracteristica_a_borrar in pelicula:
    pelicula.pop(Caracteristica_a_borrar)
    print("\n\t..:::: Característica borrada con éxito ::::..")
  else:
    print("\n\t..:: Esa característica no existe ::..")




'''def agregarPeliculas():
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
'''
  

    

    

        