import sqlite3

from src.components.MBox import MBox

def insertChangeOnService(root, id, val1, val2, val3, val4, val5, val6):

    conn = sqlite3.connect("./dbconection/ma.db")
    cursor =conn.cursor()
    instruction = f"UPDATE clientes SET patente='{val1}', marca='{val2}', modelo='{val3}', nombre='{val4}', fecha='{val5}', descripcion='{val6}' WHERE id_registro='{id}';"
    cursor.execute(instruction)
    conn.commit()
    conn.close()
    root.destroy()
    return MBox("info", f"se han modificado los registros\npatente: {val1}\nmarca: {val2}\nmodelo: {val3}\nnombre: {val4}\nfecha: {val5}\ndescripcion: {val6}")

def insertChangeOnSupply(root, id, val1, val2, val3, val4, val5, val6):

    conn = sqlite3.connect("./dbconection/ma.db")
    cursor =conn.cursor()
    instruction = f"UPDATE insumos SET insumo_nombre='{val1}', costo_unidad='{val2}', precio_venta='{val3}', ganancia='{val4}', dinero_invertido='{val5}', stock='{val6}' WHERE id_insumo='{id}';"
    cursor.execute(instruction)
    conn.commit()
    conn.close()
    root.destroy()
    return MBox("info", f"se han modificado los registros\nnombre de insumo: {val1}\ncosto unidad: {val2}\nprecio de venta: {val3}\nganancia: {val4}\ndinero invertido: {val5}\nstock: {val6}")