from customtkinter import CTkImage, CTkButton
from PIL import Image

from ..views.showNewService import showNewService
from ..views.showNewSupply import showNewSupply
from ..views.showPrint import showPrint

def show(type):
    if type == "client":
        showNewService()
    elif type == "supply":
        showNewSupply()
    elif type == "print":
        showPrint()

def btnAddNew(father, icon, size, text, col, type):

    text=text.upper()

    icon = CTkImage(light_image=Image.open(icon), dark_image=Image.open(icon), size=size)
    
    buttonC = CTkButton(father, image=icon, command=lambda:show(type), text=text, font=("Roboto", 14), fg_color="#FFF", text_color="gray23", anchor="center", height=50, hover_color="gray89")
    buttonC.grid(row=0, column=col, padx=3)

    buttonC.configure(cursor="hand2")