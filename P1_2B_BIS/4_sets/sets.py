'''set es una colocacion desordenada, inmutable* y no indexada.
No hay miembros duplicados.
es un tipo de datos para tener una coleccion de valores poero no tiene ni indice ni orden 
'''

import os 
os.system("cls")

personas={"Ramiro","Choche","Lupe"}
print (personas)
personas.add("Peje")
print (personas)
personas.pop ()
print (personas)
personas.clear ()
print (personas)

varios={3.12, 3, True, "hola"}
print(varios)

#ejemplo: crear un programa que solicite los emails de los alumnos de la UTD almacenar en una lista y 
#posteriormente mostrar en pantalla los mails sin duplicado

opc="si"
email=[]
os.system("cls")
while opc =="si":
    email.append(input("Introduce el email: "))
    
    opc=input("¿Desea incluir un corrreo mas?: ").lower()

print(email)

