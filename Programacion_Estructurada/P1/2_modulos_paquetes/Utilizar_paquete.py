from paquete_1 import modulos

print ( modulos.saludar ("Gustavo"))
modulos.borrar_pantalla()
nom,tel=modulos.solicitar_datos2()
print (f"agenda telefonica: {tel}\n\t numero: {tel}")
modulos.esperar_tecla()