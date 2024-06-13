import sqlite3

from src.components.MBox import MBox

def deleteService(root, id_registro):
    try:
        conn = sqlite3.connect("./dbconection/ma.db")
        cursor = conn.cursor()
        instruction = f"DELETE FROM clientes WHERE id_registro='{id_registro}';"
        cursor.execute(instruction)
        conn.commit()
        conn.close()
        root.destroy()
        return MBox("success", "service eliminado con éxito.")
    except:
        return MBox("error", "error al eliminar el registro.")

def deleteSupply(root, id_insumo):
    try:
        conn = sqlite3.connect("./dbconection/ma.db")
        cursor = conn.cursor()
        instruction = f"DELETE FROM insumos WHERE id_insumo='{id_insumo}'"
        cursor.execute(instruction)
        conn.commit()
        conn.close()
        root.destroy()
        return MBox("success", "insumo eliminado con éxito.")
    except:
        return MBox("error", "error al eliminar el registro.")