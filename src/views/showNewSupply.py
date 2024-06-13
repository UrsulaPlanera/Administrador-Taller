from customtkinter import CTkImage, CTkLabel, CTkEntry, CTkFrame, CTkToplevel, CTkButton, CTkTextbox
from PIL import Image

from ..components.enterpriseLogo import enterpriseLogo

from dbconection.validationNewEntry import validationNewEntry

from src.components.MBox import MBox

def showNewSupply():

    showEditC = CTkToplevel(fg_color="#FFF")
    showEditC.grab_set()

    showEditC.minsize(700, 500)
    showEditC.maxsize(700,500)

    width= showEditC.winfo_screenwidth()

    fontRezise = ()
    if(width <= 1280):
        fontRezise=("Roboto", 9)
    elif(width > 1280 and width < 1400):
        fontRezise=("Roboto", 12)
    else:
        fontRezise=("Roboto", 14)


    showEditC.title("INGRESAR NUEVO INSUMO")
    showEditC.after(200, lambda: showEditC.iconbitmap("static/ico.ico"))
        
    showEditC.rowconfigure(0, weight=0)
    showEditC.rowconfigure(1, weight=1)
    showEditC.columnconfigure(0, weight=1)

    header = CTkFrame(showEditC, fg_color="#FFF")
    header.grid(row=0, column=0, sticky="nswe", padx=20)
    header.columnconfigure(0, weight=1)
    header.columnconfigure(1, weight=1)

    enterpriseLogo(header, 0, "w")

    iconPenBlue = CTkImage(light_image=Image.open("static/penBlue.png"), dark_image=Image.open("static/penBlue.png"), size=(24,24))
    iconPenBlueLabel = CTkLabel(header, image=iconPenBlue, text="", fg_color="#FFF")
    iconPenBlueLabel.grid(row=0, column=1, sticky="e")

    container = CTkFrame(showEditC, border_width=0, fg_color="#FFF")
    container.grid(row=1, column=0, sticky="nswe", padx=20)
        
    container.columnconfigure(0, weight=1)
    container.columnconfigure(1, weight=1)
    container.rowconfigure(0, weight=1)
    container.rowconfigure(1, weight=1)
    container.rowconfigure(2, weight=1)

    """nombre"""
    nameSupplyFrame = CTkFrame(container, fg_color="#FFF")
    nameSupplyFrame.grid(row=0, column=0, sticky="nswe", padx=3)
    nameSupplyFrame.columnconfigure(0, weight=1)

    nameSupplyLabel = CTkLabel(nameSupplyFrame, text="NOMBRE DE INSUMO", font=fontRezise,text_color="gray23")
    nameSupplyLabel.grid(row=0, column=0, sticky="w")

    nameSupplyEntry = CTkEntry(nameSupplyFrame, fg_color="#FFF", text_color="gray23",  font=fontRezise, border_color="gray89", border_width=1, placeholder_text="NOMBRE DE INSUMO", placeholder_text_color="gray89")
    nameSupplyEntry.grid(row=1, column=0, sticky="nswe")

    """costo unidad"""
    priceUnityFrame = CTkFrame(container, fg_color="#FFF")
    priceUnityFrame.grid(row=0, column=1, sticky="nswe", padx=3)
    priceUnityFrame.columnconfigure(0, weight=1)

    priceUnityLabel = CTkLabel(priceUnityFrame, text="PRECIO DE UNIDAD", font=fontRezise,text_color="gray23")
    priceUnityLabel.grid(row=0, column=0, sticky="w")

    priceUnityEntry = CTkEntry(priceUnityFrame, fg_color="#FFF", text_color="gray23",  font=fontRezise, border_color="gray89", border_width=1, placeholder_text="PRECIO DE UNIDAD", placeholder_text_color="gray89")
    priceUnityEntry.grid(row=1, column=0, sticky="nswe")

    """precio venta"""
    priceSaleFrame = CTkFrame(container, fg_color="#FFF")
    priceSaleFrame.grid(row=1, column=0, sticky="nswe", padx=3)
    priceSaleFrame.columnconfigure(0, weight=1)

    priceSaleLabel = CTkLabel(priceSaleFrame, text="PRECIO DE VENTA", font=fontRezise,text_color="gray23")
    priceSaleLabel.grid(row=0, column=0, sticky="w")

    priceSaleEntry = CTkEntry(priceSaleFrame, fg_color="#FFF", text_color="gray23",  font=fontRezise, border_color="gray89", border_width=1, placeholder_text="PRECIO DE VENTA", placeholder_text_color="gray89")
    priceSaleEntry.grid(row=1, column=0, sticky="nswe")

    """revenue"""
    revenueFrame = CTkFrame(container, fg_color="#FFF")
    revenueFrame.grid(row=1, column=1, sticky="nswe", padx=3)
    revenueFrame.columnconfigure(0, weight=1)

    revenueLabel = CTkLabel(revenueFrame, text="GANACIA", font=fontRezise,text_color="gray23")
    revenueLabel.grid(row=0, column=0, sticky="w")

    revenueEntry = CTkEntry(revenueFrame, fg_color="#FFF", text_color="gray23",  font=fontRezise, border_color="gray89", border_width=1, placeholder_text="GANACIA", placeholder_text_color="gray89")
    revenueEntry.grid(row=1, column=0, sticky="nswe")
    
    """inversion"""
    inversionFrame = CTkFrame(container, fg_color="#FFF")
    inversionFrame.grid(row=2, column=0, sticky="nswe", padx=3)
    inversionFrame.columnconfigure(0, weight=1)

    inversionLabel = CTkLabel(inversionFrame, text="DINERO INVERTIDO", font=fontRezise,text_color="gray23")
    inversionLabel.grid(row=0, column=0, sticky="w")

    inversionEntry = CTkEntry(inversionFrame, fg_color="#FFF", text_color="gray23",  font=fontRezise, border_color="gray89", border_width=1, placeholder_text="DINERO INVERTIDO", placeholder_text_color="gray89")
    inversionEntry.grid(row=1, column=0, sticky="nswe")

    """stock"""
    stockFrame = CTkFrame(container, fg_color="#FFF")
    stockFrame.grid(row=2, column=1, sticky="nswe", padx=3)
    stockFrame.columnconfigure(0, weight=1)

    stockLabel = CTkLabel(stockFrame, text="STOCK", font=fontRezise,text_color="gray23")
    stockLabel.grid(row=0, column=0, sticky="w")

    stockEntry = CTkEntry(stockFrame, fg_color="#FFF", text_color="gray23",  font=fontRezise, border_color="gray89", border_width=1, placeholder_text="STOCK", placeholder_text_color="gray89")
    stockEntry.grid(row=1, column=0, sticky="nswe")

    def saveNewEntry():
        type = "SUPPLY"
        val1 = nameSupplyEntry.get()
        val2 = priceUnityEntry.get()
        val3 = priceSaleEntry.get()
        val4 = revenueEntry.get()
        val5 = inversionEntry.get()
        val6 = stockEntry.get()
        if (len(val1) > 0) and (len(val2) > 0) and (len(val3) > 0) and (len(val4) > 0) and (len(val5) > 0) and (len(val6) > 0):
            validationNewEntry(type, val1, val2, val3, val4, val5, val6)
        else:
            MBox("error", "rellene todos los campos.")

    saveBtn = CTkButton(showEditC, command=lambda:saveNewEntry(), font=fontRezise, fg_color="gray89", text="GUARDAR", text_color="#FFF", hover_color="#029BD5", height=40)
    saveBtn.grid(row=2, column=0, sticky="nswe", pady=3, padx=20)
    saveBtn.configure(cursor="hand2")