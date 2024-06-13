from tkinter import Frame
from customtkinter import CTkImage, CTkLabel, CTkEntry
from PIL import Image

def entryUsers(father, fontRezise, iconName, placeholder, row):

    entryUsersC = Frame(father, bg="#FFF") #contenedor de espacio password
    entryUsersC.grid(row=row, column=0, sticky="nswe", pady=20)
    entryUsersC.columnconfigure(0, weight=1)

    entryUsersCC = Frame(entryUsersC, bg="#FFF") #cpntenedor icon/entry
    entryUsersCC.grid(row=0, column=0, sticky="nswe")
    entryUsersCC.columnconfigure(0, weight=0)
    entryUsersCC.columnconfigure(1,weight=1)

    icon= CTkImage(light_image=Image.open(iconName), dark_image=Image.open(iconName), size=(15,15))

    iconEntryUsersLabel = CTkLabel(entryUsersCC, bg_color="#FFF", image=icon, text="")
    iconEntryUsersLabel.grid(row=0, column=0, padx=5)

    entryUsersCCEntry = CTkEntry(entryUsersCC, font=fontRezise, placeholder_text=placeholder, placeholder_text_color="gray89", text_color="gray23", border_width=0, fg_color="#FFF")
    entryUsersCCEntry.grid(row=0, column=1, sticky="nswe")

    linearEntryUsersC = Frame(entryUsersC, bg="gray89", height=1) #linea decorativa debajo
    linearEntryUsersC.grid(row=1, column=0, sticky="nswe")

    return entryUsersCCEntry