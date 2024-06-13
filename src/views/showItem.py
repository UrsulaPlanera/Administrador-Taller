from customtkinter import CTkLabel, CTkFrame, CTkImage, CTkButton
from PIL import Image

from .editService import editService
from .editSupply import editSupply
from dbconection.validationPrinter import validationPrintCustomerSimple, validationToPrintOnlySupply

from ..components.acceptDelete import acceptDelete

showItemC = None

def item(column, name, parameter, font):
    nameMayus = name.upper()
    color = "gray23"

    if(nameMayus == "PATENTE") or (nameMayus == "NOMBRE DE INSUMO"):
        color = "#029BD5"

    itemLabel = CTkLabel(showItemC, fg_color="#FFF", text_color=color, text=f"{nameMayus}: {parameter}", font=font)
    itemLabel.grid(row=0, column=column)

    return nameMayus

def showItem(father, font, row, type, id, parameter1, parameter2, parameter3, parameter4,  parameter5, parameter6):

    typeMayus = type.upper()

    try:
        global showItemC
        showItemC = CTkFrame(father, fg_color="#FFF", border_width=1, border_color="gray23", corner_radius=0)
        showItemC.grid(row=row, column=0, sticky="nswe", padx=3, pady=3)
        showItemC.columnconfigure(0, weight=1)
        showItemC.columnconfigure(1, weight=1)
        showItemC.columnconfigure(2, weight=1)
        showItemC.columnconfigure(3, weight=1)
        showItemC.columnconfigure(4, weight=1)
        showItemC.columnconfigure(5, weight=1)
        showItemC.columnconfigure(6, weight=0)

        if(typeMayus == "CLIENT"):
            """patente"""
            patent = item(0, "patente", parameter1, font)

            """marca"""
            brand = item(1, "marca", parameter2, font)

            """modelo"""
            model = item(2, "modelo",parameter3, font)

            """name"""
            name = item(3, "nombre", parameter4,  font)

            """fecha"""
            date = item(4, "fecha", parameter5, font)

            """decripcion"""
            description = CTkLabel(showItemC, fg_color="#FFF", text_color="gray23", text=parameter6, font=font, wraplength=400)
            description.grid(row=0, column=5, padx=3, pady=3, sticky="nswe")
        
        elif(typeMayus == "SUPPLY"):

            supplyName = item(0, "nombre de insumo", parameter1, font)

            priceUnity = item(1, "precio de unidad", parameter2, font)

            priceSale = item(2, "precio de venta", parameter3, font)

            revenue = item(3, "ganancia", parameter4, font)

            inversion = item(4, "dinero invertido", parameter5, font)

            stock = item(5, "stock", parameter6, font)

        """buttons"""
        def custom():
            if typeMayus == "CLIENT": 
                editService(id, parameter1, parameter2, parameter3, parameter4, parameter5, parameter6)
            elif typeMayus == "SUPPLY":
                editSupply(id, parameter1, parameter2, parameter3, parameter4, parameter5, parameter6)

        def delete():
            acceptDelete(font, typeMayus, id, parameter1, parameter2, parameter3, parameter4, parameter5, parameter6)

        def print():
            if typeMayus == "CLIENT":
                validationPrintCustomerSimple(id)
            elif typeMayus == "SUPPLY":
                validationToPrintOnlySupply(id)

        buttonsFrame = CTkFrame(showItemC, fg_color="#FFF")
        buttonsFrame.grid(row=0, column=6, sticky="nswe", padx=3, pady=3)

        iconPrinter = CTkImage(light_image=Image.open("static/printerwhite.png"), dark_image=Image.open("static/printerwhite.png"), size=(15,15))
        btnPrinter = CTkButton(buttonsFrame, command=lambda:print(), image=iconPrinter, text="", fg_color="gray89", hover_color="#63B630", width=50)
        btnPrinter.grid(row=0, column=0, pady=2)
        btnPrinter.configure(cursor="hand2")

        iconEdit = CTkImage(light_image=Image.open("static/pen.png"), dark_image=Image.open("static/pen.png"), size=(15,15))
        btnEdit = CTkButton(buttonsFrame, command=lambda:custom(), image=iconEdit, text="", fg_color="gray89", hover_color="SteelBlue2", width=50)
        btnEdit.grid(row=1, column=0, pady=2)
        btnEdit.configure(cursor="hand2")

        iconTrash = CTkImage(light_image=Image.open("static/trash.png"), dark_image=Image.open("static/trash.png"), size=(15,15))
        btnTrash = CTkButton(buttonsFrame, command=lambda:delete(), image=iconTrash, text="", fg_color="gray89", hover_color="firebrick3", width=50)
        btnTrash.grid(row=2, column=0, pady=2)
        btnTrash.configure(cursor="hand2")

    except TypeError as error:
        print(error)