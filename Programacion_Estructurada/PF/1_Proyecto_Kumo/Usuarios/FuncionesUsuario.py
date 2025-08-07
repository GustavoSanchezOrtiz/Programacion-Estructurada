import ConexionBD
import Funciones
import hashlib

conexion, cursor = ConexionBD.conexionBD()

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def crear_usuario():
    Funciones.BorrarPantalla()
    nombre = input("Ingresa tu nombre: ").upper().strip()
    email = input("Ingresa tu email: ").upper().strip()
    password = input("Ingresa tu contraseña: ")
    password=hash_password(password) #Encriptacion de contraseña
    if conexion and cursor:
        try:
            cursor.execute("insert into usuarios (nombre, email, password) VALUES (%s, %s, %s)", (nombre, email, password))
            conexion.commit()
            print("Usuario creado exitosamente.")
        except:
            print("Error al crear el usuario. Por favor, verifica los datos e intenta de nuevo.")
        Funciones.EsperarTecla()
    else:
        print("No se pudo establecer conexión con la base de datos.")

def iniciar_sesion():
    Funciones.BorrarPantalla()
    email = input("Ingresa tu email: ").upper().strip()
    password = input("Ingresa tu contraseña: ")
    password=hash_password(password) #Encriptacion de contraseña
    if conexion and cursor:
        try:
            cursor.execute("SELECT * FROM usuarios WHERE email = %s AND password = %s", (email, password))
            usuario = cursor.fetchone()
            if usuario:
                print(f"Bienvenido {usuario[1]}!")
                Funciones.menu_ventas(usuario[0])  # ID del usuario
            else:
                print("Email o contraseña incorrectos.")
        except:
            print("Error al iniciar sesión. Por favor, verifica los datos e intenta de nuevo.")
        Funciones.EsperarTecla()
    else:
        print("No se pudo establecer conexión con la base de datos.")  

def iniciar_sesion_invitado():
    Funciones.BorrarPantalla()
    try:
        nombre_usuario = "INVITADO"
        sql="select * from usuarios where nombre = %s"
        val=(nombre_usuario,)
        cursor.execute(sql,val)
        valor_verificado=cursor.fetchall()
    except:
        print("Error al iniciar sesión como invitado. Por favor, intenta de nuevo.")
        Funciones.EsperarTecla()
        
    if valor_verificado: 
        print("Has iniciado sesión como invitado.")
        Funciones.menu_ventas(valor_verificado[0][0])  # ID del usuario
        Funciones.EsperarTecla()
    else:
        if conexion and cursor:
            try:
                cursor.execute("insert into usuarios (nombre, email, password) VALUES (%s, %s, %s)", (nombre_usuario, "invitado@kumo.com", ""))
                conexion.commit()
                print("Has iniciado sesión como invitado.")
            except:
                print("Error al crear el usuario invitado. Por favor, intenta de nuevo.")
                Funciones.EsperarTecla()
        else:
            print("No se pudo establecer conexión con la base de datos.")
            Funciones.EsperarTecla()


    