from customtkinter import CTkToplevel, CTkLabel, CTkFrame, CTkImage, CTkComboBox, CTkEntry, CTkButton
from PIL import Image
from dbconection.validationPrinter import validationToPrintCustomerHistory, validationToPrintSupplies

from ..components.MBox import MBox

def showPrint():
    
    showPrintC = CTkToplevel(fg_color="#FFF")
    showPrintC.grab_set()

    showPrintC.minsize(400,300)
    showPrintC.maxsize(400,300)

    width= showPrintC.winfo_screenwidth()

    fontRezise = ()
    if(width <= 1280):
        fontRezise=("Roboto", 9)
    elif(width > 1280 and width < 1400):
        fontRezise=("Roboto", 12)
    else:
        fontRezise=("Roboto", 14)


    showPrintC.title("GENERAR PDF")
    showPrintC.after(200, lambda: showPrintC.iconbitmap("static/ico.ico"))
    showPrintC.columnconfigure(0, weight=1)
    showPrintC.rowconfigure(0, weight=0)

    titleFrame = CTkFrame(showPrintC, fg_color="#FFF")
    titleFrame.grid(row=0, column=0, sticky="nswe")
    titleFrame.columnconfigure(0, weight=1)
    titleFrame.rowconfigure(0, weight=1)

    icon = CTkImage(light_image=Image.open("static/printer.png"), dark_image=Image.open("static/printer.png"), size=(24,24))
    titleLabel = CTkLabel(titleFrame, image=icon, text="  GENERAR PDF", font=fontRezise, fg_color="#FFF", text_color="gray23", compound="left")
    titleLabel.grid(row=0, column=0, sticky="nswe", pady=40)

    typeFrame=CTkFrame(showPrintC, fg_color="#FFF")
    typeFrame.grid(row=1, column=0, sticky="nswe", padx=50)
    typeFrame.columnconfigure(0, weight=1)

    typeLabel = CTkLabel(typeFrame, text="TIPO", text_color="gray23", fg_color="#FFF", font=fontRezise)
    typeLabel.grid(row=0, column=0, sticky="w")

    def activateOption(choice):
        if choice == "INSUMOS":
            patentEntry.delete(0, "end")
            patentEntry.configure(state="disabled")
        else:
            patentEntry.configure(state="normal")

    typeCombobox = CTkComboBox(typeFrame, values=["CLIENTES", "INSUMOS"], state="readonly", command=activateOption, font=fontRezise, text_color="gray23", border_color="gray89", fg_color="#FFF", button_color="gray89", button_hover_color="#029BD5", corner_radius=0, dropdown_fg_color="#FFF", dropdown_text_color="gray23", dropdown_font=fontRezise, dropdown_hover_color="#029BD5")
    typeCombobox.grid(row=1, column=0, sticky="nswe")
    typeCombobox.set("CLIENTES")
    typeCombobox.configure(cursor="hand2")

    patentFrame = CTkFrame(showPrintC, fg_color="#FFF")
    patentFrame.grid(row=2, column=0, sticky="nswe", padx=50)
    patentFrame.columnconfigure(0, weight=1)

    patentLabel = CTkLabel(patentFrame, text="PATENTE", text_color="gray23", font=fontRezise, fg_color="#FFF")
    patentLabel.grid(row=0, column=0, sticky="w")

    patentEntry= CTkEntry(patentFrame, placeholder_text="PATENTE", text_color="gray23", placeholder_text_color="gray89", fg_color="#FFF", border_color="gray89", border_width=1)
    patentEntry.grid(row=1, column=0, sticky="nswe")

    def getValues():
        typeCombo = typeCombobox.get()
        typeEntry = patentEntry.get()
        if (typeCombo == "CLIENTES") and (len(typeEntry) >0):
            validationToPrintCustomerHistory(typeEntry)
        elif (typeCombo == "CLIENTES") and (len(typeEntry) ==0):
            MBox("error", "debe ingresar una patente válida.")
        elif(typeCombo == "INSUMOS"):
            validationToPrintSupplies()

    btnTrigger = CTkButton(showPrintC, text="GENERAR", command=lambda:getValues(), text_color="#FFF", fg_color="gray89", corner_radius=0, hover_color="#029BD5")
    btnTrigger.grid(row=3, column=0, sticky="nswe", padx=50, pady=20)

    showPrintC.mainloop()