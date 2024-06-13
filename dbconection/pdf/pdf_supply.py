from fpdf import FPDF
from fpdf.fonts import FontFace
from datetime import datetime
import os
from uuid import uuid4
from src.components.MBox import MBox

fecha = datetime.today().strftime("%d/%m/%Y")

def pdfSupply(data):
    class PDF(FPDF):
        def header(self):
            width = self.w
            self.line(20,20,20,45)
            self.line(20,20,width-20,20)
            self.line(width-20,20,width-20,45)
            self.line(20,45,width-20,45)
            self.line((width/3)*2-20,20,(width/3)*2-20,45)
            self.image("dbconection/pdf/logo.png", x=(width/3)-(width/3)/3-5, y=25, h=16)
            self.set_font("helvetica", "B", 12)
            self.text((width/3)*2-10, 29+3.175, f"INSUMOS")
            self.set_font("helvetica", "", 9)
            self.text((width/3)*2-10, 33+3.175, f"FECHA DE EMISION: {fecha}")
            self.ln(30)

        def footer(self):
            self.set_y(-15)
            self.set_font("helvetica", "", 9)
            self.cell(0, 10, f"Página {self.page_no()}/{{nb}}", align="RIGHT")

    pdf = PDF()
    pdf.set_margins(20,20,20)
    pdf.add_page()
    pdf.set_font("helvetica", "", 9)

    TABLE_DATA = data

    style = FontFace(emphasis="BOLD", fill_color=(227,227,227))
    with pdf.table(text_align=("LEFT", "LEFT", "LEFT", "LEFT", "LEFT", "LEFT"), headings_style=style) as table:
        for data_row in TABLE_DATA:
            row = table.row()
            for datum in data_row:
                row.cell(datum)

    uid = uuid4()
    path_download = os.path.join(os.path.expanduser('~'), 'Downloads')
    pdf.output(f"{path_download}/INSUMOS-{uid}.pdf")
    MBox("success", "pdf generado correctamente. puede encontrarlo en descargas.")