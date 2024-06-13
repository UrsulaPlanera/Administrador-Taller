from customtkinter import CTkImage, CTkLabel, CTkEntry, CTkFrame, CTkToplevel, CTkButton, CTkTextbox
from PIL import Image
from tkcalendar import Calendar

from ..components.enterpriseLogo import enterpriseLogo
from  src.components.MBox import MBox
from ..components.calendar import showCalendar

from dbconection.validationNewEntry import validationNewEntry

def showNewService():

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


    showEditC.title("REGISTRAR NUEVO SERVICE")
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
        
    container.rowconfigure(2, weight=1)
    container.columnconfigure(0, weight=1)

    carC = CTkFrame(container, fg_color="#FFF")
    carC.grid(row=0, column=0, sticky="nswe")
    carC.columnconfigure(0, weight=1)
    carC.columnconfigure(1, weight=1)
    carC.columnconfigure(2, weight=1)

    """patent"""

    patentSFFrame = CTkFrame(carC, fg_color="#FFF")
    patentSFFrame.grid(row=0, column=0, sticky="nswe", padx=3)
    patentSFFrame.columnconfigure(0, weight=1)

    patentSFLabel = CTkLabel(patentSFFrame, text="PATENTE", font=fontRezise,text_color="gray23")
    patentSFLabel.grid(row=0, column=0, sticky="w")

    patentSFEntry = CTkEntry(patentSFFrame, fg_color="#FFF", text_color="gray23",  font=fontRezise, border_color="gray89", border_width=1, placeholder_text="PATENTE", placeholder_text_color="gray89")
    patentSFEntry.grid(row=1, column=0, sticky="nswe")

    """brand"""

    brandSFFrame = CTkFrame(carC, fg_color="#FFF")
    brandSFFrame.grid(row=0, column=1, sticky="nswe", padx=3)
    brandSFFrame.columnconfigure(0, weight=1)

    brandSFLabel = CTkLabel(brandSFFrame, text="MARCA", font=fontRezise,text_color="gray23")
    brandSFLabel.grid(row=0, column=0, sticky="w")

    brandSFEntry = CTkEntry(brandSFFrame, fg_color="#FFF", text_color="gray23",  font=fontRezise, border_color="gray89", border_width=1, placeholder_text="MARCA", placeholder_text_color="gray89")
    brandSFEntry.grid(row=1, column=0, sticky="nswe")

    """model"""
    modelSFFrame = CTkFrame(carC, fg_color="#FFF")
    modelSFFrame.grid(row=0, column=2, sticky="nswe", padx=3)
    modelSFFrame.columnconfigure(0, weight=1)

    modelSFLabel = CTkLabel(modelSFFrame, text="MODELO", font=fontRezise,text_color="gray23")
    modelSFLabel.grid(row=0, column=0, sticky="w")

    modelSFEntry = CTkEntry(modelSFFrame, fg_color="#FFF", text_color="gray23",  font=fontRezise, border_color="gray89", border_width=1, placeholder_text="MODELO", placeholder_text_color="gray89")
    modelSFEntry.grid(row=1, column=0, sticky="nswe")

    dataC = CTkFrame(container, fg_color="#FFF")
    dataC.grid(row=1, column=0, sticky="nswe")
    dataC.columnconfigure(0, weight=1)
    dataC.columnconfigure(1, weight=1)
    dataC.columnconfigure(2, weight=1)

    """nameframe"""
    nameSFFrame = CTkFrame(dataC, fg_color="#FFF")
    nameSFFrame.grid(row=0, column=0, sticky="nswe", padx=3)
    nameSFFrame.columnconfigure(0, weight=1)

    nameSFLabel = CTkLabel(nameSFFrame, text="NOMBRE", font=fontRezise,text_color="gray23")
    nameSFLabel.grid(row=0, column=0, sticky="w")

    nameSFEntry = CTkEntry(nameSFFrame, fg_color="#FFF", text_color="gray23",  font=fontRezise, border_color="gray89", border_width=1, placeholder_text="NOMBRE", placeholder_text_color="gray89")
    nameSFEntry.grid(row=1, column=0, sticky="nswe")

    """dateframe"""

    dateFrame = CTkFrame(dataC, fg_color="#FFF")
    dateFrame.grid(row=0, column=1, sticky="nswe")

    dateLabel = CTkLabel(dateFrame, fg_color="#FFF", text_color="gray23", font=fontRezise, text="FECHA")
    dateLabel.grid(row=0, column=0, sticky="w")

    dateEntry= CTkEntry(dateFrame, placeholder_text="FECHA", text_color="gray23", placeholder_text_color="gray89", font=fontRezise, fg_color="#FFF", border_color="gray89", border_width=1)
    dateEntry.grid(row=1,column=0, sticky="nswe", padx=2)

    dateBtn = CTkButton(dateFrame, text="SELECCIONAR FECHA", command=lambda:showCalendar(dateEntry, fontRezise), fg_color="gray89", text_color="#FFF", hover_color="#029BD5")
    dateBtn.grid(row=1, column=1)
    dateBtn.configure(cursor="hand2")

    descriptionFrame = CTkFrame(container, fg_color="#FFF")
    descriptionFrame.grid(row=2, column=0, sticky="nswe")
    descriptionFrame.columnconfigure(0, weight=1)
    descriptionFrame.rowconfigure(1, weight=1)
    
    descriptionLabel = CTkLabel(descriptionFrame, fg_color="#FFF", text="DESCRIPCION", text_color="gray23", font=fontRezise)
    descriptionLabel.grid(row=0, column=0, sticky="w")
    descriptionEntry= CTkTextbox(descriptionFrame, fg_color="#FFF", font=fontRezise, text_color="gray23", border_color="gray89", border_width=1, scrollbar_button_color="gray89", scrollbar_button_hover_color="#029BD5")
    descriptionEntry.grid(row=1, column=0, sticky="nswe")
        

    def saveNewEntry():
        type = "CLIENT"
        val1 = patentSFEntry.get()
        val2 = brandSFEntry.get()
        val3 = modelSFEntry.get()
        val4 = nameSFEntry.get()
        val5 = dateEntry.get()
        val6 = descriptionEntry.get(1.0, "end").strip()
        if (len(val1) > 0) and (len(val2) > 0) and (len(val3) > 0) and (len(val5) > 0) and (len(val6) > 0):
            name = val4
            if(len(val4) == 0):
                name="NO AGREGADO"
            validationNewEntry(type, val1, val2, val3, name, val5, val6)
        else:
            MBox("error", "rellene todos los campos.")


    saveBtn = CTkButton(showEditC, command=lambda:saveNewEntry(), font=fontRezise, fg_color="gray89", text="GUARDAR", text_color="#FFF", hover_color="#029BD5", height=40)
    saveBtn.grid(row=2, column=0, sticky="nswe", pady=3, padx=20)
    saveBtn.configure(cursor="hand2")