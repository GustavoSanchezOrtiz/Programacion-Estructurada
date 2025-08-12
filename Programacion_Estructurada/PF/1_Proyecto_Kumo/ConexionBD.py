import mysql.connector

def conexionBD():
    try:
        conexion=mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="bd_proyecto_kumo",
        )
        cursor=conexion.cursor(buffered=True)
        return conexion, cursor
    except:
        input(f"En este momento no posible comunicarse con el sistema, intentelo mas tarde, presione enter para continuar ...")
        return None, None

