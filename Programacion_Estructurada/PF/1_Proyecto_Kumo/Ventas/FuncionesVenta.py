import ConexionBD
import Funciones
import datetime
import pymysql
import pandas as pd
conexion, cursor = ConexionBD.conexionBD()

def obtener_valores_venta():
    try:
        sql = "select Costo_del_producto from insumos"
        cursor.execute(sql)
        valores = cursor.fetchall()
        total = sum([fila[0] for fila in valores])
        return total
    except:
        print("Error al obtener los valores de venta. Por favor, intenta de nuevo.")
        Funciones.EsperarTecla()
        return None

def venta_menudeo(ID_usuario):
    Funciones.BorrarPantalla()
    print(".:: Venta menudeo ::.")
    Costo_de_produccion = obtener_valores_venta()
    Costo_de_produccion = float(Costo_de_produccion)
    botella_medio = 4.14
    botella_litro = 5.22
    sabor = 1
    Lista_Sabores = []
    while sabor != "":
        try:
            Funciones.BorrarPantalla()
            print("\tSabores disponibles: \n1. Fresa\n2. Horchata\n3. Horchata con chocolate \n4. Capuchino con avellana\n5. Piña colada\n6. Pistache \n7. Mango\n8. Platano")
            sabor = input("Ingresa el numero del sabor vendido para salir presiona enter: ")
            if sabor == "1":
                sabor = "Fresa"
            elif sabor == "2":
                sabor = "Horchata"
            elif sabor == "3":
                sabor = "Horchata con chocolate"
            elif sabor == "4":
                sabor = "Capuchino con avellana"
            elif sabor == "5":
                sabor = "Piña colada"
            elif sabor == "6":
                sabor = "Pistache"
            elif sabor == "7":
                sabor = "Mango"
            elif sabor == "8":
                sabor = "Platano"

            if sabor != "":
                Lista_Sabores.append(sabor)
        except ValueError:
            print("Error al ingresar el valor. Por favor, intenta de nuevo.")
    porciones_vendidas = len(Lista_Sabores)
    #Costo total por cada 4 litros(por porcion)
    Total = 35*2 + 22*4
    Costo_de_produccion = Costo_de_produccion+(botella_litro*2 + botella_medio*4)
    Ganancia = Total - Costo_de_produccion
    fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    Total_venta = Total * porciones_vendidas
    Ganancia_total = Ganancia * porciones_vendidas
    try:
        sql = ("INSERT INTO ventas (ID_venta, ID_usuario, Venta, Total, Ganancia, Fecha) VALUES (NULL, %s, %s, %s, %s, %s)")
        values = (ID_usuario, str(Lista_Sabores), Total_venta, Ganancia_total, fecha)
        cursor.execute(sql, values)
        conexion.commit()
        print("Venta menudeo registrada exitosamente.")
    except:
        print(f" Vuelva a intentarlo. No fue posible realizar la venta menudeo:")
    Funciones.EsperarTecla()

def venta_mayoreo(ID_usuario):
    Funciones.BorrarPantalla()
    print(".:: Venta mayoreo ::.")
    Costo_de_produccion = obtener_valores_venta()
    Costo_de_produccion = float(Costo_de_produccion)
    botella_medio = 4.14
    botella_litro = 5.22
    sabor = 1
    Lista_Sabores = []
    while sabor != "":
        try:
            Funciones.BorrarPantalla()
            print("\tSabores disponibles: \n1. Fresa\n2. Horchata\n3. Horchata con chocolate \n4. Capuchino con avellana\n5. Piña colada\n6. Pistache \n7. Mango\n8. Platano")
            sabor = input("Ingresa el numero del sabor vendido para salir presiona enter: ")
            if sabor == "1":
                sabor = "Fresa"
            elif sabor == "2":
                sabor = "Horchata"
            elif sabor == "3":
                sabor = "Horchata con chocolate"
            elif sabor == "4":
                sabor = "Capuchino con avellana"
            elif sabor == "5":
                sabor = "Piña colada"
            elif sabor == "6":
                sabor = "Pistache"
            elif sabor == "7":
                sabor = "Mango"
            elif sabor == "8":
                sabor = "Platano"

            if sabor != "":
                Lista_Sabores.append(sabor)
        except ValueError:
            print("Error al ingresar el valor. Por favor, intenta de nuevo.")
    porciones_vendidas = len(Lista_Sabores)
    #Costo total por cada 4 litros(por porcion)
    if porciones_vendidas >= 4:
        Total = 32*2 + 20*4
    elif porciones_vendidas >= 12:
        Total = 30*2 + 18*4
    Costo_de_produccion = Costo_de_produccion+(botella_litro*2 + botella_medio*4)
    Ganancia = Total - Costo_de_produccion
    fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    Total_venta = Total * porciones_vendidas
    Ganancia_total = Ganancia * porciones_vendidas
    try:
        sql = ("INSERT INTO ventas (ID_venta, ID_usuario, Venta, Total, Ganancia, Fecha) VALUES (NULL, %s, %s, %s, %s, %s)")
        values = (ID_usuario, str(Lista_Sabores), Total_venta, Ganancia_total, fecha)
        cursor.execute(sql, values)
        conexion.commit()
        print("Venta mayoreo registrada exitosamente.")
    except:
        print(f" Vuelva a intentarlo. No fue posible realizar la venta mayoreo:")
    Funciones.EsperarTecla()


def agregar_insumo(ID_usuario):
    Funciones.BorrarPantalla()
    print(".:: Agregar insumo (costos x cada 4 litros)::.")
    nombre = input("Ingresa el nombre del insumo: ").upper().strip()
    Costo = input("Ingresa el costo del insumo: ").strip()
    sql = "INSERT INTO insumos (ID_Producto, Nombre_producto, Costo_del_producto, ID_usuario) VALUES (NULL, %s, %s, %s);"
    try:
        values = (nombre, Costo, ID_usuario)
        cursor.execute(sql, values)
        conexion.commit()
        print("Insumo agregado exitosamente.")
        Funciones.EsperarTecla()
    except Exception as e:
        print(" Vuelva a intentarlo. No fue posible agregar insumo:")
        print(f"Error: {e}")
        Funciones.EsperarTecla()

def modificar_insumo():
    try:
        Funciones.BorrarPantalla()
        print(".:: Modificar insumo ::.")
        sql = "SELECT * FROM insumos"
        cursor.execute(sql)
        insumos = cursor.fetchall()
        if not insumos:
            print("No hay insumos para modificar.")
            Funciones.EsperarTecla()
        else:
            print("Insumos disponibles:")
            for insumo in insumos:
                print(f"ID: {insumo[0]}, Nombre: {insumo[1]}, Costo: {insumo[2]}")
            Funciones.EsperarTecla()
            id_insumo = input("Ingresa el ID del insumo a modificar: ").strip()
            nuevo_nombre = input("Ingresa el nuevo nombre del insumo: ").upper().strip()
            nuevo_costo = input("Ingresa el nuevo costo del insumo: ").strip()
            sql = "UPDATE insumos SET Nombre_producto = %s, Costo_del_producto = %s WHERE ID = %s"
            values = (nuevo_nombre, nuevo_costo, id_insumo)
            cursor.execute(sql, values)
            conexion.commit()
    except:
        print(" Vuelva a intentarlo. No fue posible modificar insumo:")
        Funciones.EsperarTecla()

def eliminar_insumo():
    Funciones.BorrarPantalla()
    print(".:: Eliminar insumo ::.")
    try:
        sql = "SELECT * FROM insumos"
        cursor.execute(sql)
        insumos = cursor.fetchall()
        if not insumos:
            print("No hay insumos para eliminar.")
            Funciones.EsperarTecla()
        else:
            print("Insumos disponibles:")
            for insumo in insumos:
                print(f"ID: {insumo[0]}, Nombre: {insumo[1]}, Costo: {insumo[2]}")
            Funciones.EsperarTecla()
            id_insumo = input("Ingresa el ID del insumo a eliminar: ").strip()
            sql = "DELETE FROM insumos WHERE ID = %s"
            cursor.execute(sql, (id_insumo,))
            conexion.commit()
    except:
        print(" Vuelva a intentarlo. No fue posible eliminar insumo:")
        Funciones.EsperarTecla()

def mostrar_ventas_por_usuario(ID_usuario):
    Funciones.BorrarPantalla()
    print(".:: Ventas por usuario ::.")
    try:
        # Obtiene las ventas del usuario especificado
        sql = "SELECT * FROM ventas WHERE ID_usuario = %s"
        cursor.execute(sql, (ID_usuario,))
        ventas = cursor.fetchall()
        # Obtiene el total de ventas del usuario
        sql ="select Total from ventas where ID_usuario = %s"
        cursor.execute(sql, (ID_usuario,))
        total_ventas = cursor.fetchall()
        total = sum([fila[0] for fila in total_ventas]) if total_ventas else 0
        total = float(total)
        #obtencion de ganancia total
        sql = "SELECT Ganancia FROM ventas WHERE ID_usuario = %s"
        cursor.execute(sql, (ID_usuario,))
        ganancia_ventas = cursor.fetchall()
        ganancia = sum([fila[0] for fila in ganancia_ventas]) if ganancia_ventas else 0
        ganancia = float(ganancia)
        if not ventas:
            print("No hay ventas registradas para este usuario.")
        else:
            print("_"*100)
            for venta in ventas:
                print(f"ID Venta: {venta[0]}, Usuario ID: {venta[1]}, Venta: {venta[2]}, Total: {venta[3]}, Ganancia: {venta[4]}, Fecha: {venta[5]}")
            print("_"*100)
            print(f"Total de ventas del usuario: {total}")
            print(f"Ganancia total del usuario: {ganancia}")
    except Exception as e:
        print("Error al mostrar las ventas por usuario. Por favor, intenta de nuevo.")
        print(f"Detalles del error: {e}")
    Funciones.EsperarTecla()

def mostrar_todas_las_ventas():
    Funciones.BorrarPantalla()
    print(".:: Todas las ventas ::.")
    try:
        # Obtiene todas las ventas
        sql = "SELECT * FROM ventas"
        cursor.execute(sql,)
        ventas = cursor.fetchall()
        # Obtiene el total de ventas
        sql ="select Total from ventas"
        cursor.execute(sql,)
        total_ventas = cursor.fetchall()
        total = sum([fila[0] for fila in total_ventas]) if total_ventas else 0
        total = float(total)
        #obtencion de ganancia total
        sql = "SELECT Ganancia FROM ventas"
        cursor.execute(sql,)
        ganancia_ventas = cursor.fetchall()
        ganancia = sum([fila[0] for fila in ganancia_ventas]) if ganancia_ventas else 0
        ganancia = float(ganancia)
        if not ventas:
            print("No hay ventas registradas.")
        else:
            print("_"*100)
            for venta in ventas:
                print(f"ID Venta: {venta[0]}, Usuario ID: {venta[1]}, Venta: {venta[2]}, Total: {venta[3]}, Ganancia: {venta[4]}, Fecha: {venta[5]}")
            print("_"*100)
            print(f"Total de ventas: {total}")
            print(f"Ganancia total: {ganancia}")
            desea_importar = input("¿Deseas exportar las ventas a un archivo Excel? (s/n): ").strip().lower()
            if desea_importar == 's':
                importacion_a_exel()
            else:
                None
    except Exception as e:
        print("Error al mostrar las ventas. Por favor, intenta de nuevo.")
        print(f"Detalles del error: {e}")
    Funciones.EsperarTecla()

def modificar_venta(ID_usuario):
    Funciones.BorrarPantalla()
    print(".:: Modificar venta ::.")
    try:
        sql = "SELECT * FROM ventas WHERE ID_usuario = %s"
        cursor.execute(sql, (ID_usuario,))
        ventas = cursor.fetchall()
        if not ventas:
            print("No hay ventas registradas para este usuario.")
            Funciones.EsperarTecla()
            return
        print("Ventas: ")
        for venta in ventas:
            print(f"ID Venta: {venta[0]}, Usuario ID: {venta[1]}, Venta: {venta[2]}, Total: {venta[3]}, Ganancia: {venta[4]}, Fecha: {venta[5]}")
        id_venta = input("Ingresa el ID de la venta a modificar: ").strip()
        nuevo_total = input("Ingresa el nuevo total de la venta: ").strip()
        nueva_ganancia = input("Ingresa la nueva ganancia de la venta: ").strip()
        sql = "UPDATE ventas SET Total = %s, Ganancia = %s WHERE ID_venta = %s AND ID_usuario = %s"
        values = (nuevo_total, nueva_ganancia, id_venta, ID_usuario)
        cursor.execute(sql, values)
        conexion.commit()
        print("Venta modificada exitosamente.")
    except Exception as e:
        print("Error al modificar la venta. Por favor, intenta de nuevo.")
        print(f"Detalles del error: {e}")
    Funciones.EsperarTecla()

def importacion_a_exel():
    df = pd.read_sql("SELECT * FROM ventas", conexion)

    df.to_excel("ventas_exportadas.xlsx", index=False)