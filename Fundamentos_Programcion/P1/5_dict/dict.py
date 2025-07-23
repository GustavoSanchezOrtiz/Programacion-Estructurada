'''dict.- es un tipo de datos que se utiliza par almacenar datos de diferente tipo de datos pero en ligar de tener
como las listas indices numericos tiene alfanumericos. Es decir es algo parecido como los objetos
tambien se conoce como un arreglo asosiativo u objeto JSON
el diccionario es una coleccion ordenada y modificables'''

import os


os.system("cls")
#lista
paises=["Mexico","brasil","España","Canada"]
#dict o objeto
Pais_Mexico={"nombre":"Mexico","capital":"CDMX","poblacion":"1200000000","lengua oficial":"Español"}
Pais_Brasil={"nombre":"Brasil","capital":"Brasilia","poblacion":"1000000000","lengua oficial":"Portugues"}
Pais_canada={"nombre":"Canada","capital":"Ottawa","poblacion":"900000000","lengua oficial":{"Ingles","Frances"}}

#alumnos
alumno_1={"nombre":"bibiana", "apellido_paterno":"Soria", "apellido_materno":"Muños","Carrera":"TI","matricula":"123123123",
          "area":"software_muliplataforma",
          "modalidad":"bilingue",
          }

print(alumno_1)
for i in alumno_1:
    print (f"{i}={alumno_1[i]}")

alumno_1["telefono"]="6181551803"
print(alumno_1)
for i in alumno_1:
    print (f"{i}={alumno_1[i]}")
