lista1 = [
    #0
    [1,2,3],
    #1
    [4,5,6],
    #2
    [7,8,9]
          ]

print(lista1)
import os 
os.system("cls")

print(lista1[0][2])

for fila in lista1:
    for elemento in fila:
        print(elemento, end="_")
        print()

lista1[0][0]=99

os.system("cls")


print(lista1)
