from customtkinter import CTkToplevel, CTkLabel, CTkFrame, CTkButton

from dbconection.deleteData import deleteService, deleteSupply

def acceptDelete(fontRezise, typeOf, id, val1, val2, val3, val4, val5, val6):

    acceptDeleteC = CTkToplevel(fg_color="#FFF")
    acceptDeleteC.grab_set()

    acceptDeleteC.minsize(300,300)
    acceptDeleteC.maxsize(300,300)

    acceptDeleteC.title("ELIMINAR")
    acceptDeleteC.after(200, lambda: acceptDeleteC.iconbitmap("static/ico.ico"))
    acceptDeleteC.columnconfigure(0, weight=1)
    acceptDeleteC.rowconfigure(0, weight=1)

    message = CTkLabel(acceptDeleteC, font=fontRezise, text=f"SE ELIMINARA EL REGISTRO:\n{val1}\n{val2}\n{val3}\n{val4}\n{val5}\n{val6}", wraplength=250, text_color="gray23", fg_color="#FFF")
    message.grid(row=0, column=0, sticky="nswe", padx=10)

    def delete():
        if typeOf == "CLIENT":
            deleteService(acceptDeleteC,id)
        elif typeOf == "SUPPLY":
            deleteSupply(acceptDeleteC,id)

    def cancel():
        acceptDeleteC.destroy()

    btnFrame = CTkFrame(acceptDeleteC, fg_color="#FFF")
    btnFrame.grid(row=1, column=0, sticky="nswe", padx=10, pady=10)
    btnFrame.columnconfigure(0, weight=1)
    btnFrame.columnconfigure(0, weight=1)

    btnDelete = CTkButton(btnFrame, command=lambda:delete(), text="ACEPTAR", font=fontRezise, text_color="#FFF", fg_color="gray89", hover_color="firebrick3", corner_radius=0)
    btnDelete.grid(row=1, column=0, sticky="nswe", padx=2)
    btnDelete.configure(cursor="hand2")

    btnCancel = CTkButton(btnFrame, command=lambda:cancel(), text="CANCELAR", font=fontRezise, text_color="#FFF", fg_color="gray89", hover_color="SteelBlue2", corner_radius=0)
    btnCancel.grid(row=1, column=1, sticky="nswe", padx=2)
    btnCancel.configure(cursor="hand2")