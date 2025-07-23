#lista vacia
arreglo = []

#agregar elementos
arreglo.append(10)
arreglo.append(20)

palabra= "unico"

arreglo.append(palabra)

arreglo.append("monolito")

print("arreglo actual es :", arreglo)
import os 
os.system("cls")
print("arreglo actual en primera posicion :", arreglo[0])
print("arreglo actual en primera posicion :", arreglo[-1])

del arreglo[1]
print(arreglo)

arreglo.remove("unico")
print(arreglo)

arreglo.insert(1,99)
print(arreglo)