'''una funciones un conjunto de instrucciones que se agrupan bajo un nombre en particular como un programa mas pequeño que cumple con
una tarea especifica la funcion se puede reutilizar con el simple echo de invocarla es decir mandarla llamar 

sintaxis: 

def nombredemifuncion(parametros): 
    bloque o conjunto de instrucciones

las funciones pueden ser de 4 tipos 
1.- funcion que no recibe parametros y no regresa valor 
2.- funcion que no recibe parametros y regresa valor
3.- Funcion que recibe parametros y no regresa valor
4.- Funcion que recibe parametros y regresa valor
'''
#funcion que no recibe parametros y no regresa valor
def solicitar_datos1():
    nombre = input("¿Cual es tu nombre? ")
    telefono = input("¿Cual es tu telefono? ")
    print(f"Hola {nombre}, tu telefono es {telefono}")

#funcion que no recibe parametros y regresa valor
def solicitar_datos2():
    nombre = input("¿Cual es tu nombre? ")
    telefono = input("¿Cual es tu telefono? ")
    return nombre, telefono

#funcion que recibe parametros y no regresa valor
def solicitar_datos3(nombre, telefono):
    nombre=nombre
    telefono=telefono
    print(f"Hola {nombre}, tu telefono es {telefono}")

#funcion que recibe parametros y regresa valor
def solicitar_datos4(nombre, telefono):
    nom=nombre
    tel=telefono
    return nom, tel

#llamada a la funcion