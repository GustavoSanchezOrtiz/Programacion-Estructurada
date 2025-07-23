'''
crear un programa que calcule e imprima la tabla de multiplicar de un numero entero positivo
requisito:
con funciones que regresen valor y usen parametros

'''
import os 
os.system("cls")

#solicitud de datos
numero=int(input("introduce un numero entero para realizar la tabla de multiplicar que se desea: "))

#proceso v1
resultado1=numero*1
print(f"{numero} x 1 = {resultado1}")
resultado2=numero*2
print(f"{numero} x 2 = {resultado2}")
resultado3=numero*3
print(f"{numero} x 3 = {resultado3}")
resultado4=numero*4
print(f"{numero} x 4 = {resultado4}")
resultado5=numero*5
print(f"{numero} x 5 = {resultado5}")
resultado6=numero*6
print(f"{numero} x 6 = {resultado6}")
resultado7=numero*7
print(f"{numero} x 7 = {resultado7}")
resultado8=numero*8
print(f"{numero} x 8 = {resultado8}")
resultado9=numero*9
print(f"{numero} x 9 = {resultado9}")
resultado10=numero*10
print(f"{numero} x 10 = {resultado10}")

#proceso v2
for i in range(1,11):
    resultado=numero*i
    print(f"{numero} x {i} = {resultado}")

#proceso v3
i=1
while i<= 10:
    resultado=numero*i
    print(f"{numero} x {i} = {resultado}")
    i+=1

#proceso v4
def tabla_multiplicar(numero):
    resultado1=numero*1
    resultado2=numero*2
    resultado3=numero*3
    resultado4=numero*4
    resultado5=numero*5
    resultado6=numero*6
    resultado7=numero*7
    resultado8=numero*8
    resultado9=numero*9
    resultado10=numero*10
    return resultado1, resultado2, resultado3, resultado4, resultado5, resultado6, resultado7, resultado8, resultado9, resultado10

#llamada a la funcion
resultado1, resultado2, resultado3, resultado4, resultado5, resultado6, resultado7, resultado8, resultado9, resultado10=tabla_multiplicar(numero)
print(f"la tabla de multiplicar del {numero} es: \n{resultado1} \n{resultado2} \n{resultado3} \n{resultado4} \n{resultado5} \n{resultado6} \n{resultado7} \n{resultado8} \n{resultado9} \n{resultado10}")
# esta si es la de arriba no esta es v3
def tabla_multiplicar2(numero):
    num=numero
    respuesta=""
    for i in range(1,11):
        resultado=num*i
        respuesta+=f"\t{num} x {i} = {resultado}\n"
    return respuesta
#llamada a la funcion
respuesta=tabla_multiplicar2(numero)
print(f"la tabla de multiplicar del {numero} es: \n{respuesta}")