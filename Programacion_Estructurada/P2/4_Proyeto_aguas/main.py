import Agua
import os 



def main():
    datos=[]
    Lista_de_sabores = Agua.lista_de_sabores()
    opc=True
    azucar_bulto, costo_por_lata_de_carnetion, costo_por_lata_de_lechera,costo_bote_de_CMC, costo_de_sal, costo_de_vainilla, costo_de_esencia, costo_por_mensualidad_bebbia = Agua.reiniciar_costos_a_valores_determinados()
    costo_por_dia_de_bebbia, costo_por_mensualidad_bebbia=Agua.asignacion_por_mensualidad_bebbia(costo_por_mensualidad_bebbia)
    costo_esencia_por_litro_promedio, costo_de_esencia=Agua.asignacion_esencia_por_litro(costo_de_esencia)
    costo_de_vainilla_por_litro, costo_de_vainilla=Agua.asignacion_de_vainilla_por_litro(costo_de_vainilla)
    costo_de_sal_por_litro, costo_de_sal=Agua.asignacion_de_sal_por_litro(costo_de_sal)
    costo_CMC_por_litro, costo_bote_de_CMC=Agua.asignacion_CMC_por_litro(costo_bote_de_CMC)
    costo_de_lechera_por_litro, costo_por_lata_de_lechera=Agua.asignacion_lechera_por_litro(costo_por_lata_de_lechera)
    costo_carnetion_por_litro, costo_por_lata_de_carnetion=Agua.asignacion_carnetion_por_litro(costo_por_lata_de_carnetion)
    costo_azucar_por_litro, azucar_bulto=Agua.asignacion_azucar_por_litro(azucar_bulto)
    Costo_de_insumos_lista_por_litro, Costos_de_insumos_lista_por_objeto_total = Agua.asignacion_costos_de_insumos(costo_azucar_por_litro, costo_carnetion_por_litro, costo_de_lechera_por_litro, costo_CMC_por_litro, costo_de_sal_por_litro, costo_de_vainilla_por_litro, costo_esencia_por_litro_promedio, costo_por_mensualidad_bebbia , costo_por_dia_de_bebbia, azucar_bulto, costo_por_lata_de_carnetion, costo_por_lata_de_lechera, costo_bote_de_CMC, costo_de_sal, costo_de_vainilla, costo_de_esencia)

    costo_de_esencia_de_pistache, costo_de_charola_de_fresa, costo_de_mango_por_kilo, costo_por_lata_de_chocolate_abuelita, costo_por_lata_de_cafe = Agua.restablecer_costos_especificos_por_sabor()
    costo_esencia_por_cada_litro_pistache, costo_de_esencia_de_pistache = Agua.Asignacion_costos_especificos_pistache(costo_de_esencia_de_pistache)
    costo_de_fresa_por_litro , costo_de_charola_de_fresa = Agua.Asignacion_costos_especificos_fresa(costo_de_charola_de_fresa)
    costo_de_mango_por_litro , costo_de_mango_por_kilo = Agua.Asignacion_costos_especificos_mango(costo_de_mango_por_kilo)
    costo_por_litro_chocolate_abuelita , costo_por_lata_de_chocolate_abuelita = Agua.Asignacion_costos_especificos_horchata_con_chocolate_abuelita(costo_por_lata_de_chocolate_abuelita)
    costo_por_litro_cafe , costo_por_lata_de_cafe = Agua.Asignacion_costos_especificos_cafe_con_leche(costo_por_lata_de_cafe)
    lista_de_costos_de_insumos_especificos_por_sabor, lista_de_costos_de_insumos_especificos_por_objeto_total = Agua.Asignacion_lista_costos_especificos_por_sabor(costo_esencia_por_cada_litro_pistache, costo_de_fresa_por_litro, costo_de_mango_por_litro, costo_por_litro_chocolate_abuelita, costo_por_litro_cafe, costo_por_lata_de_chocolate_abuelita, costo_por_lata_de_cafe, costo_de_charola_de_fresa, costo_de_mango_por_kilo, costo_de_esencia_de_pistache)

    costo_agua_base=Agua.ganancias_de_las_aguas(Costo_de_insumos_lista_por_litro, Costos_de_insumos_lista_por_objeto_total, lista_de_costos_de_insumos_especificos_por_sabor, lista_de_costos_de_insumos_especificos_por_objeto_total)
    costo_agua_horchata_abuelita=Agua.ganancia_agua_de_horchata_con_chocolate_abuelita(costo_agua_base,lista_de_costos_de_insumos_especificos_por_sabor)
    costo_agua_pistache=Agua.ganancia_agua_de_pistache(costo_agua_base,lista_de_costos_de_insumos_especificos_por_sabor)
    costo_agua_mango=Agua.ganancia_agua_de_mango(costo_agua_base,lista_de_costos_de_insumos_especificos_por_sabor)
    costo_agua_fresa=Agua.ganancia_agua_de_fresa(costo_agua_base,lista_de_costos_de_insumos_especificos_por_sabor)
    while opc:
        
        opcion=Agua.menu_principal()
        match opcion:
                case "1":
                    Agua.menu_registrar_ventas(datos, costo_agua_horchata_abuelita, costo_agua_base, costo_agua_pistache,costo_agua_fresa,costo_agua_mango)
                    
                case "2":
                    Agua.menu_costos_insumos(Costo_de_insumos_lista_por_litro, Costos_de_insumos_lista_por_objeto_total, lista_de_costos_de_insumos_especificos_por_sabor, lista_de_costos_de_insumos_especificos_por_objeto_total)
                case "3":
                    Agua.menu_sabores(Lista_de_sabores)
                case "4":
                    opc=False
                
                    
                case _:
                    os.system("cls") 
                    input("⚠️Opción invalida vuelva a intentarlo ... por favor⚠️")
                    
if __name__ == "__main__":
    main()