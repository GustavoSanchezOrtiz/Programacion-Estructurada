#crear una lista de numeros e imprimir el contenido

import os 

os.system("cls")

lista=[1,2,3,4,5]

print(lista)

for i in lista:
    print(i)


#crear una lista de palbras y posteriormente buscar la coincidencia de una palabra

palabras=["numeros","arroz","azucar","que coman","pastel","revolucion francesa"]
buscar=input("que palabra busca: ")
encontro=False


for i in range (0, len(palabras)):
    if palabras[i]==buscar:
        encontro=True

if encontro==True:
    print (f"se encontro la palabra {buscar}")
else:
    print(f"no se encontro la palabra {buscar}")
  

if buscar in palabras:
    print(f"la palabra {buscar} si fue encontrada")
    veces=palabras.count(buscar)
    if veces>1:
        print(f"la palabra se encontro {veces} veces")
else:
    print(f"la palabra {buscar} no fue encontrada")


#añadir elementos ala lista

numeros=[]

opcion=True
while opcion==True:
    numero=float(input("introduce un numero entero o decimal: "))
    numeros.append(numero)
    respuesta=input("¿deseas agregar otro numero? ").lower()
    if respuesta=="si":
        opcion=True
    else:
        opcion=False

print(f"la lista quedo de la siguiente forma:\n\t {numeros}") 


#agenda de numeros

agenda=[
        ["carlos", "6181234567"],
        ["esteban", "6189029029"],
        ["martin", "6189029129"]
]

print (agenda)
for i in agenda:
    print(i)

cadena=""

for r in range(0,3):
    for c in range(0,2):
        cadena+=f"{agenda[r] [c]},"
        cadena+="\n"
    print(cadena)