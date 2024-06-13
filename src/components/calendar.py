from customtkinter import CTkToplevel, CTkButton
from tkcalendar import Calendar

def showCalendar(entry, fontRezise):
        calendarC = CTkToplevel(fg_color="#FFF")
        calendarC.grab_set()

        calendarC.resizable(False, False)

        calendarC.title("CALENDARIO")
        calendarC.after(200, lambda: calendarC.iconbitmap("static/ico.ico"))

        calendarC.columnconfigure(0, weight=0)

        calendar = Calendar(calendarC, font=fontRezise, selectmode="day", date_pattern="dd/mm/yy", background="#FFF", bordercolor="gray89", foreground="gray23", headersbackground="#FFF", headersforeground="gray23", selectforeground="#FFF", selectbackground="#029BD5", headerbackground="#FFF", headerforeground="gray23", othermonthbackground="#FFF", othermonthforeground="gray23", othermonthwebackground="#FFF", othermonthweforeground="gray23", weekendbackground="#FFF", weekendforeground="gray23", disableddaybackground="#FFF", disableddayforeground="gray23")
        calendar.grid(row=0, column=0, sticky="nswe")

        submitBtn = CTkButton(calendarC, text="ACEPTAR", font=fontRezise, text_color="#FFF", fg_color="gray89", hover_color="#029BD5", corner_radius=0, command=lambda:getDate())
        submitBtn.grid(row=1, column=0, sticky="nswe")
        submitBtn.configure(cursor="hand2")

        def getDate():
            dateSelect = calendar.get_date()
            entry.delete(0, "end")
            entry.insert(0, dateSelect)
            calendarC.destroy()

        calendarC.mainloop()