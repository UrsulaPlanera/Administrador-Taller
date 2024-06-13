from customtkinter import CTkImage, CTkLabel
from PIL import Image

def enterpriseLogo(father, row, sticky):
    iconEnterprise = CTkImage(light_image=Image.open("static/EnterpriseLogoUSABLE.png"), dark_image=Image.open("static/EnterpriseLogoUSABLE.png"), size=(250, 72))
    enterpriseLogoFrame = CTkLabel(father, image=iconEnterprise, text="")
    enterpriseLogoFrame.grid(row=row, column=0, sticky=sticky, pady = 50)