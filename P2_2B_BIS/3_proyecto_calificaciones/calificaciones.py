#funciones califiaciones
import os

def borrar_pantalla():
    os.system("cls")

def esperar_tecla():
    input("Oprima cualquier tecla para continuar ➡️")

def mostar_calificaciones(listas):
 borrar_pantalla()
 print("\t📂.:: Mostrar Calificaciones ::.📂\n")  
 
 if len(listas)>0:
        print(f"{'Nombre👤':<15}{'Cal1📝':<10}{'Cal2📝':<10}{'Cal3📝':<10}")
        print(f"{'-'*40}")
        for fila in listas:
            print(F"{fila[0]:<15}{fila[1]:<10}{fila[2]:<10}{fila[3]:<10}")
            print(f"{'-'*40}")
            cuantos=len(listas)
            print(f"son {cuantos} alumnos👤")

 else:
        print("❌No hay calificaciones registradas en el sistema❌")

def agregar_calificaciones(listas):
   borrar_pantalla()
   print("\t..::📝agregar calificaciones📝::..")
   calificaciones=[]
   nombre=input("\n📝ingrese el nombre del alumno :").upper().strip()
   try:
    for i in range(1,4):
        continua=True
        while continua:
            cal=float(input(f"💾calificaion {i} :"))
            if cal>=0 and cal<11:
                calificaciones.append(cal)
                continua=False
            else:
                print(print("⚠️Ingresa un numero valido⚠️"))
   except ValueError:
      print("⚠️ingrese un numero entre 0 y 10⚠️")
   listas.append([nombre]+calificaciones)
   print ("✅accion realizada con exito✅")
   

def menu_principal():
   
   os.system("cls")
   print("\n\t\t...:::📧 SISTEMA DE GESTION DE CALIFICACIONES 📧:::... \n\t\t\t 1️⃣.- Agregar  \n\t\t\t 2️⃣.- Mostar \n\t\t\t 3️⃣.- Calcular Promedios \n\t\t\t 4️⃣.- salir")
   opcion=input("\t Elige una opción: ").upper()
   return opcion

def calcular_promedios(listas):
    borrar_pantalla()
    print(".::🛠️ Calcular promedios 🛠️::.\n")  
 
    if len(listas)>0:
            '''print(f"{'Nombre':<15}{'promedio':<10}")
            print(f"{'-'*40}")
            for fila in listas:
                cal1=fila[1]
                cal2=fila[2]
                cal3=fila[3]
                promedio= (cal1+cal2+cal3)/3
                print(F"{fila[0]:<15}{promedio}")
                print(f"{'-'*40}")
                cuantos=len(listas)
            print(f"son {cuantos} alumnos")'''
            promedio_grupal=0
            for fila in listas:
                nombre=fila[0]
                '''i=1
                suma=0
                while i>0 and i<=3:
                    suma+=fila[i]
                    i+=1
                promedio_D=suma/3'''
                promedio_D=sum(fila[1:])/3
                print(f"{'👤nombre':<15}{'📝promedio'}")
                print(f"{nombre:<15}{promedio_D:.2f}")
                promedio_grupal+=promedio_D
            print (f"{'-'*30}")
            promedio_grupal=promedio_grupal/len(listas)
            print (f"📝promedio del grupo ={promedio_grupal}")
                
    else:
            print("❌No hay calificaciones registradas en el sistema❌")


'''print(f"Nombre :{renglon[0]} \n calificacion 1: {renglon[1]}\n calificacion 2: {renglon[2]}\n calificacion 3: {renglon[3]}")'''