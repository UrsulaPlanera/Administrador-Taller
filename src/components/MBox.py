from customtkinter import CTkToplevel
from tkinter import Label

def MBox(title, message):

    titleMayus = title.upper()
    messageMayus = message.upper()

    windowMBox = CTkToplevel(fg_color="#FFF")

    windowMBox.minsize(300,300)
    windowMBox.maxsize(300,300)

    windowMBox.title(titleMayus)
    windowMBox.grab_set()
    windowMBox.after(200, lambda: windowMBox.iconbitmap("static/ico.ico"))
    windowMBox.rowconfigure(0, weight=0)
    windowMBox.rowconfigure(1, weight=1)
    windowMBox.columnconfigure(0, weight=1)

    if(titleMayus=="ERROR"):
        motive = Label(windowMBox, text="⚠", font=("Roboto",30), pady=10, bg="#FFF", fg="firebrick3")
    elif(titleMayus=="INFO"):
        motive = Label(windowMBox, text="ⓘ", font=("Roboto",25), pady=10, bg="#FFF", fg="RoyalBlue1")
    elif(titleMayus=="SUCCESS"):
        motive= Label(windowMBox, text="✔", font=("Roboto",30), pady=10, bg="#FFF", fg="#3AB564")
    
    iconMotive = motive
    iconMotive.grid(row=0, column=0)

    bodyMessage = Label(windowMBox, text=messageMayus, font=("Roboto", 10), bg="#FFF", fg="gray33", wraplength=250)
    bodyMessage.grid(row=1, column=0)

    windowMBox.mainloop()