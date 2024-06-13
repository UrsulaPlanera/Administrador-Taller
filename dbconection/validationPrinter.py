from dbconection.getData import getData, getForValue, getToIdClient,getToIdSupply, getSupplies
from dbconection.pdf.pdf_client import pdfClient
from dbconection.pdf.pdf_supply import pdfSupply

from src.components.MBox import MBox

def validationToPrintSupplies():
    data = getData("insumos")
    print(data)

def validationToPrintCustomerHistory(patent):
    patentMayus = patent
    data = getForValue("clientes", "patente", patentMayus)
    if(len(data)==0):
        MBox("error","No se han encontrado registros con la patente indicada. Revise los caracteres ingresados.")
    else:
        patent = data[0][1]
        brand = data[0][2]
        model = data[0][3]
        description=[["FECHA", "DESCRIPCION"]]
        for row in data:
            descriptionPart = [row[5],row[6]]
            description.append(descriptionPart)
        pdfClient(patent,brand,model,description)

def validationPrintCustomerSimple(id):
    data = getToIdClient(id)
    patent = data[0][1]
    brand = data[0][2]
    model = data[0][3]
    description=[["FECHA", "DESCRIPCION"]]
    for row in data:
        descriptionPart = [row[5],row[6]]
        description.append(descriptionPart)
    pdfClient(patent,brand,model,description)

def validationToPrintOnlySupply(id):
    data = getToIdSupply(id)
    description = [["NOMBRE DE INSUMO", "COSTO DE UNIDAD", "PRECIO DE VENTA", "GANACIA", "DINERO INVERTIDO", "STOCK"]]
    for row in data:
        descriptionPart = [row[1], row[2], row[3], row[4], row[5], row[6]]
        description.append(descriptionPart)
    pdfSupply(description)

def validationToPrintSupplies():
    data = getSupplies()
    if(len(data)==0):
        MBox("error","No se han encontrado registros con la patente indicada. Revise los caracteres ingresados.")
    else:
        description = [["NOMBRE DE INSUMO", "COSTO DE UNIDAD", "PRECIO DE VENTA", "GANACIA", "DINERO INVERTIDO", "STOCK"]]
        for row in data:
            descriptionPart = [row[1], row[2], row[3], row[4], row[5], row[6]]
            description.append(descriptionPart)
        pdfSupply(description)