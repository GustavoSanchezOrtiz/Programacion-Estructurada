peliculas=[]
def agregar_pelicula():
    pelicula_a_agregar=input("¿que pelicula desea agrregar? :").upper()
    peliculas.append(pelicula_a_agregar)
    print (peliculas)

def eliminar_pelicula():
    pelicula_a_eliminar=input("¿que pelicula desea elimnar? :").upper()
    peliculas.remove(pelicula_a_eliminar)
    print(peliculas)
    print (peliculas)

def modificar_pelicula():

    pelicula_a_modificar=input("¿a que pelicula desea modifcarle el nombre? :").upper()
    encontro=0
    for i in range (0,len(peliculas)):
      if pelicula_a_modificar==peliculas[i]:
        encontro=encontro+1
    if encontro>1:
      print (peliculas)
      seleccion=int(input(f"se encontaron {encontro} peliculas con el mismo nombre, ingrese la casilla en la que esta :")) 
      seleccion=seleccion-1
      peliculas.pop(seleccion)
      nuevo_nombre_de_pelicula=input("¿cual sera el nuevo nombre de la pelicula? :").upper()
      peliculas.insert(seleccion, nuevo_nombre_de_pelicula)
      print (peliculas)
    if encontro==1:
        indice=peliculas.index(pelicula_a_modificar)
        peliculas.pop(indice)
        nuevo_nombre_de_pelicula=input("¿cual sera el nuevo nombre de la pelicula? :").upper()
        peliculas.insert(indice, nuevo_nombre_de_pelicula)
        print (peliculas)

def consultar_pelicula():
    
    print (peliculas)

def borrar_pantalla():
    import os
    os.system("cls")

def buscar_pelicula():
    buscar_pelicula=input("¿que pelicula busca? :").upper()
    if buscar_pelicula in peliculas:
        print("la pelicula si fue encontrada")
    else:
        print("la pelicula no fue encontrada")
        
def borrar_lista_de_peliculas():
    peliculas.clear()
    
    


def esperar_tecla():
    input=("Presione una tecla para continuar :")