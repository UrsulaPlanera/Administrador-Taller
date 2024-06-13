from .getData import *

from src.components.MBox import MBox
from src.views.showItem import showItem

def getSearchValidation(father, search1, search2, search3, font):
            select1 = search1.get().upper()
            select2 = search2.get().upper()
            select3 = search3.get().upper()

            for widget in father.winfo_children():
                widget.destroy()

            try:
                if(select1 == "BUSCAR"):
                    MBox("error", "no se han realizado busquedas")

                elif(select1 == "CLIENTES" or select1 == "INSUMOS") and (select2 == "SELECCIONAR") and (len(select3) == 0):
                    response = getData(select1)

                    typeFor = ""
                    if select1 == "CLIENTES":
                        typeFor = "CLIENT"
                    elif select1 == "INSUMOS":
                        typeFor = "SUPPLY"

                    if(len(response) == 0):
                        MBox("error", "no se han encontrado coincidencias.")
                    else:
                        cont = 0
                        for register in response:
                            showItem(father, font, cont, typeFor, register[0], register[1], register[2], register[3], register[4],  register[5], register[6])
                            cont +=1

                elif(select1 == "CLIENTES" or select1=="INSUMOS") and (select2 =="SELECCIONAR") and (len(select3) > 0):
                    MBox("error", "debe clasificar la busqueda antes de continuar")
                
                elif(select1 == "CLIENTES") and (select2 =="PATENTE" or select2 == "NOMBRE") and (len(select3) > 0):
                    typeFor="CLIENT"
                    response = getForValue(select1, select2, select3)
                    if(len(response) == 0):
                        MBox("error", "no se han encontrado coincidencias.")
                    else:
                        cont = 0
                        for register in response:
                            showItem(father, font, cont, typeFor, register[0], register[1], register[2], register[3], register[4],  register[5], register[6])
                            cont +=1

                elif(select1 == "INSUMOS") and (select2 =="NOMBRE" or select2 == "STOCK") and (len(select3) > 0):
                    if(select2=="NOMBRE"):
                        select2="INSUMO_NOMBRE"
                    typeFor="SUPPLY"
                    response = getForValue(select1, select2, select3)
                    if(len(response) == 0):
                        MBox("error", "no se han encontrado coincidencias.")
                    else:
                        cont = 0
                        for register in response:
                            showItem(father, font, cont, typeFor, register[0], register[1], register[2], register[3], register[4],  register[5], register[6])
                            cont +=1

            except TypeError as e:
                print(e)