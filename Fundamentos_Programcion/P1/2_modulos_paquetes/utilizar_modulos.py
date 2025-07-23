#1er froma de importar modulos
import modulos

modulos.borrar_pantalla()
print (modulos.saludar("Dagoberto Fiscal"))
modulos.esperar_tecla()

#2da forma de importar modulos
from modulos import saludar, borrar_pantalla, esperar_tecla
borrar_pantalla()

print (saludar("Gustavo"))
esperar_tecla()

nombre= input("ingresa el nombre del contacto: ")
telefono= input("ingresa el telefono del contacto: ")
nom, tel =modulos.solicitar_datos4(nombre, telefono)
print (f"\t Hola {nom}, \n\t Tu telefono es {tel}")
