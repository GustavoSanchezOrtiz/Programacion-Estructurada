#funciones de proyecto aguas 

def borrar_pantalla():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def esperar_tecla():
    input("\n\tPresione Enter para continuar...")


def menu_principal():
    borrar_pantalla()
    print ("\t\t\n..:: MENU PRINCIPAL ::..")
    opcion=input("\n\t1.- Registrar ventas \n\t2.- Costos de insunmos \n\t3.- Sabores \n\t4.- Salir \n\n\tIngrese una opción: ")
    return opcion

# Costos de insumos variables
def asignacion_azucar_por_litro(azucar_bulto):
    if azucar_bulto <= 0:  
        azucar_bulto=440 # Costo por bulto de azucar
    cantidad_azucar_por_bulto=25 # Cantidad de azucar por bulto KG
    costo_por_kg_azucar = azucar_bulto / cantidad_azucar_por_bulto # Costo por KG de azucar
    cantidad_azucar_por_litro=280 # Cantidad de azucar por litro de agua grms de azucar
    costo_azucar_por_litro = (costo_por_kg_azucar * cantidad_azucar_por_litro) / 1000 # Costo de azucar por litro de agua
    return costo_azucar_por_litro, azucar_bulto
        
def asignacion_carnetion_por_litro(costo_por_lata_de_carnetion):
    if costo_por_lata_de_carnetion <= 0:
        costo_por_lata_de_carnetion = 139 # Costo por lata de carnation presentación de 1.8 kg
    cantidad_de_tsbp_por_lata_carnetion = 141 # Cantidad de cucharadas soperas por lata de carnation
    costo_por_tsbp_carnetion = costo_por_lata_de_carnetion / cantidad_de_tsbp_por_lata_carnetion # Costo por cucharada sopera de carnation
    cantidad_de_tazas_de_carnetion_por_litro = 1/2 # Cantidad de tazas de carnation por litro de agua
    costo_por_taza_carnetion = costo_por_tsbp_carnetion * 16 # Costo por taza de carnation
    costo_carnetion_por_litro = costo_por_taza_carnetion * cantidad_de_tazas_de_carnetion_por_litro # Costo de carnation por litro de agua
    return costo_carnetion_por_litro, costo_por_lata_de_carnetion

def asignacion_lechera_por_litro(costo_por_lata_de_lechera):
    if costo_por_lata_de_lechera <= 0:
        costo_por_lata_de_lechera = 21 # Costo por lata de lechera presentación de 397 grms
    cantidad_lechera_por_litro = 1 # Cantidad de lechera por litro de agua en tazas
    costo_de_lechera_por_litro = costo_por_lata_de_lechera / cantidad_lechera_por_litro # Costo de lechera por litro de agua
    return costo_de_lechera_por_litro, costo_por_lata_de_lechera

def asignacion_CMC_por_litro(costo_bote_de_CMC):
    if costo_bote_de_CMC <= 0:
        costo_bote_de_CMC = 50 # Costo por bote de CMC presentación de 360 grms
    cantidad_CMC_por_litro = 2 # Cantidad de CMC por litro en grms
    costo_CMC_por_litro = (costo_bote_de_CMC / 360) * cantidad_CMC_por_litro # Costo de CMC por litro de agua
    return costo_CMC_por_litro, costo_bote_de_CMC

def asignacion_de_sal_por_litro(costo_de_sal):
    if costo_de_sal <= 0:
        costo_de_sal = 24 # Costo de sal por bote de 1 kg
    cantidad_de_sal_por_litro = 2 # Cantidad de sal por litro de agua en grms
    costo_de_sal_por_litro = (costo_de_sal / 1000) * cantidad_de_sal_por_litro # Costo de sal por litro de agua
    return costo_de_sal_por_litro, costo_de_sal
    
def asignacion_de_vainilla_por_litro(costo_de_vainilla):
    if costo_de_vainilla <= 0:
        costo_de_vainilla = 180 # Costo de vainilla por bote de 4 litros
    cantidad_de_vainilla_por_litro = 15 # Cantidad de vainilla por litro de agua en ml
    costo_de_vainilla_por_litro = (costo_de_vainilla / 4000) * cantidad_de_vainilla_por_litro # Costo de vainilla por litro de agua
    return costo_de_vainilla_por_litro, costo_de_vainilla

# Costos variables por cada tipo de agua
def asignacion_esencia_por_litro(costo_de_esencia):
    if costo_de_esencia <= 0:
        costo_de_esencia = 260 # Costo de esencia por bote de 1 litro
    cantidad_de_esencia_por_litro_promedio = 20 # Cantidad de esencia por litro de agua en ml
    costo_esencia_por_litro_promedio = (costo_de_esencia / 1000) * cantidad_de_esencia_por_litro_promedio # Costo de esencia por litro de agua promedio
    return costo_esencia_por_litro_promedio, costo_de_esencia

#costos de insumos fijos
def asignacion_por_mensualidad_bebbia(costo_por_mensualidad_bebbia):
    if costo_por_mensualidad_bebbia <= 0:
        costo_por_mensualidad_bebbia = 239
    costo_por_dia_de_bebbia = costo_por_mensualidad_bebbia / 30 # Costo por día de Bebbia
    return costo_por_dia_de_bebbia, costo_por_mensualidad_bebbia

def reiniciar_costos_a_valores_determinados():
    azucar_bulto = 0 # Costo por bulto de azucar
    costo_por_lata_de_carnetion = 0 # Costo por lata de carnation presentación de 1.8 kg
    costo_por_lata_de_lechera = 0 # Costo por lata de lechera presentación de 397 grms
    costo_bote_de_CMC = 0 # Costo por bote de CMC presentación de 360 grms
    costo_de_sal = 0 # Costo de sal por bote de 1 kg    
    costo_de_vainilla = 0 # Costo de vainilla por bote de 4 litros
    costo_de_esencia = 0 # Costo de esencia por bote de 1 litro
    costo_por_mensualidad_bebbia = 0 # Costo por mensualidad de Bebbia
    return (azucar_bulto, costo_por_lata_de_carnetion, costo_por_lata_de_lechera,costo_bote_de_CMC, costo_de_sal, costo_de_vainilla, costo_de_esencia, costo_por_mensualidad_bebbia)

def asignacion_costos_de_insumos(costo_azucar_por_litro, costo_carnetion_por_litro, costo_lechera_por_litro, costo_CMC_por_litro, costo_sal_por_litro, costo_vainilla_por_litro, costo_esencia_por_litro, costo_por_mensualidad_bebbia , costo_por_dia_de_bebbia, azucar_bulto, costo_por_lata_de_carnetion, costo_por_lata_de_lechera, costo_bote_de_CMC, costo_de_sal, costo_de_vainilla, costo_de_esencia):

    Costo_de_insumos_lista_por_litro = {
        "Azucar": costo_azucar_por_litro,
        "Carnation": costo_carnetion_por_litro,
        "Lechera": costo_lechera_por_litro,
        "CMC": costo_CMC_por_litro,
        "Sal": costo_sal_por_litro,
        "Vainilla": costo_vainilla_por_litro,
        "Esencia": costo_esencia_por_litro,
        "Dia Bebbia": costo_por_dia_de_bebbia
    }
    Costos_de_insumos_lista_por_objeto_total = {
        "Azucar por bulto": azucar_bulto,
        "Carnation por lata": costo_por_lata_de_carnetion,
        "Lechera por lata": costo_por_lata_de_lechera,
        "CMC por bote": costo_bote_de_CMC,
        "Sal por bote": costo_de_sal,
        "Vainilla por bote": costo_de_vainilla,
        "Esencia por bote": costo_de_esencia,
        "Mensualidad Bebbia": costo_por_mensualidad_bebbia
    }
    return Costo_de_insumos_lista_por_litro, Costos_de_insumos_lista_por_objeto_total

def Asignacion_costos_especificos_pistache(costo_de_esencia_de_pistache):
    if costo_de_esencia_de_pistache <= 0:
        costo_de_esencia = 260 # Costo de esencia por bote de 1 litro
    cantidad_de_esencia_por_litro_pistache = 30 # Cantidad de esencia por litro de agua en ml
    costo_esencia_por_cada_litro_pistache = (costo_de_esencia / 1000) * cantidad_de_esencia_por_litro_pistache # Costo de esencia por litro de agua pistache
    return costo_esencia_por_cada_litro_pistache, costo_de_esencia_de_pistache

def Asignacion_costos_especificos_fresa( costo_de_charola_de_fresa):
    cantidad_de_fresa_por_litro =  80 # Cantidad de fresa por litro de agua en grms
    if costo_de_charola_de_fresa <= 0:
        costo_de_charola_de_fresa = 55 # Costo de charola de fresa presentación de 500 grms
    costo_fresa_por_kilo = costo_de_charola_de_fresa *2 # Costo de fresa por kilo
    costo_de_fresa_por_litro = (costo_fresa_por_kilo / 1000) * cantidad_de_fresa_por_litro # Costo de fresa por litro de agua
    return costo_de_fresa_por_litro , costo_de_charola_de_fresa

def Asignacion_costos_especificos_mango(costo_de_mango_por_kilo):
    cantidad_de_mango_por_litro = 400 # Cantidad de mango por litro de agua en grms
    if costo_de_mango_por_kilo <= 0:
        costo_de_mango_por_kilo = 40 # Costo de mango por kilo
    costo_de_mango_por_litro = (costo_de_mango_por_kilo / 1000) * cantidad_de_mango_por_litro # Costo de mango por litro de agua
    return costo_de_mango_por_litro , costo_de_mango_por_kilo

def Asignacion_costos_especificos_horchata_con_chocolate_abuelita(costo_por_lata_de_chocolate_abuelita):
    cantidad_de_chocolate_abuelita_por_litro = 8 # Cantidad de chocolate abuelita por litro de agua en tsbp
    if costo_por_lata_de_chocolate_abuelita <= 0:
        costo_por_lata_de_chocolate_abuelita = 230 # Costo por lata de chocolate abuelita presentación de 2.3 KG
    peso_de_tsbp_chocolate_abuelita = 15 # Peso de cucharada sopera de chocolate abuelita en grms
    costo_por_litro_chocolate_abuelita = (costo_por_lata_de_chocolate_abuelita / 2300) * peso_de_tsbp_chocolate_abuelita * cantidad_de_chocolate_abuelita_por_litro
    return costo_por_litro_chocolate_abuelita , costo_por_lata_de_chocolate_abuelita

def Asignacion_costos_especificos_cafe_con_leche(costo_por_lata_de_cafe):
    cantidad_de_cafe_por_litro = 2 # Cantidad de café por litro de agua en tsbp
    if costo_por_lata_de_cafe <= 0:
        costo_por_lata_de_cafe = 200 # Costo por lata de café presentación de 400 grms
    peso_de_tsbp_cafe = 10 # Peso de cucharada sopera de café en grms
    costo_por_litro_cafe = (costo_por_lata_de_cafe / 400) * peso_de_tsbp_cafe * cantidad_de_cafe_por_litro
    return costo_por_litro_cafe , costo_por_lata_de_cafe


def restablecer_costos_especificos_por_sabor():
    costo_de_esencia_de_pistache = 0
    costo_de_charola_de_fresa = 0
    costo_de_mango_por_kilo = 0
    costo_por_lata_de_chocolate_abuelita = 0
    costo_por_lata_de_cafe = 0
    return (costo_de_esencia_de_pistache, costo_de_charola_de_fresa, costo_de_mango_por_kilo, costo_por_lata_de_chocolate_abuelita, costo_por_lata_de_cafe)

def Asignacion_lista_costos_especificos_por_sabor(costo_esencia_por_cada_litro_pistache, costo_de_fresa_por_litro, costo_de_mango_por_litro, costo_por_litro_chocolate_abuelita, costo_por_litro_cafe, costo_por_lata_de_chocolate_abuelita, costo_por_lata_de_cafe, costo_de_charola_de_fresa, costo_de_mango_por_kilo, costo_de_esencia_de_pistache):

    lista_de_costos_de_insumos_especificos_por_sabor = {
        "HORCHATA": 0,
        "HORCHATA_CON_CHOCOLATE_ABUELITA": costo_por_litro_chocolate_abuelita,
        "PIÑA_COLADA": 0,
        "PISTACHE": costo_esencia_por_cada_litro_pistache,
        "FRESA_CON_LECHE": costo_de_fresa_por_litro,
        "MANGO_CON_LECHE": costo_de_mango_por_litro,
        "NUEZ": 0,
        "PLATANO": 0,
        "CAFE_CON_LECHE": costo_por_litro_cafe
    }
    lista_de_costos_de_insumos_especificos_por_objeto_total = {
        "HORCHATA": 0,
        "HORCHATA_CON_CHOCOLATE_ABUELITA": costo_por_lata_de_chocolate_abuelita,
        "PIÑA_COLADA": 0,
        "PISTACHE": costo_de_esencia_de_pistache,
        "FRESA_CON_LECHE": costo_de_charola_de_fresa,
        "MANGO_CON_LECHE": costo_de_mango_por_kilo,
        "NUEZ": 0,
        "PLATANO": 0,
        "CAFE_CON_LECHE": costo_por_lata_de_cafe
    }
    return lista_de_costos_de_insumos_especificos_por_sabor, lista_de_costos_de_insumos_especificos_por_objeto_total

def mostrar_costos_de_insumos(Costo_de_insumos_lista_por_litro, Costos_de_insumos_lista_por_objeto_total):
    print("\n\t..:: COSTOS DE INSUMOS POR LITRO::..")
    for insumo, costo in Costo_de_insumos_lista_por_litro.items():
        if insumo == "Mensualidad Bebbia":
            print(f"{insumo}: ${costo:.2f} por dia")
        else:
            print(f"{insumo}: ${costo:.2f} por litro")
    print("\n\t..:: COSTOS DE INSUMOS POR OBJETO TOTAL ::..")
    for insumo, costo in Costos_de_insumos_lista_por_objeto_total.items():
        if insumo == "Mensualidad Bebbia":
            print(f"{insumo}: ${costo:.2f} por mes")
        else:
            print(f"{insumo}: ${costo:.2f}")
    esperar_tecla()

def menu_cambiar_costos_de_insumos():
    print("\n\t..:: CAMBIAR COSTO DE INSUMOS ::..")
    opcion_menu_insumos=input("\n\t1.- Cambiar costo de azucar \n\t2.- Cambiar costo de carnation \n\t3.- Cambiar costo de lechera \n\t4.- Cambiar costo de CMC \n\t5.- Cambiar costo de sal \n\t6.- Cambiar costo de vainilla \n\t7.- Cambiar costo de esencia \n\t8.- Cambiar costo de mensualidad Bebbia \n\t9.- Salir \n\n\tIngrese una opción: ")
    borrar_pantalla()
    return opcion_menu_insumos

def obtencion_variables_costos_de_insumos(Costos_de_insumos_lista_por_objeto_total, Costo_de_insumos_lista_por_litro):
    for i in Costos_de_insumos_lista_por_objeto_total.items():
        azucar_bulto = Costos_de_insumos_lista_por_objeto_total["Azucar por bulto"]
        costo_por_lata_de_carnetion = Costos_de_insumos_lista_por_objeto_total["Carnation por lata"]
        costo_por_lata_de_lechera = Costos_de_insumos_lista_por_objeto_total["Lechera por lata"]
        costo_bote_de_CMC = Costos_de_insumos_lista_por_objeto_total["CMC por bote"]
        costo_de_sal = Costos_de_insumos_lista_por_objeto_total["Sal por bote"]
        costo_de_vainilla = Costos_de_insumos_lista_por_objeto_total["Vainilla por bote"]
        costo_de_esencia = Costos_de_insumos_lista_por_objeto_total["Esencia por bote"]
        costo_por_mensualidad_bebbia = Costos_de_insumos_lista_por_objeto_total["Mensualidad Bebbia"]

    for i in Costo_de_insumos_lista_por_litro.items():
        costo_azucar_por_litro = Costo_de_insumos_lista_por_litro["Azucar"]
        costo_carnetion_por_litro = Costo_de_insumos_lista_por_litro["Carnation"]
        costo_lechera_por_litro = Costo_de_insumos_lista_por_litro["Lechera"]
        costo_CMC_por_litro = Costo_de_insumos_lista_por_litro["CMC"]
        costo_sal_por_litro = Costo_de_insumos_lista_por_litro["Sal"]
        costo_vainilla_por_litro = Costo_de_insumos_lista_por_litro["Vainilla"]
        costo_esencia_por_litro = Costo_de_insumos_lista_por_litro["Esencia"]
        costo_por_dia_de_bebbia = Costo_de_insumos_lista_por_litro["Dia Bebbia"]
    
    return (azucar_bulto, costo_por_lata_de_carnetion, costo_por_lata_de_lechera, costo_bote_de_CMC, costo_de_sal, costo_de_vainilla, costo_de_esencia, costo_por_mensualidad_bebbia,costo_azucar_por_litro, costo_carnetion_por_litro, costo_lechera_por_litro, costo_CMC_por_litro, costo_sal_por_litro, costo_vainilla_por_litro, costo_esencia_por_litro, costo_por_dia_de_bebbia)

def menu_costos_insumos(Costo_de_insumos_lista_por_litro, Costos_de_insumos_lista_por_objeto_total, lista_de_costos_de_insumos_especificos_por_sabor, lista_de_costos_de_insumos_especificos_por_objeto_total):
    Continuar_menu_costos_insumos = True
    while Continuar_menu_costos_insumos:
        try:
            borrar_pantalla()
            print ("\t\t\n..:: COSTOS DE INSUMOS ::..")
            opcion=input("\n\t1.- Ver costo de insumos \n\t2.- Cambiar costo de insumos \n\t3.- Ver costos de insumos específicos por sabor \n\t4.- Cambiar costos de insumos específicos por sabor \n\t5.- Reiniciar Valores Predetirmanados(insumos especificos) \n\t 6.- Reiniciar Valores Predetermiandos(insumos generales) \n\t 7.- Salir\n\tIngrese una opción: ")
            borrar_pantalla()
            match opcion: 
                case "1":
                    mostrar_costos_de_insumos(Costo_de_insumos_lista_por_litro, Costos_de_insumos_lista_por_objeto_total)
                case "2":
                    Continuar = True
                    while Continuar==True:
                        try:
                            opcion_menu_insumos = menu_cambiar_costos_de_insumos()

                            azucar_bulto, costo_por_lata_de_carnetion, costo_por_lata_de_lechera, costo_bote_de_CMC, costo_de_sal, costo_de_vainilla, costo_de_esencia, costo_por_mensualidad_bebbia,costo_azucar_por_litro, costo_carnetion_por_litro, costo_lechera_por_litro, costo_CMC_por_litro, costo_sal_por_litro, costo_vainilla_por_litro, costo_esencia_por_litro, costo_por_dia_de_bebbia = obtencion_variables_costos_de_insumos(Costos_de_insumos_lista_por_objeto_total, Costo_de_insumos_lista_por_litro)
                            
                            
                            match opcion_menu_insumos:

                                case "1":
                                    print(f"\n\tCosto actual de azucar por bulto: ${azucar_bulto:.2f}")
                                    nuevo_azucar_bulto = float(input("\n\tIngrese el nuevo costo por bulto de azucar: "))
                                    costo_azucar_por_litro, azucar_bulto=asignacion_azucar_por_litro(nuevo_azucar_bulto)
                                    Costo_de_insumos_lista_por_litro, Costos_de_insumos_lista_por_objeto_total = asignacion_costos_de_insumos(costo_azucar_por_litro, costo_carnetion_por_litro, costo_lechera_por_litro, costo_CMC_por_litro, costo_sal_por_litro, costo_vainilla_por_litro, costo_esencia_por_litro, costo_por_mensualidad_bebbia, costo_por_dia_de_bebbia, azucar_bulto, costo_por_lata_de_carnetion, costo_por_lata_de_lechera, costo_bote_de_CMC, costo_de_sal, costo_de_vainilla, costo_de_esencia)
                                case "2":
                                    print(f"\n\tCosto actual de carnation por lata: ${costo_por_lata_de_carnetion:.2f}")
                                    costo_por_lata_de_carnetion = float(input("\n\tIngrese el nuevo costo por lata de carnation: "))
                                    costo_carnetion_por_litro, costo_por_lata_de_carnetion = asignacion_carnetion_por_litro(costo_por_lata_de_carnetion)
                                    Costo_de_insumos_lista_por_litro, Costos_de_insumos_lista_por_objeto_total = asignacion_costos_de_insumos(costo_azucar_por_litro, costo_carnetion_por_litro, costo_lechera_por_litro, costo_CMC_por_litro, costo_sal_por_litro, costo_vainilla_por_litro, costo_esencia_por_litro, costo_por_mensualidad_bebbia, costo_por_dia_de_bebbia, azucar_bulto, costo_por_lata_de_carnetion, costo_por_lata_de_lechera, costo_bote_de_CMC, costo_de_sal, costo_de_vainilla, costo_de_esencia)
                                case "3":
                                    print(f"\n\tCosto actual de lechera por lata: ${costo_por_lata_de_lechera:.2f}")
                                    costo_por_lata_de_lechera = float(input("\n\tIngrese el nuevo costo por lata de lechera: "))
                                    costo_lechera_por_litro, costo_por_lata_de_lechera = asignacion_lechera_por_litro(costo_por_lata_de_lechera)
                                    Costo_de_insumos_lista_por_litro, Costos_de_insumos_lista_por_objeto_total = asignacion_costos_de_insumos(costo_azucar_por_litro, costo_carnetion_por_litro, costo_lechera_por_litro, costo_CMC_por_litro, costo_sal_por_litro, costo_vainilla_por_litro, costo_esencia_por_litro, costo_por_mensualidad_bebbia, costo_por_dia_de_bebbia, azucar_bulto, costo_por_lata_de_carnetion, costo_por_lata_de_lechera, costo_bote_de_CMC, costo_de_sal, costo_de_vainilla, costo_de_esencia)
                                case "4":
                                    print(f"\n\tCosto actual de CMC por lata: ${costo_bote_de_CMC}")
                                    costo_bote_de_CMC = float(input("\n\tIngrese el nuevo costo por lata de CMC: "))
                                    costo_CMC_por_litro, costo_bote_de_CMC = asignacion_CMC_por_litro(costo_bote_de_CMC)
                                    Costo_de_insumos_lista_por_litro, Costos_de_insumos_lista_por_objeto_total = asignacion_costos_de_insumos(costo_azucar_por_litro, costo_carnetion_por_litro, costo_lechera_por_litro, costo_CMC_por_litro, costo_sal_por_litro, costo_vainilla_por_litro, costo_esencia_por_litro, costo_por_mensualidad_bebbia, costo_por_dia_de_bebbia, azucar_bulto, costo_por_lata_de_carnetion, costo_por_lata_de_lechera, costo_bote_de_CMC, costo_de_sal, costo_de_vainilla, costo_de_esencia)
                                case "5":
                                    print(f"\n\tCosto actual de sal por bote: ${costo_de_sal:.2f}")
                                    costo_de_sal = float(input("\n\tIngrese el nuevo costo por bote de sal: "))
                                    costo_sal_por_litro, costo_de_sal = asignacion_de_sal_por_litro(costo_de_sal)
                                    Costo_de_insumos_lista_por_litro, Costos_de_insumos_lista_por_objeto_total = asignacion_costos_de_insumos(costo_azucar_por_litro, costo_carnetion_por_litro, costo_lechera_por_litro, costo_CMC_por_litro, costo_sal_por_litro, costo_vainilla_por_litro, costo_esencia_por_litro, costo_por_mensualidad_bebbia, costo_por_dia_de_bebbia, azucar_bulto, costo_por_lata_de_carnetion, costo_por_lata_de_lechera, costo_bote_de_CMC, costo_de_sal, costo_de_vainilla, costo_de_esencia)
                                case "6":
                                    print(f"\n\tCosto actual de vainilla por bote: ${costo_de_vainilla:.2f}")
                                    costo_de_vainilla = float(input("\n\tIngrese el nuevo costo por bote de vainilla: "))
                                    costo_vainilla_por_litro, costo_de_vainilla = asignacion_de_vainilla_por_litro(costo_de_vainilla)
                                    Costo_de_insumos_lista_por_litro, Costos_de_insumos_lista_por_objeto_total = asignacion_costos_de_insumos(costo_azucar_por_litro, costo_carnetion_por_litro, costo_lechera_por_litro, costo_CMC_por_litro, costo_sal_por_litro, costo_vainilla_por_litro, costo_esencia_por_litro, costo_por_mensualidad_bebbia, costo_por_dia_de_bebbia, azucar_bulto, costo_por_lata_de_carnetion, costo_por_lata_de_lechera, costo_bote_de_CMC, costo_de_sal, costo_de_vainilla, costo_de_esencia)
                                case "7":
                                    print(f"\n\tCosto actual de esencia por bote: ${costo_de_esencia:.2f}")
                                    costo_de_esencia = float(input("\n\tIngrese el nuevo costo por bote de esencia: "))
                                    costo_esencia_por_litro, costo_de_esencia = asignacion_esencia_por_litro(costo_de_esencia)
                                    Costo_de_insumos_lista_por_litro, Costos_de_insumos_lista_por_objeto_total = asignacion_costos_de_insumos(costo_azucar_por_litro, costo_carnetion_por_litro, costo_lechera_por_litro, costo_CMC_por_litro, costo_sal_por_litro, costo_vainilla_por_litro, costo_esencia_por_litro, costo_por_mensualidad_bebbia, costo_por_dia_de_bebbia, azucar_bulto, costo_por_lata_de_carnetion, costo_por_lata_de_lechera, costo_bote_de_CMC, costo_de_sal, costo_de_vainilla, costo_de_esencia)
                                case "8":
                                    print(f"\n\tCosto actual de mensualidad Bebbia: ${costo_por_mensualidad_bebbia:.2f}")
                                    costo_por_mensualidad_bebbia = float(input("\n\tIngrese el nuevo costo por mensualidad de Bebbia: "))
                                    costo_por_dia_de_bebbia, costo_por_mensualidad_bebbia = asignacion_por_mensualidad_bebbia(costo_por_mensualidad_bebbia)
                                    Costo_de_insumos_lista_por_litro, Costos_de_insumos_lista_por_objeto_total = asignacion_costos_de_insumos(costo_azucar_por_litro, costo_carnetion_por_litro, costo_lechera_por_litro, costo_CMC_por_litro, costo_sal_por_litro, costo_vainilla_por_litro, costo_esencia_por_litro, costo_por_mensualidad_bebbia, costo_por_dia_de_bebbia, azucar_bulto, costo_por_lata_de_carnetion, costo_por_lata_de_lechera, costo_bote_de_CMC, costo_de_sal, costo_de_vainilla, costo_de_esencia)
                                case "9":
                                    Continuar = False
                                case _:
                                    print("\n⚠️Opción invalida, por favor intente nuevamente⚠️")
                                    esperar_tecla()
                        except ValueError:
                            print("\n⚠️Error: Entrada no válida. Por favor, ingrese un número válido.⚠️")
                            esperar_tecla()
                case "3":
                    print("\n\t..:: COSTOS DE INSUMOS POR LITRO ESPECIFICOS ::..")
                    for insumo_especifico, costo_especifico in lista_de_costos_de_insumos_especificos_por_sabor.items():
                        print(f"{insumo_especifico}: ${costo_especifico:.2f} por litro")
                    print("\n\t..:: COSTOS DE INSUMOS POR OBJETO TOTAL ::..")
                    for insumo_especifico, costo_especifico in lista_de_costos_de_insumos_especificos_por_objeto_total.items():
                        print(f"{insumo_especifico}: ${costo_especifico:.2f}")
                    esperar_tecla()
                case "4":
                    print("\n\t..:: CAMBIAR COSTOS DE INSUMOS ESPECIFICOS POR SABOR ::..")
                    Continuar_insumos_especificos = True
                    while Continuar_insumos_especificos == True:
                        try:
                            for insumo, costo in lista_de_costos_de_insumos_especificos_por_objeto_total.items():
                                costo_por_lata_de_chocolate_abuelita = lista_de_costos_de_insumos_especificos_por_objeto_total["HORCHATA_CON_CHOCOLATE_ABUELITA"]
                                costo_por_lata_de_cafe = lista_de_costos_de_insumos_especificos_por_objeto_total["CAFE_CON_LECHE"]
                                costo_de_charola_de_fresa = lista_de_costos_de_insumos_especificos_por_objeto_total["FRESA_CON_LECHE"]  
                                costo_de_mango_por_kilo = lista_de_costos_de_insumos_especificos_por_objeto_total["MANGO_CON_LECHE"]
                            for insumo, costo in lista_de_costos_de_insumos_especificos_por_sabor.items():
                                costo_esencia_por_cada_litro_pistache = lista_de_costos_de_insumos_especificos_por_sabor["PISTACHE"]
                                costo_de_fresa_por_litro = lista_de_costos_de_insumos_especificos_por_sabor["FRESA_CON_LECHE"]
                                costo_de_mango_por_litro = lista_de_costos_de_insumos_especificos_por_sabor["MANGO_CON_LECHE"]
                                costo_por_litro_chocolate_abuelita = lista_de_costos_de_insumos_especificos_por_sabor["HORCHATA_CON_CHOCOLATE_ABUELITA"]
                                costo_por_litro_cafe = lista_de_costos_de_insumos_especificos_por_sabor["CAFE_CON_LECHE"]
                            print("\n\t1.- Cambiar costo de horchata \n\t2.- Cambiar costo de horchata con chocolate abuelita \n\t3.- Cambiar costo de piña colada \n\t4.- Cambiar costo de pistache \n\t5.- Cambiar costo de fresa con leche \n\t6.- Cambiar costo de mango con leche \n\t7.- Cambiar costo de nuez \n\t8.- Cambiar costo de plátano \n\t9.- Cambiar costo de café con leche \n\t10.- Salir")
                            opcion_menu_insumos_especificos = input("\n\tIngrese una opción: ")
                            borrar_pantalla()
                            match opcion_menu_insumos_especificos:
                                case "1":
                                    print(f"\n\tCosto actual de horchata: ${lista_de_costos_de_insumos_especificos_por_sabor['HORCHATA']:.2f}")
                                    nuevo_costo_horchata = float(input("\n\tIngrese el nuevo costo por litro de horchata: "))
                                    lista_de_costos_de_insumos_especificos_por_sabor["HORCHATA"] = nuevo_costo_horchata

                                case "2":
                                    print(f"\n\tCosto actual de lata chocolate abuelita: ${costo_por_lata_de_chocolate_abuelita:.2f}")
                                    nuevo_costo_chocolate_abuelita = float(input("\n\tIngrese el nuevo costo por lata de chocolate abuelita: "))
                                    costo_por_litro_chocolate_abuelita, costo_por_lata_de_chocolate_abuelita = Asignacion_costos_especificos_horchata_con_chocolate_abuelita(nuevo_costo_chocolate_abuelita)
                                    lista_de_costos_de_insumos_especificos_por_sabor, lista_de_costos_de_insumos_especificos_por_objeto_total = Asignacion_lista_costos_especificos_por_sabor(costo_esencia_por_cada_litro_pistache, costo_de_fresa_por_litro, costo_de_mango_por_litro, costo_por_litro_chocolate_abuelita, costo_por_litro_cafe, costo_por_lata_de_chocolate_abuelita, costo_por_lata_de_cafe, costo_de_charola_de_fresa, costo_de_mango_por_kilo, costo_esencia_por_cada_litro_pistache)
                                case "3":
                                    print(f"\n\tCosto actual de piña colada: ${lista_de_costos_de_insumos_especificos_por_sabor['PIÑA_COLADA']:.2f}")
                                    nuevo_costo_pina_colada = float(input("\n\tIngrese el nuevo costo por litro de piña colada: "))
                                    lista_de_costos_de_insumos_especificos_por_sabor["PIÑA_COLADA"] = nuevo_costo_pina_colada
                                case "4":
                                    print(f"\n\tCosto adicional actual de pistache: ${costo_esencia_por_cada_litro_pistache:.2f}")
                                    nuevo_costo_pistache = float(input("\n\tIngrese el nuevo costo por litro de pistache: "))
                                    costo_esencia_por_cada_litro_pistache, costo_de_esencia_de_pistache = Asignacion_costos_especificos_pistache(nuevo_costo_pistache)
                                    lista_de_costos_de_insumos_especificos_por_sabor, lista_de_costos_de_insumos_especificos_por_objeto_total = Asignacion_lista_costos_especificos_por_sabor(costo_esencia_por_cada_litro_pistache, costo_de_fresa_por_litro, costo_de_mango_por_litro, costo_por_litro_chocolate_abuelita, costo_por_litro_cafe, costo_por_lata_de_chocolate_abuelita, costo_por_lata_de_cafe, costo_de_charola_de_fresa, costo_de_mango_por_kilo, costo_esencia_por_cada_litro_pistache)
                                case "5":
                                    print(f"\n\tCosto actual de charola de fresa: ${costo_de_fresa_por_litro:.2f}")
                                    nuevo_costo_charola_fresa = float(input("\n\tIngrese el nuevo costo por charola de fresa: "))
                                    costo_de_fresa_por_litro , costo_de_charola_de_fresa = Asignacion_costos_especificos_fresa(nuevo_costo_charola_fresa)
                                    lista_de_costos_de_insumos_especificos_por_sabor, lista_de_costos_de_insumos_especificos_por_objeto_total = Asignacion_lista_costos_especificos_por_sabor(costo_esencia_por_cada_litro_pistache, costo_de_fresa_por_litro, costo_de_mango_por_litro, costo_por_litro_chocolate_abuelita, costo_por_litro_cafe, costo_por_lata_de_chocolate_abuelita, costo_por_lata_de_cafe, costo_de_charola_de_fresa, costo_de_mango_por_kilo, costo_esencia_por_cada_litro_pistache)
                                case "6":
                                    print(f"\n\tCosto actual de kilo de mango: ${costo_de_mango_por_kilo:.2f}")
                                    nuevo_costo_mango = float(input("\n\tIngrese el nuevo costo por kilo de mango: "))
                                    costo_de_mango_por_litro, costo_de_mango_por_kilo = Asignacion_costos_especificos_mango(nuevo_costo_mango)
                                    lista_de_costos_de_insumos_especificos_por_sabor, lista_de_costos_de_insumos_especificos_por_objeto_total = Asignacion_lista_costos_especificos_por_sabor(costo_esencia_por_cada_litro_pistache, costo_de_fresa_por_litro, costo_de_mango_por_litro, costo_por_litro_chocolate_abuelita, costo_por_litro_cafe, costo_por_lata_de_chocolate_abuelita, costo_por_lata_de_cafe, costo_de_charola_de_fresa, costo_de_mango_por_kilo, costo_esencia_por_cada_litro_pistache)
                                case "7":
                                    print(f"\n\tCosto actual de nuez: ${lista_de_costos_de_insumos_especificos_por_sabor['NUEZ']:.2f}")
                                    nuevo_costo_nuez = float(input("\n\tIngrese el nuevo costo por litro de nuez: "))
                                    lista_de_costos_de_insumos_especificos_por_sabor["NUEZ"] = nuevo_costo_nuez
                                case "8":
                                    print(f"\n\tCosto actual de plátano: ${lista_de_costos_de_insumos_especificos_por_sabor['PLATANO']:.2f}")
                                    nuevo_costo_platano = float(input("\n\tIngrese el nuevo costo por litro de plátano: "))
                                    lista_de_costos_de_insumos_especificos_por_sabor["PLATANO"] = nuevo_costo_platano
                                case "9":
                                    print(f"\n\tCosto actual lata de cafe${costo_por_lata_de_cafe:.2f}")
                                    nuevo_costo_cafe = float(input("\n\tIngrese el nuevo costo por lata de café: "))
                                    costo_por_litro_cafe, costo_por_lata_de_cafe = Asignacion_costos_especificos_cafe_con_leche(nuevo_costo_cafe)
                                    lista_de_costos_de_insumos_especificos_por_sabor, lista_de_costos_de_insumos_especificos_por_objeto_total = Asignacion_lista_costos_especificos_por_sabor(costo_esencia_por_cada_litro_pistache, costo_de_fresa_por_litro, costo_de_mango_por_litro, costo_por_litro_chocolate_abuelita, costo_por_litro_cafe, costo_por_lata_de_chocolate_abuelita, costo_por_lata_de_cafe, costo_de_charola_de_fresa, costo_de_mango_por_kilo, costo_esencia_por_cada_litro_pistache)
                                case "10":
                                    Continuar_insumos_especificos = False
                                case _:
                                    print("\n⚠️Opción invalida, por favor intente nuevamente⚠️")
                                    esperar_tecla()
                        except ValueError:
                            print("\n⚠️Error: Entrada no válida. Por favor, ingrese un número válido.⚠️")
                            esperar_tecla()
                            return menu_costos_insumos(Costo_de_insumos_lista_por_litro, Costos_de_insumos_lista_por_objeto_total, lista_de_costos_de_insumos_especificos_por_sabor, lista_de_costos_de_insumos_especificos_por_objeto_total)
                case "5":
                    print("\n\t..:: REINICIAR VALORES PREDETERMINADOS DE INSUMOS ESPECIFICOS POR SABOR ::..")
                    restablecer_costos_especificos_por_sabor()
                    lista_de_costos_de_insumos_especificos_por_sabor, lista_de_costos_de_insumos_especificos_por_objeto_total = Asignacion_lista_costos_especificos_por_sabor(0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
                    print("\n\tValores reiniciados exitosamente.")
                    esperar_tecla()
                case "6":
                    print("\n\t..:: REINICIAR VALORES PREDETERMINADOS DE INSUMOS GENERALES ::..")
                    reiniciar_costos_a_valores_determinados()
                    Costo_de_insumos_lista_por_litro, Costos_de_insumos_lista_por_objeto_total = asignacion_costos_de_insumos(costo_azucar_por_litro, costo_carnetion_por_litro, costo_lechera_por_litro, costo_CMC_por_litro, costo_sal_por_litro, costo_vainilla_por_litro, costo_esencia_por_litro, costo_por_mensualidad_bebbia , costo_por_dia_de_bebbia, azucar_bulto, costo_por_lata_de_carnetion, costo_por_lata_de_lechera, costo_bote_de_CMC, costo_de_sal, costo_de_vainilla, costo_de_esencia)
                    print("\n\tValores reiniciados exitosamente.")
                    esperar_tecla()
                case "7":
                    Continuar_menu_costos_insumos = False
                case _:
                    print("\n⚠️Opción invalida, por favor intente nuevamente con un número válido⚠️")
                    esperar_tecla()
        except ValueError:
            print("\n⚠️Error: Entrada no válida. Por favor, ingrese un número válido.⚠️")
            return menu_costos_insumos()

def lista_de_sabores():
    Lista_de_sabores = [
    "HORCHATA",
    "HORCHATA_CON_CHOCOLATE_ABUELITA",
    "PIÑA_COLADA",
    "PISTACHE",
    "FRESA_CON_LECHE",
    "MANGO_CON_LECHE",
    "NUEZ",
    "PLATANO",
    "CAFE_CON_LECHE"
    ]
    return Lista_de_sabores

def menu_sabores(Lista_de_sabores):
    
    Continuar_menu_sabores = True
    while Continuar_menu_sabores == True:
        borrar_pantalla()
        print ("\t\t.:: ACCIONES SABORES ::..")
        opcion_menu_sabores=input("\n\t1.- Ver lista de sabores \n\t2.- Agregar sabor \n\t3.- Eliminar sabor \n\t4.- Salir \n\n\tIngrese una opción: ")
        borrar_pantalla()
        match opcion_menu_sabores:
            case "1":
                
                print("\n\tLista de sabores disponibles:")
                for sabor in Lista_de_sabores:
                    sabor = sabor.lower()
                    sabor = sabor.replace("_", " ")
                    print(f"\t- Agua de {sabor}")
                esperar_tecla()
            case "2":
                nuevo_sabor = input("\n\tSin espacios ni caracteres especiales para espacios use _ \n\tIngrese el nombre del nuevo sabor : ").strip().upper()
                if len(nuevo_sabor) == 0:
                    print("\n⚠️Error: El nombre del sabor no puede estar vacío.⚠️")
                    esperar_tecla()
                    return menu_sabores()
                Lista_de_sabores.append(nuevo_sabor)
                nuevo_sabor = nuevo_sabor.lower()
                nuevo_sabor = nuevo_sabor.replace("_", " ")
                print(f"\n\tSabor '{nuevo_sabor}' agregado exitosamente.")
                esperar_tecla()
            case "3":
                sabor_a_eliminar = input("\n\tSin espacios ni caracteres especiales para espacios use _\n\tIngrese el nombre del sabor a eliminar: ").strip().upper()
                if sabor_a_eliminar in Lista_de_sabores:
                    Lista_de_sabores.remove(sabor_a_eliminar)
                    print(f"\n\tSabor '{sabor_a_eliminar}' eliminado exitosamente.")
                else:
                    print(f"\n\tSabor '{sabor_a_eliminar}' no encontrado.")
                esperar_tecla()
            case "4":
                Continuar_menu_sabores = False
            case _:
                print("\n⚠️Opción invalida, por favor intente nuevamente⚠️")
                esperar_tecla()

        
def ganancias_de_las_aguas(Costo_de_insumos_lista_por_litro, Costos_de_insumos_lista_por_objeto_total, lista_de_costos_de_insumos_especificos_por_sabor, lista_de_costos_de_insumos_especificos_por_objeto_total):
    azucar_bulto, costo_por_lata_de_carnetion, costo_por_lata_de_lechera, costo_bote_de_CMC, costo_de_sal, costo_de_vainilla, costo_de_esencia, costo_por_mensualidad_bebbia,costo_azucar_por_litro, costo_carnetion_por_litro, costo_lechera_por_litro, costo_CMC_por_litro, costo_sal_por_litro, costo_vainilla_por_litro, costo_esencia_por_litro, costo_por_dia_de_bebbia = obtencion_variables_costos_de_insumos(Costos_de_insumos_lista_por_objeto_total, Costo_de_insumos_lista_por_litro)
    costo_agua_base= costo_azucar_por_litro + costo_carnetion_por_litro + costo_lechera_por_litro + costo_sal_por_litro + costo_CMC_por_litro + costo_vainilla_por_litro + costo_esencia_por_litro
    return costo_agua_base

def ganancia_agua_de_pistache(costo_agua_base,lista_de_costos_de_insumos_especificos_por_sabor):
    for insumo, costo in lista_de_costos_de_insumos_especificos_por_sabor.items():
        costo_esencia_por_cada_litro_pistache = lista_de_costos_de_insumos_especificos_por_sabor["PISTACHE"]
    costo_agua_pistache = costo_agua_base + costo_esencia_por_cada_litro_pistache
    return costo_agua_pistache

def ganancia_agua_de_mango(costo_agua_base,lista_de_costos_de_insumos_especificos_por_sabor):
    for insumo, costo in lista_de_costos_de_insumos_especificos_por_sabor.items():
        costo_de_mango_por_litro = lista_de_costos_de_insumos_especificos_por_sabor["MANGO_CON_LECHE"]
    costo_agua_mango = costo_agua_base + costo_de_mango_por_litro
    return costo_agua_mango

def ganancia_agua_de_fresa(costo_agua_base,lista_de_costos_de_insumos_especificos_por_sabor):
    for insumo, costo in lista_de_costos_de_insumos_especificos_por_sabor.items():
        costo_de_fresa_por_litro = lista_de_costos_de_insumos_especificos_por_sabor["FRESA_CON_LECHE"]
    costo_agua_fresa = costo_agua_base + costo_de_fresa_por_litro
    return costo_agua_fresa

def ganancia_agua_de_horchata_con_chocolate_abuelita(costo_agua_base,lista_de_costos_de_insumos_especificos_por_sabor):
    for insumo, costo in lista_de_costos_de_insumos_especificos_por_sabor.items():
        costo_por_litro_chocolate_abuelita = lista_de_costos_de_insumos_especificos_por_sabor["HORCHATA_CON_CHOCOLATE_ABUELITA"]
    costo_agua_horchata_abuelita = costo_agua_base + costo_por_litro_chocolate_abuelita
    return costo_agua_horchata_abuelita



def venta_directa(datos, costo_agua_horchata_abuelita, costo_agua_base, costo_agua_pistache,costo_agua_fresa,costo_agua_mango):
    borrar_pantalla()
    Precio_venta_litro=35
    Precio_venta_medio=22
    print ("\t\t\n..:: VENTA DIRECTA ::..")

    from datetime import date
    
    Lista_de_sabores=lista_de_sabores()
    
    try:
        fecha_venta = date.today()
        datos.append(f"Venta Directa")
        datos.append(fecha_venta)
        print(f"\n\tFecha de venta: {fecha_venta.strftime('%d/%m/%Y')}")
        Porciones_vendidadas = int(input("\n\tIngrese la cantidad de porciones vendidas: "))  
        borrar_pantalla()
        acum_ganancia_real=0
        acum_costo=0
        acum_entrada_de_dinero=0
        for i in range(Porciones_vendidadas):
            a=0
            
            try:
                print("Ingrese los sabores vendidos")
                print("\n\tLista de sabores disponibles:")
                for sabor in Lista_de_sabores:
                    a+=1
                    sabor = sabor.lower()
                    sabor = sabor.replace("_", " ")
                    print(f"\t- {a}.-Agua de {sabor}")
                sabor_elegido=int(input("Escoge el sabor: "))
                sabor_elegido=sabor_elegido-1
                Venta_de_sabor_elegido=Lista_de_sabores[sabor_elegido]
                datos.append(Venta_de_sabor_elegido)
                if Venta_de_sabor_elegido =="PISTACHE":
                    costo=costo_agua_pistache
                elif Venta_de_sabor_elegido =="FRESA_CON_LECHE":
                    costo=costo_agua_fresa
                elif Venta_de_sabor_elegido =="HORCHATA_CON_CHOCOLATE_ABUELITA":
                    costo=costo_agua_horchata_abuelita
                elif Venta_de_sabor_elegido =="MANGO_CON_LECHE":
                    costo=costo_agua_mango
                else:
                    costo=costo_agua_base
                seleccion=input("Enter para continuar, (NO) para asignar\nSe uso la distribucion 2 litros y 4 medio?").upper()
                costo_botella_agua_1_litro=7.15
                costo_botella_agua_medio_litro=5.5
                if seleccion=="":
                    costo=costo+(2*costo_botella_agua_1_litro)+(4*costo_botella_agua_medio_litro)
                    entrada_de_dinero=(2*Precio_venta_litro)+(4*Precio_venta_medio)
                elif seleccion==("NO"):
                    Continuar=True
                    while Continuar==True:
                        try:
                            cuantas_de_litro=int(input("¿Cuantas Botellas De Litro Vendiste"))
                            cuantas_de_medio=int(input("¿Cuantas Botellas De Medio Litro Vendiste?"))
                            cantidad_agua_medio=cuantas_de_medio*500
                            cantidad_agua_litro=cuantas_de_litro*1000
                            verificacion=cantidad_agua_litro+cantidad_agua_medio
                            if verificacion==4000:
                                costo=costo+(cuantas_de_litro*costo_botella_agua_1_litro)+(cuantas_de_medio*costo_botella_agua_medio_litro)
                                entrada_de_dinero=(cuantas_de_litro*Precio_venta_litro)+(cuantas_de_medio*Precio_venta_medio)
                                Continuar=False
                            else:
                                print("los valores no completan la porcion porfavor verifique")
                        except ValueError:
                            input("Tiene que ser un numero")
                ganancia_real=entrada_de_dinero-costo
                acum_entrada_de_dinero=acum_entrada_de_dinero+entrada_de_dinero
                acum_costo=acum_costo+costo
                acum_ganancia_real=acum_ganancia_real+ganancia_real
                

                esperar_tecla()
                borrar_pantalla()
            except ValueError:
                print("\n⚠️Error: Entrada no válida. Por favor, ingrese un número válido.⚠️")
                esperar_tecla
        separador=(f"-"*40)
        datos.append(f"Entrada De Dinero: ${acum_entrada_de_dinero:.2f}")
        datos.append(f"Costo Total: ${acum_costo:.2f}")
        datos.append(f"Ganancia Real: ${acum_ganancia_real:.2f}")
        datos.append(separador)
        for i in datos:
            print(i)
        esperar_tecla()
        
        
    except ValueError:
        print("\n⚠️Error: Entrada no válida. Por favor, ingrese un número válido.⚠️")
        esperar_tecla()

def venta_mayoreo(datos, costo_agua_horchata_abuelita, costo_agua_base, costo_agua_pistache,costo_agua_fresa,costo_agua_mango):
    borrar_pantalla()
    Precio_venta_litro=32
    Precio_venta_medio=20
    print ("\t\t\n..:: VENTA MAYOREO ::..")

    from datetime import date
    
    Lista_de_sabores=lista_de_sabores()
    
    try:
        fecha_venta = date.today()
        datos.append(f"Venta Mayoreo")
        datos.append(fecha_venta)
        print(f"\n\tFecha de venta: {fecha_venta.strftime('%d/%m/%Y')}")
        Porciones_vendidadas = int(input("\n\tIngrese la cantidad de porciones vendidas: "))  
        borrar_pantalla()
        acum_ganancia_real=0
        acum_costo=0
        acum_entrada_de_dinero=0
        for i in range(Porciones_vendidadas):
            a=0
            
            try:
                print("Ingrese los sabores vendidos")
                print("\n\tLista de sabores disponibles:")
                for sabor in Lista_de_sabores:
                    a+=1
                    sabor = sabor.lower()
                    sabor = sabor.replace("_", " ")
                    print(f"\t- {a}.-Agua de {sabor}")
                sabor_elegido=int(input("Escoge el sabor: "))
                sabor_elegido=sabor_elegido-1
                Venta_de_sabor_elegido=Lista_de_sabores[sabor_elegido]
                datos.append(Venta_de_sabor_elegido)
                if Venta_de_sabor_elegido =="PISTACHE":
                    costo=costo_agua_pistache
                elif Venta_de_sabor_elegido =="FRESA_CON_LECHE":
                    costo=costo_agua_fresa
                elif Venta_de_sabor_elegido =="HORCHATA_CON_CHOCOLATE_ABUELITA":
                    costo=costo_agua_horchata_abuelita
                elif Venta_de_sabor_elegido =="MANGO_CON_LECHE":
                    costo=costo_agua_mango
                else:
                    costo=costo_agua_base
                seleccion=input("Enter para continuar, (NO) para asignar\nSe uso la distribucion 2 litros y 4 medio?").upper()
                costo_botella_agua_1_litro=7.15
                costo_botella_agua_medio_litro=5.5
                if seleccion=="":
                    costo=costo+(2*costo_botella_agua_1_litro)+(4*costo_botella_agua_medio_litro)
                    entrada_de_dinero=(2*Precio_venta_litro)+(4*Precio_venta_medio)
                elif seleccion==("NO"):
                    Continuar=True
                    while Continuar==True:
                        try:
                            cuantas_de_litro=int(input("¿Cuantas Botellas De Litro Vendiste"))
                            cuantas_de_medio=int(input("¿Cuantas Botellas De Medio Litro Vendiste?"))
                            cantidad_agua_medio=cuantas_de_medio*500
                            cantidad_agua_litro=cuantas_de_litro*1000
                            verificacion=cantidad_agua_litro+cantidad_agua_medio
                            if verificacion==4000:
                                costo=costo+(cuantas_de_litro*costo_botella_agua_1_litro)+(cuantas_de_medio*costo_botella_agua_medio_litro)
                                entrada_de_dinero=(cuantas_de_litro*Precio_venta_litro)+(cuantas_de_medio*Precio_venta_medio)
                                Continuar=False
                            else:
                                print("los valores no completan la porcion porfavor verifique")
                        except ValueError:
                            input("Tiene que ser un numero")
                ganancia_real=entrada_de_dinero-costo
                acum_entrada_de_dinero=acum_entrada_de_dinero+entrada_de_dinero
                acum_costo=acum_costo+costo
                acum_ganancia_real=acum_ganancia_real+ganancia_real
                

                esperar_tecla()
                borrar_pantalla()
            except ValueError:
                print("\n⚠️Error: Entrada no válida. Por favor, ingrese un número válido.⚠️")
                esperar_tecla
        separador=(f"-"*40)
        datos.append(f"Entrada De Dinero: ${acum_entrada_de_dinero:.2f}")
        datos.append(f"Costo Total: ${acum_costo:.2f}")
        datos.append(f"Ganancia Real: ${acum_ganancia_real:.2f}")
        datos.append(separador)
        for i in datos:
            print(i)
        esperar_tecla()
        
        
    except ValueError:
        print("\n⚠️Error: Entrada no válida. Por favor, ingrese un número válido.⚠️")
        esperar_tecla()
        
    

def menu_registrar_ventas(datos, costo_agua_horchata_abuelita, costo_agua_base, costo_agua_pistache,costo_agua_fresa,costo_agua_mango):
    borrar_pantalla()
    print ("\t\t\n..:: REGISTRAR VENTAS ::..")
    decision_regreso_o_continuar_ventas=input("\n\t1.- Registrar venta de agua directa \n\t2.- Registrar venta de agua a mayoreo \n\t3.- Salir \n\n\tIngrese una opción: ")
    match decision_regreso_o_continuar_ventas:
        case "1":
            venta_directa(datos, costo_agua_horchata_abuelita, costo_agua_base, costo_agua_pistache,costo_agua_fresa,costo_agua_mango)
        case "2":
            venta_mayoreo(datos, costo_agua_horchata_abuelita, costo_agua_base, costo_agua_pistache,costo_agua_fresa,costo_agua_mango)
        case "3":
            return "salir"
        case _:
            print("\n⚠️Opción invalida, por favor intente nuevamente⚠️")
            menu_registrar_ventas()


